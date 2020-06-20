#include <stdio.h>

int main(void)
{
  float num, min, max;
  printf("Enter number or 0 to end: ");
  scanf("%f", &num);min = num;max = num;
  while(num != 0)
{
  if(num > max){ max = num; } 
  if(num < min){ min = num; } 
 printf("Enter another number or 0 to end: ");
  scanf("%f", &num);
}
   printf("The Range of numbers is[%.f - %.f]", min, max); 

  return 0;
}