public class class_et_objects {
  public static class car
  {
    int id;
    String marque;
    String modele;
    
    public void print()
    {
      System.out.println("Car id: " + id + ", marque: " + marque + ", modele: "+ modele + "."); 
    }
  }
  public static void main(String[] args) 
  {
    car vehicule = new car();
    vehicule.id = 15;
    vehicule.marque = "la marque";
    vehicule.modele = "la modele";
    vehicule.print();
  }
}