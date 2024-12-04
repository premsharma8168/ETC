public class ReverseString {
    public static void main(String[] args) {
        String str = "PremSharma";
        StringBuilder reversed = new StringBuilder(str).reverse();
        System.out.println(reversed);
    }
}