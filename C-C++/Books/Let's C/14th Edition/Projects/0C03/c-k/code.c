#include <stdio.h>

float dis(float x1,float y1,float x2,float y2){ return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2); }
int main(void)
{
  float x, y, r;float x1, y1;
  printf("Enter center point: ");scanf("%f,%f", &x, &y);
  printf("Enter raduis: ");scanf("%f", &r);
  
  printf("Enter center point: ");scanf("%f,%f", &x1, &y1);
  if(dis(x, y, x1, y1) == r*r)
  {
    printf("Point is on the Circle");
  }else if(dis(x, y, x1, y1) < r*r)
  {
    printf("Point is in the Circle");
  }else{
    printf("Point is outside the Circle");
 }
  return 0;
}