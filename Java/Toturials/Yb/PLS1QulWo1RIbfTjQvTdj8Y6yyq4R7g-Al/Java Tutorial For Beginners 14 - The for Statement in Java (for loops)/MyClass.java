public class MyClass {
  public static void main(String[] args)
  {
    int[] myintarray = {1, 2, 3, 4, 5};
    for (int i = 0; i <  5; i++)
    {
      System.out.println(myintarray[i]);
    }
    for (int element : myintarray)
    {
      System.out.println(element);
    }

  }
}