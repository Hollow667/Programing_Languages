#include <stdio.h>
#include <math.h>
#define PI acos(-1.0)
float to_rad(float deg){ return deg * PI / 180; }
int main(void)
{
  float a;
  printf("Enter Angle in degrees: ");scanf("%f", &a);
  a = to_rad(a);
  printf("cos(%.lf)=%.lf\nsin(%.lf)=%.lf\ntan(%.lf)=%.lf\ncot(%.lf)=%.lf\n", a, cos(a), a, sin(a), a,  tan(a), a, 1 / tan(a));
  return 0;
}