#include <stdio.h>

int main(void)
{
  float x,y; int i,j;
  printf("%%f%%d%%f ");
  scanf("%f%d%f", &x, &i, &y); // 10.3 5 6
  printf("%f%d%f", x, i, y);          // 10.30000056.000000

  printf("%%d%%f%%d ");
  scanf("%d%f%d", &i, &x, &j); // 12.3 45.6 789
  printf("%d%f%d", i, x, j);          // 10.30000056.000000

  return 0;
}