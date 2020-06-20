#include <stdio.h>

#define MEAN(x,y) ((x+y)/2)
#define ABS(x) (x>0?x:-x)
#define MAX(x,y) (x>y?x:y)

#define AND &&
#define UP_SHIFT 'A'-'a'
#define SMALL_CASE(x) (x>='a' AND x<='z')
#define TO_UP_CASE(x) (SMALL_CASE(x)?x+UP_SHIFT: x)

int main(void)
{
  printf("%c %c", TO_UP_CASE('a'), TO_UP_CASE('A'));
  return 0;
}