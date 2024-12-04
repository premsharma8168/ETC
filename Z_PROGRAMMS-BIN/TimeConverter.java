import java.util.Scanner;

public class TimeConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter time in 12-hour format (hh:mm AM/PM): ");
        String input = scanner.nextLine();
        scanner.close();

        String[] parts = input.split(":");
        int hours = Integer.parseInt(parts[0]);
        int minutes = Integer.parseInt(parts[1].substring(0, 2));
        String period = parts[1].substring(3).toUpperCase();

        if (period.equals("PM") && hours != 12) {
            hours += 12;
        } else if (period.equals("AM") && hours == 12) {
            hours = 0;
        }

        System.out.printf("%02d:%02d", hours, minutes);
    }
}