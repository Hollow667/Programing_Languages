#include <stdio.h>

int main(void)
{
  char chr;
  printf("Enter a character: ");
  scanf("%c", &chr);
  if(1)
 {
 printf("The ASCII Value of the character %c is %i", chr, chr);
  }else{ 
    printf("The character is not in the ASCII table");
  }
  return 0;
}