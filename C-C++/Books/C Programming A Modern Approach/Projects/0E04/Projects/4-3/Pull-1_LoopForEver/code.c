#include <stdio.h>
int num;int rnum = 0;
int main()
{
  // first way
  printf("Enter an integer number: ");
  scanf("%i", &num);
  printf("Start Looping\n");
  while(num > 0);
  {
    printf("here %i\n", num);
    rnum = num - num / 10; 
    num  = num / 10;
    rnum = rnum * 10;
  }

  printf("The reversal is: %i", rnum);
  return 0;
}

