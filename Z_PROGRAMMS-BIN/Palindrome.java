public class Palindrome {
    public static void main(String[] args) {
        String str = "Sharmaji";
        String reversed = new StringBuilder(str).reverse().toString();
        System.out.println(reversed);
    }
}