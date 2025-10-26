import java.util.*;
class Student {
    String name;
    int score;
    Student(String n,int s){name=n;score=s;}
}
class SortStudents {
    public static void main(String[] args) {
        List<Student> list=new ArrayList<>();
        list.add(new Student("A",90));
        list.add(new Student("B",75));
        list.add(new Student("C",85));
        Collections.sort(list,(x,y)->y.score-x.score);
        for(Student s:list) System.out.println(s.name+" "+s.score);
    }
}
