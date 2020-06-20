#include <stdio.h>
#define AND &&
#define SMALL_CASE(x) (x >= 'a' AND x <= 'z')
#define CAPITAL_CASE(x) (x >= 'A' AND x <= 'B')
#define MAX(x,y) (x>y?x:y)
int main(void)
{
  printf("%i", SMALL_CASE('x'));
  printf("%i", MAX(1,2));
  return 0;
}