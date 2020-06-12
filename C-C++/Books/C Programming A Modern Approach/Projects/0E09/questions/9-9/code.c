#include <stdio.h>

void swap(int a, int b){int j = a; a=b; b = j; } 

void swap_p(int* a, int* b){
 int j = *a; 
  *a = *b;
  *b = j;}
int main(void)
{
  int a = 0; int b = 1;
  swap(a, b);
  printf("%i %i", a, b);


  a = 0; b = 1;
  swap_p(&a, &b);
  printf("\n%i %i", a, b);

  return 0;
}