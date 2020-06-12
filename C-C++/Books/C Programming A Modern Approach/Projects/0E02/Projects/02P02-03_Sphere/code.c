#include <stdio.h>

#define pi 3.1415
int main()
{
  float r;
  float v;
  char unit[10];
  printf("enter radius: ");
  scanf("%f %s", &r, &unit);
  v = 4.0f / 3.0f * pi * r * r * r;
  printf("The volume of the sphere with raduis %.f is %.5f %s", r, v, unit); 
  return 0;
}