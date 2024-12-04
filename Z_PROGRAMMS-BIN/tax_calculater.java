import java.util.*;
public class tax_calculater {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your Income in Rupees:");
        int income = sc.nextInt();
        int tax;
        if (income <= 300000)
        {
            System.out.println("You have to Pay 0 % Tax");
            tax = 0;
        }
        else if (income >= 300001 && income <= 700000)
        {
            System.out.println("You have to Pay 5 % Tax");
            tax = (int) (income*0.05);
        }
        else if (income >= 700001 && income <= 1000000)
        {
            System.out.println("You have to Pay 10 % Tax");
            tax = (int) (income*0.1);
        }
        else if (income >= 1000001 && income <= 1200000)
        {
            System.out.println("You have to Pay 15 % Tax");
            tax = (int) (income*0.15);
        }
        else if (income >= 1200001 && income <= 1500000)
        {
            System.out.println("You have to Pay 20 % Tax");
            tax = (int) (income*0.2);
        }
        else { 
            System.out.println("You have to Pay 30 % Tax");
            tax = (int) (income*0.3);
        }
        sc.close();
        System.out.println("You have to Pay : "+tax+" as your Income tax");
    }
}