#include <stdio.h>

int are_sym(int arr[], int size){
int i = 0;
int to = size / 2;
for(i = 0; i< size;i++){if(arr[i] != arr[size-1-i]){return 0;}}
return 1;
}

int main(void)
{
  int arr1[] = {1,2,2,1};
  int arr2[] = {1,2,1};
  int arr3[] = {1,2,3,4};
  int arr4[] = {1,2,3};
  printf("Checking Arrays are symetric... %i %i %i %i", are_sym(arr1,4), are_sym(arr2, 3), are_sym(arr3, 4), are_sym(arr4, 3));
  return 0;
}