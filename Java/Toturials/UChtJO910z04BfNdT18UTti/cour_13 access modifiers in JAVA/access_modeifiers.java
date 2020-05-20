public class access_modeifiers
{
  public static void main(String args[])
  {
    car v = new car();
    v.marque = "B"; // public access modifier
    v.set_info(15, "A"); // private access modifier
    v.print();

    // static is used by the class
    // each time you declear a car object the cars_number variable will increase by 1
    car v2 = new car();
    v2.car_delecleared();

    // static variables can be called frrom the calss name
    System.out.println(car.cars_number);
  }

   public static class car
  {
    static int cars_number = 0;

    private int id;
    public String marque;
    private String modele;
    
    public car()
    {
     this.cars_number++;
    } 
 
    public void set_info(int ID , String Modele)
    {
      this.id = ID;
      this.modele = Modele;
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