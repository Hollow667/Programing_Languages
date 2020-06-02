import java.util.LinkedList;
public class MyClass
{
  public static void main(String[] args)
  {
    // create a linked list
    LinkedList<String> lList = new LinkedList<String>();
    
    // adding elements
    lList.add("Mark");
    lList.add("Johan");
    lList.addFirst("Mickle");
    lList.addLast("Lissa");
    lList.add(0, "Bin"); // index, value

    // change elelemts
    lList.set(1, "Jack");
    // show elements
    for(String x : lList) { System.out.println(x); }

    // get size
    System.out.println(lList.size());

    // remove elements
    lList.remove(2);
    lList.removeFirst();
    lList.removeLast();
    lList.clear();

  }
}