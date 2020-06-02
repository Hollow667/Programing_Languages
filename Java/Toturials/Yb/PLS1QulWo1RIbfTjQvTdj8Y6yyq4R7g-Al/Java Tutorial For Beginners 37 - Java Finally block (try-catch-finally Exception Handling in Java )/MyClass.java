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
    } finally
    {
      // will always be excuted except if you call System.exit() in any the catch statement or return statement if in a function
      System.out.println("Exception handeled");
    }
  }
}