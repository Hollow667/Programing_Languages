#include <stdio.h>

int main(void)
{
  int i1, i2, i3;

  printf("Enter phone number [(xxx) xxx-xxxx]: ");
  scanf("(%d) %d-%d", &i1, &i2, &i3);
  printf("You entered %d.%d.%d", i1, i2, i3);
}