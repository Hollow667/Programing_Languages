#include <stdio.h>

int is_armstrong(int num)
{
  int res = 0;
  int n = num;
  while(num >0)
  {
    res = res + (num - (num / 10) * 10) * (num - (num / 10) * 10)  * (num - (num / 10) * 10);
    num = num / 10;
  }
  if(n == res) {return 1;}else{return 0;}
}

int main(void)
{
  int i;
  for(i = 0; i < 500; i++) {if( is_armstrong(i) == 1) {printf("%i is an Armstrong number\n", i); }}
  return 0;
}