import java.util.ArrayList;
public class ArrayList_in_JAVA {
  public static void main(String[] args){
    ArrayList <String> Etudiens = new ArrayList <String> (); // decleration
    
    //  aujouter des elements

    Etudiens.add("Ahmad");
    Etudiens.add("Sam");
    Etudiens.add("Michle");
    Etudiens.add("Pierr");

    // voir le ArrayList

    System.out.print(Etudiens);

    for(String i: Etudiens)
    {
      System.out.println(i);
    }
  
    for(int j = 0; j < Etudiens.size(); j++)
    {
      System.out.print(j);System.out.print(":" + Etudiens.get(j) + "\n");
    }

    //  supprimer un element

    Etudiens.remove(1);

    System.out.print(Etudiens);

    // modifier un element

    Etudiens.set(0, "Mark"); 

    System.out.print(Etudiens);

    // supprimer tout les elements

    Etudiens.clear();
  }
}

