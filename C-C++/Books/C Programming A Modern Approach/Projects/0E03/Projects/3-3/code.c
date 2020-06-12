#include <stdio.h>

int main(void)
{
  int i1, i2, i3, i4, i5;

  printf("Enter ISBN: ");
  scanf("%d-%d-%d-%d-%d", &i1, &i2, &i3, &i4, &i5);
  printf("GSI prefix: %d\nGroup identifier: %d\nPublisher code: %d\nItem number: %d\nCheck digit: %d", i1, i2, i3, i4, i5);
  return 0;
}