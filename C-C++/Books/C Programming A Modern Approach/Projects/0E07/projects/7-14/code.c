// newton method to find square root of an integer number
#include <stdio.h>

float sq(int x)
{
  float y = 1.0 * x / 2;
  //printf("%f %f",   (y - x/y), (1.0 * x / 1000));
  while( ((y - x/y) *  (y - x/y)) >= (1.0 * x / 1000000000)) {
    // printf("\n%f", y);
    y = (y + x/y) / 2;
  }
  return y;
}

int main(void)
{
  int x; float y;
  printf("Enter a positive number: ");
  scanf("%i", &x);
  printf("Square root: ");
  printf("%f", sq(x));
  return 0;
}