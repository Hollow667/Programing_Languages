public class MyClass 
{
  public static class Polygon
  {
    protected int height;
    protected int width;
    public void set_values(int a, int b)
    {
      this.height = a;this.width = b;
    }
  }
  public static class Rectengle extends Polygon
  {
    public double area()
    {
      return (this.height * this.width);
    }
  }
  public static class Triangle extends Polygon
  {
    public double area()
    {
      return (this.height * this.width) / 2;
    }
  }
  public static void main(String[] args)
  {
    Rectengle rec = new Rectengle();
    Triangle tri = new Triangle();

    rec.set_values(10, 10);
    tri.set_values(10, 10);

        System.out.println("Rectengle area is: " + rec.area());
        System.out.println("Triangle area is: " + tri.area());
  }
}