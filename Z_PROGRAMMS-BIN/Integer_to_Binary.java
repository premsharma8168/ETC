import java.util.*;
public class Integer_to_Binary {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to convert to binary: ");
        int number = sc.nextInt();
        System.out.print("Binary using manual method: " + manualBinaryConversion(number));
        sc.close();
    }
    public static String manualBinaryConversion(int num) {
        StringBuilder binary = new StringBuilder();
        while(num > 0) {
            binary.append(num % 2);
            num = num / 2;
        }
        return binary.reverse().toString();
    }
}