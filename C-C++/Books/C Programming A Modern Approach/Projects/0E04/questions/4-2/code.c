#include <stdio.h>

int main(void)
{
  int i = 1;
  int j = 1;

 // yes
  printf("%i %i\n", (-i) / j, (-i / j)); // -1 -1

  return 0;
}