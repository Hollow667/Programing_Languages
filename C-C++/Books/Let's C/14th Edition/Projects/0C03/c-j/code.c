#include <stdio.h>
#include <math.h>

float dis(float x1,float  y1,float x2,float y2){
 // printf("\n%f %f %f %f", x1, y1, x2, y2);
 return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)); }
int main(void)
{
  float x1, x2, x3, y1, y2, y3, l1, l2, l3;
  printf("Enter Points corrdinates [x1,y1] [x2,y2] [x3,y3]\n");
  scanf("%f,%f %f,%f %f,%f", &x1, &y1, &x2, &y2, &x3, &y3);
  //printf("%f,%f %f,%f %f,%f", x1, y1, x2, y2, x3, y3);
  l1 = dis(x1, y1, x2, y2);l2 = dis(x3, y3, x2, y2);l3 = dis(x1, y1, x3, y3);
  //printf("\n %lf %lf %lf\n", l1, l2, l3);
  if( (l1 == (l2 + l3)) + (l2 == (l1 + l3)) + (l3 == (l1+l2))){ printf("Points are on the same line"); }else{ printf("Points are not on the same line");}  
  return 0;
}