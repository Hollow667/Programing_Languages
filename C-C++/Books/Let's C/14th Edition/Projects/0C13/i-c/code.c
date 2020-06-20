#include <stdio.h>

float min(float *arr, int size)
{
  float Min =*(arr); int i=0;
  for(i = 1;i<size;i++){if(*(arr+i) < Min){Min = *(arr+i);}}
  return Min;
}
 
int main(void)
{
  float arr[] = {-1, -1, -2, 5, -1.1};
  printf("Min arr is %.f", min(&arr, 5)); 
  return 0;
}