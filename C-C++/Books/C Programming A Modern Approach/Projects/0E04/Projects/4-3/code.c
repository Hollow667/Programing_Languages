#include <stdio.h>
int num;int rnum = 0;
int main()
{
  // first way
  printf("Enter an integer number: ");
  scanf("%i", &num);
 if(num > 0)
{
 while(num > 0)
  {
    rnum += (num - num / 10 * 10); rnum *= 10; 
    num  = num / 10;
  }
  printf("The reversal is: %i", rnum/10);  return 0;
 }
  else if(num < 0)
  {
 num = -1 * num;
 while(num > 0)
  {
    rnum += (num - num / 10 * 10); rnum *= 10; 
    num  = num / 10;
  }
  printf("The reversal is: -%i", rnum/10);  return 0;
  }
  else
  {
  printf("The reversal is: 0");  return 0;
  }
  return 0;
}

