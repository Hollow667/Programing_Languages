import java.util.Scanner;

public class code
{

  public static void main(String[] args)
  {
    Scanner scan = new Scanner(System.in);

    int i = 0;
    while(scan.nextInt() != 0)
    {
      i += 1;
    }
  System.out.println(i);
  }
}