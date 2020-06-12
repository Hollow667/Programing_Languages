#include <stdio.h>

int main(void)
{
  int i;int d = 0;
  printf("Enter a number: ");
  scanf("%i", &i);
  printf("The number %i has ", i);
  while(i > 0) { i = i / 10; d++; }
  printf("%i digits", d);
  return 0;
}