import cv2
import numpy as np
import mediapipe as mp

class GestureDrawing:
    def __init__(self):
        # Initialize webcam
        self.cap = cv2.VideoCapture(0)
        
        # Set up MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # Create canvas for drawing
        self.canvas = None
        self.previous_point = None
        
        # Drawing settings
        self.drawing_color = (255, 255, 255)  # White color
        self.brush_thickness = 5
        self.eraser_thickness = 40
        
        # Mode settings
        self.drawing_mode = True  # True for drawing, False for eraser
        
        # Create window and trackbars
        cv2.namedWindow('Gesture Drawing')
        cv2.createTrackbar('R', 'Gesture Drawing', 255, 255, self.nothing)
        cv2.createTrackbar('G', 'Gesture Drawing', 255, 255, self.nothing)
        cv2.createTrackbar('B', 'Gesture Drawing', 255, 255, self.nothing)
        cv2.createTrackbar('Thickness', 'Gesture Drawing', 5, 50, self.nothing)

    def nothing(self, x):
        pass

    def get_finger_position(self, hand_landmarks, image):
        # Get index finger tip and middle finger tip coordinates
        index_finger_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        middle_finger_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        index_finger_mcp = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP]
        
        h, w, _ = image.shape
        
        # Convert coordinates
        index_tip = (int(index_finger_tip.x * w), int(index_finger_tip.y * h))
        middle_tip = (int(middle_finger_tip.x * w), int(middle_finger_tip.y * h))
        palm_pos = (int(index_finger_mcp.x * w), int(index_finger_mcp.y * h))
        
        return index_tip, middle_tip, palm_pos

    def run(self):
        while self.cap.isOpened():
            success, image = self.cap.read()
            if not success:
                break
                
            # Flip the image horizontally
            image = cv2.flip(image, 1)
            
            # Initialize canvas if not created
            if self.canvas is None:
                self.canvas = np.zeros_like(image)
            
            # Convert BGR to RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Process hand landmarks
            results = self.hands.process(image_rgb)
            
            # Get current color and thickness from trackbars
            r = cv2.getTrackbarPos('R', 'Gesture Drawing')
            g = cv2.getTrackbarPos('G', 'Gesture Drawing')
            b = cv2.getTrackbarPos('B', 'Gesture Drawing')
            self.drawing_color = (b, g, r)  # BGR format
            self.brush_thickness = cv2.getTrackbarPos('Thickness', 'Gesture Drawing')
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw hand landmarks
                    self.mp_draw.draw_landmarks(
                        image,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )
                    
                    # Get finger positions
                    index_tip, middle_tip, palm_pos = self.get_finger_position(hand_landmarks, image)
                    
                    # Calculate distance between index and middle finger tips
                    finger_distance = np.sqrt(
                        (index_tip[0] - middle_tip[0])**2 + 
                        (index_tip[1] - middle_tip[1])**2
                    )
                    
                    # Draw or erase based on finger positions
                    if finger_distance < 50:  # Fingers pinched together - drawing mode
                        if self.previous_point:
                            if self.drawing_mode:
                                cv2.line(
                                    self.canvas,
                                    self.previous_point,
                                    index_tip,
                                    self.drawing_color,
                                    self.brush_thickness
                                )
                            else:
                                cv2.circle(
                                    self.canvas,
                                    index_tip,
                                    self.eraser_thickness,
                                    (0, 0, 0),
                                    -1
                                )
                        self.previous_point = index_tip
                    else:
                        self.previous_point = None
                    
                    # Change mode based on palm position
                    cv2.circle(image, palm_pos, 10, (0, 255, 0), -1)
                    if palm_pos[1] < 100:  # Palm near top of screen
                        self.drawing_mode = not self.drawing_mode
                        cv2.waitKey(500)  # Delay to prevent rapid switching
            
            # Combine canvas with camera feed
            mask = cv2.cvtColor(self.canvas, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)
            inv_mask = cv2.bitwise_not(mask)
            
            bg = cv2.bitwise_and(image, image, mask=inv_mask)
            fg = cv2.bitwise_and(self.canvas, self.canvas, mask=mask)
            
            combined_image = cv2.add(bg, fg)
            
            # Add mode indicator
            mode_text = "Drawing Mode" if self.drawing_mode else "Eraser Mode"
            cv2.putText(
                combined_image,
                mode_text,
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )
            
            # Show the result
            cv2.imshow('Gesture Drawing', combined_image)
            
            # Handle keyboard inputs
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC to exit
                break
            elif key == ord('c'):  # 'c' to clear canvas
                self.canvas = np.zeros_like(image)
            elif key == ord('s'):  # 's' to save canvas
                cv2.imwrite('drawing.png', self.canvas)
            
        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = GestureDrawing()
    app.run()