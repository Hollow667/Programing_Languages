public class MyClass {
  public static void main(String[] args)
  {
    String myString = "Hello Wolrd";
    
    // get string length
    int len = myString.length();

    // change case
    System.out.println(myString.toLowerCase());
    System.out.println(myString.toUpperCase());

    // replace
    System.out.println(myString.replace('e', 'a'));

    // 
    System.out.println(myString.indexOf(" "));

  }
}