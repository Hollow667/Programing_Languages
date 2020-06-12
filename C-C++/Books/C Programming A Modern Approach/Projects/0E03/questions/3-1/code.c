#include <stdio.h>

int main()
{
  printf("%6d,%4d", 86, 1040); // 86,10403
  printf("%12.5e", 30.253); // 3.02530e+001
  printf("%.4f", 83.162); // 83.1620
  printf("%-6.2g", .0000009979); // 1e-006
  return 0;
}