import java.util.Scanner;
public class MyClass {
  public static void main(String[] args)
  {
    Scanner scan = new Scanner (System.in);

    System.out.println("Enter some number");
    int user_input_number = scan.nextInt();
    System.out.println("The entered value is " + user_input_number);

    System.out.println("Enter a double");
    double user_input_double = scan.nextDouble();
    System.out.println("The entered value is " + user_input_double);

    System.out.println("Enter a string");
    scan.nextLine();
    String user_input_string = scan.nextLine();
    System.out.println("The entered value is " + user_input_string);

  }
}


