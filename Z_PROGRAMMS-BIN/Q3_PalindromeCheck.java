import java.util.*;
class Q3_PalindromeCheck {
    static boolean isPalindrome(int num) {
        String numStr = String.valueOf(num);
        int left = 0;
        int right = numStr.length() - 1;
        
        while (left < right) {
            if (numStr.charAt(left) != numStr.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList<>();
        
        System.out.println("Enter 10 numbers (3 digits each):");
        for (int i = 0; i < 10; i++) {
            int num = scanner.nextInt();
            numbers.add(num);
        }
        
        System.out.println("\nNumbers with palindrome check:");
        for (int num : numbers) {
            System.out.println(num + " - " + isPalindrome(num));
        }
    }
}