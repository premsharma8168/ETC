import java.util.*;

class Q1_PrimeFactors {
    static String findPrimeFactors(int num) {
        List<Integer> factors = new ArrayList<>();
        while (num % 2 == 0) {
            factors.add(2);
            num = num / 2;
        }
        for (int i = 3; i <= Math.sqrt(num); i += 2) {
            while (num % i == 0) {
                factors.add(i);
                num = num / i;
            }
        }
        if (num > 2) {
            factors.add(num);
        }
        return factors.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList<>();
        
        System.out.println("Enter 5 numbers:");
        for (int i = 0; i < 5; i++) {
            numbers.add(scanner.nextInt());
        }
        
        Collections.sort(numbers);
        
        System.out.println("Numbers with their prime factors:");
        for (int num : numbers) {
            System.out.println(num + " - Prime factors: " + findPrimeFactors(num));
        }
    }
}