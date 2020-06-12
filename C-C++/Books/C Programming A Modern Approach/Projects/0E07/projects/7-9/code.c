#include <stdio.h>

int main(void)
{
  int h = 0;int m = 0; char p[3] = "\0";

  printf("Enter a 12-hour time: ");
  scanf("%i:%i %c%c",&h, &m, &p[0], &p[1]);
  if(p[0] == 'P' || p[0] == 'p'){h = h + 12;}
  printf("Equivalent 24-hour tim : %i:%i", h, m);
  return 0;
}