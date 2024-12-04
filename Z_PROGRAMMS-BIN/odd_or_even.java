import java.util.*;
class odd_or_even {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int obj = sc.nextInt();
        String type = (obj % 2 == 0) ? "even" : "odd";
        System.out.println(type);
    }
}