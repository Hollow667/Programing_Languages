#include <math.h>
#include <stdio.h>



int main(void)
{
  float t, v, wcf;
  printf("Tempreture: ");
  scanf("%f", &t);
  printf("Air velocity: ");
  scanf("%f", &v);
  printf("The Wind chill factor (the felt air tempreture on exposed skin due to wind): %f", 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * pow(v, 0.16));
  return 0;
}