import java.util.*;
public class pallendrome{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        String rev = "";
        int n = str.length();
        for(int i = n-1;i>=0;i--){
            rev += str.charAt(i);
        }
        if(str.equals(rev)) System.out.println(str + " its a pallendrome");
        else System.out.println(str + " not a pallendrome");
        sc.close();
    }
}