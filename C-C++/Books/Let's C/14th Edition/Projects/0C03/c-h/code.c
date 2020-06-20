#include<stdio.h>

float abs(float i){ if(i < 0) {return -1 * i ;} else {return i;} }
int main(void)
{
  float i;
 printf("Enter number: ");
  scanf("%f", &i);
  printf("Absulate value is %.f", abs(i)); 
  return 0;
}