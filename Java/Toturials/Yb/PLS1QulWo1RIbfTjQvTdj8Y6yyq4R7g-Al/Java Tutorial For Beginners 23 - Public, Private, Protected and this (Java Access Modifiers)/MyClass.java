public class MyClass {
  public static class Person
  {
  }
  public static class Student extends Person
  {
      public String name;
      public int age;
      private int password;
      public void setPassword(int password)
      {
        this.password = password;
      }
      public int getPassword()
      {
        return password;
      }
      void print()
      {
        System.out.println("Student " + name + ", is " + age + " years old");
      }
  }
  public static void main(String[] args)
  {
      Student mike = new Student();
      mike.name = "Mike";
      mike.age = 20;
      mike.setPassword(0000);
      mike.print();
  }
}