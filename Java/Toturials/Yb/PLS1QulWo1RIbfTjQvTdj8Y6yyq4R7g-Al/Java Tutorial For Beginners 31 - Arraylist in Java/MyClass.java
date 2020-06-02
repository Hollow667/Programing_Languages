import java.util.ArrayList;
public class MyClass
{

  public static void main(String[] args)
  {
    // const array size
    int simple_array[] = new int[5]; /*or {1, 2, 3, 4, 5}*/

    // sizable array
    ArrayList<Integer> myList= new ArrayList<Integer>(5);
    myList.add(1);
    myList.add(2);
    myList.add(3);
    
    // show array
    for(Integer x : myList) {System.out.println(x);}
    
    // get size
    System.out.println("size = " + myList.size());

    // indixing
    myList.set(0, 2);
    System.out.println("After changing 0're elemet");
    for(Integer x : myList) {System.out.println(x);}

    // remove element at an index
    myList.remove(2);
    System.out.println("after removing 2'nd elemet");
    for(Integer x : myList) {System.out.println(x);}

    // clear the ArrayList
    myList.clear();
    System.out.println("After clearing the ArrayList");
    System.out.println("size = " + myList.size());

    // trim the ArrayList to the size of non-nul elements
    System.out.println("After trimimg");
    myList.trimToSize();
    System.out.println("size = " + myList.size());
  }
}