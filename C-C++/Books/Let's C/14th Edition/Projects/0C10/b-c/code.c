#include <stdio.h>
void feb(float num1, float num2){float n=num1;printf(" %.f", num1 + num2);num1 = num2;num2 = n+num2;feb(num1, num2);}
int main(void)
{
   feb(1, 1); 
  return 0;
}