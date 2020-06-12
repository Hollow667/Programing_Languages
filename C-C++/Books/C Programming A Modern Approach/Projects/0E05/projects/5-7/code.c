#include <stdio.h>
int max(int n1, int n2)
{
   if(n1 >= n2){return n1;}
  return n2; 
}
int min(int n1, int n2)
{
   if(n1 <= n2){return n1;}
  return n2; 
}

int main(void)
{
  int n1, n2, n3, n4;
  printf("Enter four integers: ");
  scanf("%i %i %i %i", &n1, &n2, &n3, &n4);
  printf("Largest: %i\n", max(n1, max(n2, max(n3, n4))));
  printf("Smallest: %i\n", min(n1, min(n2, min(n3, n4))));
  return 0;
}