import java.util.Scanner;
public class code
{
  public static void main(String[] args)
  {
    Scanner scan = new Scanner(System.in);
    String name = "";
    int age = 0;

    System.out.print("Please Enter your name: ");
    name = scan.next();
    System.out.print("Please Enter your age: ");
    age = scan.nextInt();

    System.out.println("Your name is " + name + ", your age is " + age + " years old.");
  }
}