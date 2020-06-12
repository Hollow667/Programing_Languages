#include <stdio.h>

int main(void)
{
  char st[100] = "\0";int i = 0;int nov = 0;
  
  printf("Enter a sentence: ");
  scanf("%s", &st);
  while(st[i] != '\0'){ if(st[i] == 97  || st[i] == 101 || st[i] == 105 || st[i] == 111 || st[i] == 117 || st[i] == 65 || st[i] == 69 || st[i] == 73 || st[i] == 79 || st[i] == 85){nov += 1;}i++;}
  printf("You sentence contains %i vowels", nov);

  // not working
  nov = 0;
  while((st[0] = getchar()) && st[0] != '\0'){ if(st[0] == 97  || st[0] == 101 || st[0] == 105 || st[0] == 111 || st[0] == 117 || st[0] == 65 || st[0] == 69 || st[0] == 73 || st[0] == 79 || st[0] == 85){nov += 1;}}
  printf("You sentence contains %i vowels", nov);
  //printf("%i %i %i %i %i %i %i %i %i %i", 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
  return 0;
}