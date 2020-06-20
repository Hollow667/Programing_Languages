#include <stdio.h>
#include <math.h>

is_prime(int num)
{
  int end = sqrt(num);
  int i = 2;
  //printf("End: %i", end);
  for(i = 2; i<= end; i++){if(num%i == 0) {return -1; }}
  return 0;
}

int main(void)
{
  int num;
  printf("Enter a number: ");
  scanf("%i", &num);
  if(is_prime(num) == 0)
  {
    printf("The number is a primary number");
  }else
  {
    printf("The number is not a primary number");
   }
  return 0;
}