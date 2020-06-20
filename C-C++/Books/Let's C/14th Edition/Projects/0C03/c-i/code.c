#include <stdio.h>

int main(void)
{
  float len, bre, area, perimeter;
  printf("Enter rectangle dimensions: ");
  scanf("%f %f", &len, &bre);
  area = len * bre;
  perimeter = 2 * (len + bre);
  if( area > perimeter) { printf("Area is greater than perimeter"); }else{ printf("Area is not greater than perimeter"); }
  return 0;
}