import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class MyClass
{
  public static void main(String[] args)
  {
    BufferedReader br = null;
    try
    {
      br = new BufferedReader(new FileReader("file.txt")); // do not froget to close it
      String line; 
      while((line = br.readLine()) != null) {System.out.println(line);}
    } catch(IOException e) {
      System.out.println(e);
    } finally { 
      System.out.println("Done");}
      try {br.close();} catch (IOException e) {System.out.println(e);}
    }
}
