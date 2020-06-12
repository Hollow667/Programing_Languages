#include <stdio.h>
void print_squares(int num)
{
  int i = 2;printf("all squares less than %i are:\n", num);
  while( i * i <= num){if(i%2==0){printf("%i\n", i*i);}i++;}
}

int main(void)
{
  int num;
  printf("Enter a number: ");
  scanf("%i", &num);
  print_squares(num);
  return 0;
}