#include <stdio.h>
#include <math.h>
float sum(int* nums, int i)
{
  float sum = 0;
  while(i>=0){sum+=*(nums+i);i--;}
  return sum;
}

float avg(int* nums, int i)
{
  float sum = 0;int num = i;
  while(i>=0){sum+=*(nums+i);i--;}
  return sum / num;
}

float std_div(int* nums, int i)
{
  float sum = 0;int num = i;float sd = 0;float avg;
  if(i<2){return 0;}
  while(i>=0){sum+=*(nums+i);i--;}
  i = num;avg = sum / num;
  while(i>=0){sd+=(*(nums+i) - avg) * (*(nums+i) - avg) ;i--;}  
  sd = sqrt(sd / (num - 1));
  return sd;
}

int main(void)
{
  int i;int count;
   int *nums;
  printf("Enter number of numbers: ");scanf("%i", &count);
  nums = (int *) malloc(count * sizeof(int));
 for(i=0;i<count;i++){ printf("Enter %i number: ");scanf("%i", &(*(nums+i))); }
 printf("\nThe sum is  %.f", sum(nums, count - 1));
 printf("\nThe average is  %.f", avg(nums, count - 1));
 printf("\nThe STD-DIV is  %.f", std_div(nums, count - 1));
  return 0;  
}