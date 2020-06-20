#include <stdio.h>

int main(void)
{
  float dis = 0;
  printf("Enter distance between cities (KM): ");
  scanf("%f", &dis);
  printf("distance in meters %.lf\ndistance in feets %.lf\ndistance in inches %.lf", dis * 1000, dis * 1000 * 3, dis * 100 * 25.4);
  return 0;
}