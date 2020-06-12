#include <stdio.h>

int main()
{
  double r;
  double pi = 3.1415;
  double v;
  char *unit;
  printf("enter radius: ");
  scanf("%d %s", &r, &unit);
  v = 4.0f / 3.0f * pi * r * r * r;
  printf("The volume of the sphere is %.lf %s", v, unit); 
  return 0;
}