public class methods {
  public static void hi()
  { System.out.println("Show a message"); }

  public static int sum(int a, int b)
  { return a + b; }

  public static void main(String args[])
  {
    hi();
    System.out.println("1 + 2 = " +  sum(1,2));
  }
}