import cv2
import mediapipe as mp
import numpy as np

class FingerCounter:
    def __init__(self):
        # Initialize mediapipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]  # finger tip landmarks

    def count_fingers(self, image):
        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Process the image and detect hands
        results = self.hands.process(image_rgb)
        
        fingers = []
        
        if results.multi_hand_landmarks:
            # Get the first hand detected
            hand_landmarks = results.multi_hand_landmarks[0]
            
            # Draw hand landmarks
            self.mp_draw.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            
            # Get hand landmarks as list
            landmarks = []
            for lm in hand_landmarks.landmark:
                h, w, _ = image.shape
                landmarks.append([int(lm.x * w), int(lm.y * h)])
            
            # Check thumb
            if landmarks[4][0] < landmarks[3][0]:
                fingers.append(1)
            else:
                fingers.append(0)
            
            # Check other fingers
            for id in range(1, 5):
                if landmarks[self.tip_ids[id]][1] < landmarks[self.tip_ids[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            
            # Calculate total fingers
            total_fingers = fingers.count(1)
            
            # Draw rectangle and display finger count
            cv2.rectangle(image, (20, 20), (150, 120), (0, 255, 0), -1)
            cv2.putText(image, str(total_fingers), (45, 95), cv2.FONT_HERSHEY_PLAIN,
                        6, (255, 0, 0), 5)
            
        return image

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    detector = FingerCounter()
    
    while True:
        # Read frame from webcam
        success, image = cap.read()
        if not success:
            print("Failed to read from webcam")
            break
            
        # Flip the image horizontally for a later selfie-view display
        image = cv2.flip(image, 1)
        
        # Process the image and count fingers
        image = detector.count_fingers(image)
        
        # Display the image
        cv2.imshow("Finger Counter", image)
        
        # Break loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()