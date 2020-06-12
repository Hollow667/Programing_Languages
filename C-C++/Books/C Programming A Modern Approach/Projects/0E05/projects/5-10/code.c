#include <stdio.h>

int main(void)
{
  int grade;
  printf("Enter numerical grade: ");
  scanf("%i", &grade);
  grade = grade <= 59 ? 0 : grade / 10; 
  switch(grade){
    case 0:
      printf("F");break;
    case 6:
      printf("D");break;
    case 7:
      printf("C");break;
    case 8:
      printf("B");break;
    case 9:
      printf("A");break;
    case 10:
      printf("A");break;
  }
  return 0;
}