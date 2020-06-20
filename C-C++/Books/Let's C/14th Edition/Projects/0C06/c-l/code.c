#include <stdio.h>

int pn(int i, int j){ int res = 1;int k;for(k=0;k<=j;k++){res = res + i*(j-k);} return res;}
int main(void)
{
  int i, j;int k;
  for(i=1;i<10;i++){printf("\n");for(j=0;j<=i;j++){k = j%i;printf("%i ", pn(k,i));}}
  return 0;
}