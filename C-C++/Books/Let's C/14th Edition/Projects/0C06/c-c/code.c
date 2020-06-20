#include <stdio.h>
int pn(int num){ int i = 1;int res = 1;for(i = 1; i <=  num; i++){ res*=i; } return res;}
float ser(int num)
{
  float res = 0;int i = 1;
  for(i=1;i<=num;i++){res += (1.0 * i) / (1.0 * pn(i));}
  return res;
}
int main(void)
{
  int num;
  printf("Enter a number: ");
  scanf("%i", &num);
  printf("Series value is %lf", ser(num));  
  return 0;
}