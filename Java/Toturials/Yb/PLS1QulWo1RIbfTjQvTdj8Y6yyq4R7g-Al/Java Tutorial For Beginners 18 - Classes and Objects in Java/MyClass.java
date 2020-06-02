public class MyClass {
  public static class Student
  {
    int id;
    String name;
    int age;
  
    public void set_id(int id)
    {
      this.id = id;
    }
    public void set_name(String name)
    {
      this.name = name;
    }
    public void set_age(int age)
    {
      this.age = age;
    }

    public int get_id()
    {
      return this.id;
    }
    public String get_name()
    {
      return this.name;
    }
    public int get_age()
    {
      return this.age;
    }
  }

  public static void main(String[] args)
  {
    Student mark = new Student();
    
    mark.id = 2;
    mark.name = "Tim";
    mark.age = 18;

    System.out.println(mark.name + " is " + mark.age + " years old");

    Student tim = new Student();
    
    tim.set_id(1);
    tim.set_name("Mark");
    tim.set_age(15);

    System.out.println(tim.get_name() + " is " + tim.get_age() + " years old");
  }
}