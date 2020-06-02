import java.util.Date;
 // ignore warnings while compiling
public class MyClass
{
  public static void main(String[] args)
  {
    Date date = new Date();
    System.out.println(date.toString());
    System.out.println(date.getTime());
    System.out.println(date.getMonth());
    System.out.println(date.getYear() + 1900);
    System.out.println(date.getDay());
    System.out.println(date.getHours());
  }
}