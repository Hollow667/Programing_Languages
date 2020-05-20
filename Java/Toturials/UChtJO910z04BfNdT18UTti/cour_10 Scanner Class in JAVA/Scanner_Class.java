import java.util.Scanner;

/* 
* Type de Donnees
* -------------------------
* nextBoolean()	Reads a boolean value from the stdin
* nextByte()	Reads a byte value from the stdin
* next Double() 	Reads a double from the stdin
* nextFloat() 	Reads a float value from the stdin
* nextInt()		Reads an integer value from the stdin 
* nextLine()	Reads a String value from the stdin
* nextLong()	Reads a long value from the stdin
* nextShort()	Reads a short value from the stdin
*/

public class Scanner_Class{
  public static void main(String[] args){
    Scanner app = new Scanner(System.in);
    
    System.out.println("enter intger ");
    int integer_input = app.nextInt();
    System.out.println(integer_input);
    
    System.out.println("enter Double ");
    double double_input = app.nextDouble();
    System.out.println(double_input);
    
    System.out.println("enter line ");
    String str_input;
    str_input = app.nextLine();str_input = app.nextLine();
    System.out.println(str_input);
    
  }
}