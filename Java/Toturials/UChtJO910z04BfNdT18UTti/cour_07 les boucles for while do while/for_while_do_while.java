public class for_while_do_while
{
public static void main(String args[]){
//for(initialistion;condition;incr-decr){}
for (int i = 0;i < 10;i++)
{
System.out.println(i);
}
int val = 10;
for (;val > 0; val--)
{
System.out.println(val);
}
//while(condition)
int i = 10;
while(i-- > 0)
{
System.out.println(i);
}
//do {} while (condition)
//an infinit loop
/*
do
{
System.out.println("merci");
} while(1);
*/
}
}