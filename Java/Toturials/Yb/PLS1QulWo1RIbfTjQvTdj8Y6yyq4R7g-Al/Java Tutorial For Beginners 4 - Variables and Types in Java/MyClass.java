public class MyClass {
  public static void main(String[] args)
  {
    int int_var = 10;				//4 byte
    short short_var = 10;			//2 bytes
    byte byte_var = 127;			//1 bytes
    long long_var = 10000;			//8 bytes
    float float_var = (float)1000.012938;		//4 bytes
    double double_var = 192389.12039901923;	//8 bytes
    char char_var = 'a';			//2 bytes
    boolean bool_var = true;			//1 bytes

    System.out.println(byte_var);
  }
}