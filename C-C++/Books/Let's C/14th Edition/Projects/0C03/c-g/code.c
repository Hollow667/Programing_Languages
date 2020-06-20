#include <stdio.h>

int main(void)
{
  float a1, a2, a3;
  printf("Enter Angles: ");
  scanf("%f %f %f", &a1, &a2, &a3);
  if((a1+a2+a3) == 180){ printf("Triangle is valid"); }else{ printf("Triangle is not valid"); }
  return 0;
}