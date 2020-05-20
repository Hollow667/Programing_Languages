public class Getters_Setters
{
  public static class car
  {
    private int id;
    private String marque;
    private String modele;
    private int vitesse;

    public car(int ID, String Marque, String Modele, int Vitesse)
    {
      this.id = ID;
      this.marque = Marque;
      this.modele = Modele;
      this.vitesse = Vitesse;
    }

    public car()
    {
      this.id = 0;
      this.marque = "Unknown";
      this.modele = "Unknown";
      this.vitesse =0;
    }

    public int get_ID()
    {
      return this.id;
    }

    public void set_ID(int ID)
    {
      this.id = ID;
    }


    public void set_Marque(String Marque)
    {
      this.marque = Marque;
    }

    public String get_Marque()
    {
      return this.marque;
    }

    public void set_Modele(String Modele)
    {
      this.modele = Modele;
    }

    public String get_Modele()
    {
      return this.modele;
    }

    public void set_Vitesse(int Vitesse)
    {
      this.vitesse = Vitesse;
    }

    public int get_Vitesse()
    {
      return this.vitesse;
    }

    public void car_details()
    {
      System.out.println("Car: " + this.id + ", marque: " + this.marque + ", modele: " + this.modele + ", Vitesse: " + this.vitesse + " Km/h");  
    }

  }
  
  public static void main(String[] args)
  {
      car v = new car();
      v.set_ID(1234);
      v.set_Marque("KM12");
      v.set_Modele("QP-17");
      v.set_Vitesse(190);

      v.car_details();
  }
}