public class code{
  public static void main(String[] args)
  {

    String[] rec= new String[2];
    
    // rec[2] = "name"; // this will through an error

    try{
      rec[2] = "name";
    } catch (Exception ex)
    {
      System.out.println(ex.getMessage());
    }
  }
}