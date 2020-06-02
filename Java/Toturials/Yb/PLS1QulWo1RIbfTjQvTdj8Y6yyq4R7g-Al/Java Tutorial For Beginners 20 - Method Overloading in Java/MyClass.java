public class MyClass {
  public static int add(int a, int b)
  {
    System.out.println("Add for ints");
    return a + b;
  }
  public static double add(double a, double b)
  {
    System.out.println("Add for doubles");
    return a + b;
  }
  public static String add(String a, String b)
  {
    System.out.println("Add for strings");
    return a + b;
  }
  
  public static void main(String[] args)
  {
    System.out.println(add(1, 1));
    System.out.println(add(1.0, 1.0));
    System.out.println(add("Str1 ", "Str2"));
  }
}