#include <stdio.h>

int max(int a, int b) {if(a > b) {return a;} return b;}
int min(int a, int b) {if(a < b) {return a;} return b;}

void paper_size(int *l1, int *l2, int n)
{
  int i, new_l;
  *l1 =  841;
  *l2 = 1189;
  for(i = 1; i<n; i++)
  {
    new_l = max(*l1, *l2);
    *l2 = min(*l1, *l2);
    *l1 = new_l / 2;
  } 
}

int main(void)
{
  int n;int l1, l2;
  printf("Enter n for paper A(n): ");
  scanf("%i", &n);
  paper_size(&l1, &l2, n);
  printf("The Paper size is %i (mm) x %i (mm)", l2, l1);
  return 0;
}