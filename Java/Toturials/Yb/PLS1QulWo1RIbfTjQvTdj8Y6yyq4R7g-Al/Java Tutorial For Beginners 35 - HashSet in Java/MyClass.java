import java.util.*;
public class MyClass
{
  public static void main(String[] args)
  {
    HashSet<String> names = new HashSet<String>(); // no repeated elements
    names.add("Mark"); // this will be deleted since we repeat the name again in the third add
    names.add("tom");
    names.add("Mark");
    names.add("jack");
    names.add("patrik");

    Iterator<String> itr = names.iterator();
    while(itr.hasNext())
    {
      System.out.println(itr.next());
    }
    System.out.println("");

/*    while(itr.hasPrevious())
    {
      System.out.println(itr.previous());
    }*/
  }
}