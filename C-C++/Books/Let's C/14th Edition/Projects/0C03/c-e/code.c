#include <stdio.h>

int main(void)
{
  int n; int rn = 0; int num;
  printf("Enter number: ");
  scanf("%i", &n);num = n;
  do{ rn +=num - 10 *  (num / 10); rn *= 10; num = num / 10;}while(num != 0);rn /=10;
  printf("Number is: %i, Reversed number is: %i -- Numbers are equal: %s", n, rn, rn == n ? "True" : "False");
  return 0;
}