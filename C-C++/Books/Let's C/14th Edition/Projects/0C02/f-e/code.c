#include <math.h>
#include <stdio.h>

int main(void)
{
  float L1, L2, G1, G2, dis;
  printf("Enter values of latitude in degrees [L1 L2]: ");
  scanf("%f %f", &L1, &L2);
  printf("Enter values of longitude in degrees [G1 G2]: ");
  scanf("%f %f", &G1, &G2);
  dis = 3963 * acos (sin(L1 * 3.1415 / 180) * sin(L2 * 3.1415 / 180) + cos(G1 * 3.1415 / 180) * cos(G2 * 3.1415 / 180) * cos((G2 - G1) * 3.1415 / 180));
  printf("Distance between two points: %lf m", dis);
  return 0;
}