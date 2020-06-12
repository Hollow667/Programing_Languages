#include <stdio.h>

int main()
{
  float fn = 123.456;
  printf("%-8.1e\n", fn);
  printf("%10.6e\n", fn);
  printf("%-8.1f\n", fn);
  printf("%10.6f\n", fn);

  return 0;
}