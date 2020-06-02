import java.io.File;
import java.io.PrintWriter;
import java.io.IOException;
public class MyClass
{
  public static void main(String[] args)
  {
    File file = new File("filename.txt");
      try 
      {
        if(file.exists()) {file.createNewFile();}
        PrintWriter pw = new PrintWriter(file);
        pw.println("First Line");
        pw.close();
      } catch (IOException e)  {
      System.out.print(e);
     } 
  }
}