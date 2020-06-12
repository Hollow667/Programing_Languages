#include <stdio.h>
int main(void)
{
  int n = 1;
  printf("%i", n == 1 - 10); // is equal to n == 9
  if (n == 1 - 10){printf("n is between 1 and 10\n");}
  return 0;
}