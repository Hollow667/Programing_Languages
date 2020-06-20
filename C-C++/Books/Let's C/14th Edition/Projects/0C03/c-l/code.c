#include <stdio.h>

int main(void)
{
  float x, y;
  printf("Enter point: ");
  scanf("%f,%f", &x, &y);
  if(x == 0 && y != 0)
  {printf("Point is on the X-axis");}
  else if(x != 0 && y == 0)
  {printf("Point is on the Y-axis");}
  else if(x == 0 && y == 0)
  {printf("Point is on the Origin");}
  else
  {printf("The point is not on the axies or on the center point");}
  return 0;
}