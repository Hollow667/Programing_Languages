#include <stdio.h>
int main(void)
{
  char fn[100]; char sn[100];
  printf("Enter a first and last name: ");
  scanf("%s %s", &fn, &sn);
  printf("%s, %c.", sn, fn[0]);

  return 0;
}