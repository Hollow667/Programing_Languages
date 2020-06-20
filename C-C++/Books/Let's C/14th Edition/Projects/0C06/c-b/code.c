#include <stdio.h>

char to_ascii(int num){char ch = num; return ch;}
int main(void)
{
  int i = 0;char ch = 2;
  //while(i < 1000){printf("%c", ch);i++;}
  for(i=0;i<=255;i++){printf("%i %c\n", i, to_ascii(i));}
  return 0;
}