#include <stdio.h>
int digit_count(int num)
{
  int sum = 0;
  while(num > 0){ sum += num - 10 * (num / 10);num=num / 10; }
  return sum;
}

int digit_count_rec(int sum,int num)
{
  while(num > 0){ sum += num - 10 * (num / 10);num=num / 10; }
  if(num <= 0){ return sum; }
   digit_count_rec(sum,num);
  
}

int main(void)
{
  int num;
  printf("Enter a number: ");
  scanf("%i", &num);
  printf("The sum of the digits: %i", digit_count(num));
  printf("\nThe sum of the digits: %i", digit_count_rec(0,num));
  return 0;
}