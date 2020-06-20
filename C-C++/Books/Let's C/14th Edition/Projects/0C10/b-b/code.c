#include <stdio.h>
void fac(int num)
{
  int i;
  printf("factors of number %i are",num); 
  while(num!=1){for(i=2;i<=num;i++){if(num%i==0){printf(" %i", i);num = num/i;break;}}}
}

void fac_rec(int num){
 int i=0;
if(num!=1){for(i=2;i<=num;i++){if(num%i==0){printf(" %i", i);num = num/i;}}}
if(num==1){return ;}
fac_rec(num);
}

int main(void)
{
  int num;
  printf("Enter a number: ");
  scanf("%i", &num);
  fac(num);

  printf("\nfactors of number %i are:", num);fac_rec(num); 
  return 0;
}