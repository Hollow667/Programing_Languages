public class MyClass
{
  public static class Bank
  {
    public int get_int() { return 0; }
    public double get_int(int num) { return 0; }
    public void print() { System.out.println(this.get_int()); }
  }

  public static class Bank_A extends Bank
  {
    public int get_int() { return 97; }
    public double get_int(int num) { return 97 + num; }
  }

  public static void main(String[] args)
  {
    Bank BA = new Bank_A();
    System.out.println(BA.get_int()); 
    System.out.println(BA.get_int(1)); 
  }
}