#include <stdio.h>

int copy_arr(int *arr_from, int* arr_to, int to, int from)
{
 int i = 0;int j = 0; 
  for(i=from;i<to;i++){*(arr_to+j) = *(arr_from + i);j++; }
  return j;
}

int SHOW_ARR_ITER = 0;
#define SHOW_ARR(arr,size) {for(SHOW_ARR_ITER=0;SHOW_ARR_ITER<size;SHOW_ARR_ITER++){printf(" %i", arr[SHOW_ARR_ITER]);}}
int main(void)
{
  int arr1[] = {1,2,3};
  int arr2[3];
  printf("Copyiny array...");
  SHOW_ARR(arr1, 3);
  copy_arr(arr1, arr2, 3,0);
  SHOW_ARR(arr2, 3);  
  return 0;
}