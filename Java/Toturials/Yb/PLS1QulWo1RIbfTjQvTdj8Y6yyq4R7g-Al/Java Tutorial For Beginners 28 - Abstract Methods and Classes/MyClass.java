public class MyClass 
{
  public static abstract class Polegon
  {
    public abstract int area(); /* do not define the method body here */
  }

  public static class Rectangle extends Polegon
  {
    public int height; public int width;
    Rectangle(int height, int  width) { this.height = height; this.width = width; }
    public int area() {return (this.height * this.width);}
  }


 public static void main(String[] args)
  {
    Rectangle rec = new Rectangle(5, 5);
    System.out.print("Rectangle area " + rec.area());
  }
 }
 