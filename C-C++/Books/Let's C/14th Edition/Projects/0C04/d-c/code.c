#include <stdio.h>

int main(void)
{
  float num, max;
  printf("Enter number or 0 to end: ");
  scanf("%f", &num);max = num;
  while(num !=0)
  {
if(num > max){ max = num; } 
  printf("Enter another number or 0 to end: ");
  scanf("%f", &num);
}   
  printf("The Greates number is %.lf", max);
  return 0;
}