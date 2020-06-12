#include <stdio.h>

int main(void)
{
  float i, num;
  i = 0;
  do {
    printf("Enter a number: ");
    scanf("%f", &num);
    i = i >= num ? i : num;
  } while(num > 0);
  printf("The largest number aren't neccarity was %lf", i);
  return 0;
}