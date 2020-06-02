public class MyClass
{
  public static class Bank
  {
    public int get_int() { return 0; }
    public void print() { System.out.println(this.get_int()); }
  }

  public static class Bank_A extends Bank
  {
    public int get_int() { return 97; }
  }

  public static class Bank_B extends Bank
  {
    public int get_int() { return 98; }
  }

  public static class Bank_C extends Bank
  {
    public int get_int() { return 99; }
  }

  public static void main(String[] args)
  {
    Bank BA = new Bank_A();BA.print();
    Bank BB = new Bank_B();BB.print();
    Bank BC = new Bank_C();BC.print();
  }
}