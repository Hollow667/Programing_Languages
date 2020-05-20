public class access_modeifiers
{
  public static void main(String args[])
  {
    car v = new car(15,"A", "B");
    v.print();
    v.car_delecleared();

    car v2 = new car(16,"A", "C");
    v2.print();
    v2.car_delecleared();
  }

   public static class car
  {
    static int cars_number = 0;

    private int id;
    public String marque;
    private String modele;
    
    public car(int ID, String Marque, String Modele)
    {
      this.id = ID;
      this.marque = Marque;
      this.modele = Modele;

     this.cars_number++;
    } 

    public void del()
    {
      this.cars_number--;
    }

    public void print()
    {
      System.out.println("Car: " + id + ", marque: " + marque + ", modele: " + modele); 
    }

    public void car_delecleared()
    {
       System.out.println("number of decleared car objects is: " + this.cars_number);
    }

  }
}