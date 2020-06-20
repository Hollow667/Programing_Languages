#include <stdio.h>
#include <math.h>

int main(void)
{
  int a, b;float c;
  printf("Pythogorean Triplets\n");
  for(a=1;a<30;a++){for(b=1;b<a;b++){c=sqrt(b*b+a*a);if(c==(int) c){printf("%i %i %.i\n", a, b,(int) c);}}}
  return 0;
}