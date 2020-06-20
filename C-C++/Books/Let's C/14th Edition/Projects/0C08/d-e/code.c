#include <stdio.h>
void prime_factors(int num)
{int i = 0;printf("Prime factors are ");
 while(num != 1){for(i = 2;i<=num;i++){if(num%i == 0){printf("%i ", i); num = num / i; break;}}}
}
int main(void)
{
  int num; 
  printf("Enter a number to find its prime factors: ");
  scanf("%i", &num);
  prime_factors(num);
  return 0;
}