/* 
 * class extends classes
 * interface extends interfaces
 * class implements interfaces
 */
public class MyClass
{
  public static interface Bank
  {
    public int get_int();
  }
  public static class Bank_ABC implements Bank
  {
    public int get_int()
    {
      return 5;
    }
  }
  public static void main(String[] args)
  {
    Bank_ABC B = new Bank_ABC();
    System.out.println(B.get_int());
  }
}