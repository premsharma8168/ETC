import java.util.*;
class Q2_EmployeeData {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Map<Integer, String> employees = new HashMap<>();
        
        System.out.println("Enter 10 employee records (ID and Name):");
        for (int i = 0; i < 10; i++) {
            System.out.print("Enter ID: ");
            int id = scanner.nextInt();
            scanner.nextLine();
            System.out.print("Enter Name: ");
            String name = scanner.nextLine();
            employees.put(id, name);
        }
        
        employees.entrySet()
            .stream()
            .sorted((e1, e2) -> {
                String name1 = e1.getValue();
                String name2 = e2.getValue();
                return Character.compare(
                    name1.charAt(name1.length() - 1),
                    name2.charAt(name2.length() - 1)
                );
            })
            .forEach(entry -> System.out.println(
                "ID: " + entry.getKey() + ", Name: " + entry.getValue()
            ));
    }
}
