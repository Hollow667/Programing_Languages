public class MyClass
{
  public static class Cube
  {
    int len;int hig;int wid;

    Cube()
    {
      System.out.println("New Cube Created");
    }
    Cube(int l, int h, int w)
    {
      this.len = l;this.hig = h;this.wid = w;
    }

    public int get_volume()
    {
      return this.len * this.hig * this.wid;
    }
   }

  public static void main(String[] args)
  {
    Cube cube1 = new Cube();
    System.out.print(cube1.get_volume());

    Cube cube2 = new Cube(1, 2, 3);
    System.out.print(cube2.get_volume());    


  }
}