#include <stdio.h>
#include <math.h>

int main(void)
{
  float l1, l2, l3;int sum;
  printf("Enter the three sides of the Triangle: ");
  scanf("%f %f %f", &l1, &l2, &l3);sum = (l1 + l2 + l3) / 2;
  printf("The Area of the triangle: %f", sqrt(sum * (sum - l1) * (sum - l2) * (sum - l3)));
  return 0;
}