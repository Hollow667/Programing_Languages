#include <stdio.h>
//# include <conio.h>

int getkey( )
{
int ch ;
ch = getch( ) ; // will get the key action
return ch ;
}

int main(void)
{
  int ch;
  //up 72, rigth 77, down = 80, left = 75, space = 32, escap = 17, enter = 13
  while((ch = getkey()) !=32){if(ch ==72){printf("Up key");}else{printf("\n%i", ch);}}
  return 0;
}