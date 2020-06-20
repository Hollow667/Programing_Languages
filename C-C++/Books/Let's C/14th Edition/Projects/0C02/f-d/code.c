#include <math.h>
#include <stdio.h>

int main(void)
{
  float x, y, r, phi;
  
  printf("Enter Coordinates: ");
  scanf("%f %f", &x, &y);

  r = sqrt(x * x + y * y);
  phi = atan(y / x);
   
  printf("Coordinates in Polar System: r: %lf,  phi: %lf rad", r, phi);
  return 0;
}