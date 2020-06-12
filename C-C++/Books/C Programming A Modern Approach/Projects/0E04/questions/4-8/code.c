/* Compute a Universal Product Code Check digit */

#include <stdio.h>

int main(void)
{
  int total = 8;
  printf("Check digit: %d\n", 9 - ((total - 1) % 10 ));
  printf("Check digit: %d\n", (10 - (total % 10)) % 10 );
  return 0;
}
