public class MyClass
{
  public static void main(String[] args)
  {
    try
    {
      // int a = 100 / 0; // throw ArithmeticException 
      int b[] = new int[2];
      System.out.println(b[4]); // throw Exception 
    } catch (ArithmeticException e) {
      System.out.println(e);
      System.out.println("0--------------------------");
    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println(e);
      System.out.println("2--------------------------");
    } catch (Exception e) {
      // must be the last one
      System.out.println(e);
      System.out.println("1--------------------------");
    } 
  }
}