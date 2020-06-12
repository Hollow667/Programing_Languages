#include <stdio.h>

int main(void)
{
  int m, d, y;
  printf("Enter a date (mm/dd/yyyy): ");
  scanf("%2d/%2d/%4d", &m, &d, &y);
  printf("%d", y*10000+ m*100+ d);
  return 0;
}