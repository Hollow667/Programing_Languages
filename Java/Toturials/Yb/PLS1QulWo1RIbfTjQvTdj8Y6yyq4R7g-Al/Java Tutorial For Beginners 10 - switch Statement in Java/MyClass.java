public class MyClass {
  public static void main(String[] args)
  {
    int score = 90;
    switch (score)
    {
    case 100:
    case 90:
      System.out.println("Very good");
      break;
    case 60:
      System.out.println("good");
      break;
    case 40:
      System.out.println("Ok");
      break;
    default :
      System.out.println("the grades are not defined");
      break;
    }
  }
}