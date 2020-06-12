import java.util.Scanner;
public class code
{
  public static void main(String[] args)
  {
    int i;int num;
    Scanner scan = new Scanner(System.in);

    System.out.print("What mutiplication table do you want to see: ");
    num = scan.nextInt();
    for(i = 0; i<= 10; i++){System.out.println(num + " * " + i + " = " + num*i);} 
  }
}