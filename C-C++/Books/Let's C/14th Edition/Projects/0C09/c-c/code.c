#include <stdio.h>
float pn(int x)
{
  float res = 1;
  while(x >=1){ res = res * x; x=x-1; }
  return res;
}
float pow(float num, int p)
{
  float res = 1;
  while(p >=1){ res = res * num;p-=1; }
  return res;
}

float sin(float x)
{
  int i = 0;float res = 0;
  res = res + x; 
  for(i=0;i<11;i++){
    res = res + (pow(-1, i)) * pow(x, (2*i+1)) / (pn(2*i+1)) + (pow(-1, i+1)) * pow(x, (4*i+1)) / (pn(4*i+1));
    printf("\n%f + %f = %f", (pow(-1, i)) * pow(x, (2*i+1)) / (pn(2*i+1)) , (pow(-1, i+1)) * pow(x, (4*i+1)) / (pn(4*i+1)), res);   
  }
  return res;
}
int main(void)
{
  float angle;
  printf("Enter Angle in Radian: ");
  scanf("%f", &angle);
  printf("sin(%.f) = %.f", angle, sin(angle));
  return 0;
}