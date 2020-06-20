#include <stdio.h>

int main(void)
{
  float len, brd, rad; float pi = 3.1415692;
  printf("Enter the Length and Breadth of the Rectangle: ");
  scanf("%f %f", &len, &brd);
  printf("The area of the Rectengle: %.lf, The perimeter of the Rectangle %.lf", len * brd, 2 * (len + brd));
  printf("\nEnter the radius of the Circle: ");
  scanf("%f", &rad);
  printf("The area of the Circle: %f, The circumference of the Circle is: %f", pi * rad * rad, 2.0 * pi * rad);
  return 0;
}