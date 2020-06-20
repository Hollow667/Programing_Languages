#include <stdio.h>

int fac(int n){ int res = 1; 
 	if(n<=0){return 1;}
	while(n>0){res *=n;n--;} 
	return res; }
int main(void)
{
  int num;
  printf("Enter number: ");
  scanf("%i", &num);
  printf("factorial(%i) = %i", num, fac(num));
  return 0;
}