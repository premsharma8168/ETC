public class LcmHcf {
    protected int n1;
    protected int n2;

    public LcmHcf(int n1, int n2) {
        this.n1 = n1;
        this.n2 = n2;
    }

    public void sumofDigits() {
        int sum1 = calculateSumOfDigits(n1);
        int sum2 = calculateSumOfDigits(n2);
        System.out.println("Sum of digits of " + n1 + " is: " + sum1);
        System.out.println("Sum of digits of " + n2 + " is: " + sum2);
    }

    private int calculateSumOfDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        } 
        return sum;
    }

    public void printAverage() {
        double average = (n1 + n2) / 2.0;
        System.out.println("Average of " + n1 + " and " + n2 + " is: " + average);
    }

    public void lcmhcf() {
        int hcf = calculateHCF(n1, n2);
        int lcm = (n1 * n2) / hcf;
        System.out.println("HCF of " + n1 + " and " + n2 + " is: " + hcf);
        System.out.println("LCM of " + n1 + " and " + n2 + " is: " + lcm);
    }

    private int calculateHCF(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static void main(String[] args) {
        LcmHcf obj = new LcmHcf(12, 18);

        obj.sumofDigits();
        obj.printAverage();
        obj.lcmhcf();
    }
}
