#include <stdio.h>

int main(void)
{
  int h;int m;
  printf("Enter a 24-hour time: ");
  scanf("%i:%i", &h, &m);
  printf("Equivalent 12-hour time: %i:%i %s", h % 12 >0 ? h % 12 : h, m, h % 12 > 0 ? "PM" : "AM");  
  return 0;
} 