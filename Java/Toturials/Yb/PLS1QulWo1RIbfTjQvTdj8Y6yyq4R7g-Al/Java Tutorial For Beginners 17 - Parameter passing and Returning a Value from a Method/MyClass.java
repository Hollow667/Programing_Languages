public class MyClass {
  public static void main(String[] args)
  {
    sayHello("ahmad");
    int res = Add(1, 2);
    System.out.print(res);
  }

  public static void sayHello(String name)
  {
    System.out.println("Hello "+ name);
  }

  public static int Add (int a, int b)
  {
    System.out.println(a+b);
    return a+b;
  }
}