#include <stdio.h>

int main(void)
{
  int i = -1;int j = 0; int are_anagrams = 1;char fw[100]; char sw[100];
  
  printf("Enter first word: ");
  do { i++;fw[i] = getchar(); }while(fw[i] != '\n');

  i = -1;
  printf("Enter second word: ");
  do { i++;sw[i] = getchar(); }while(sw[i] != '\n');

  i = 0;
  while(fw[i] != '\n')
  {
    j = 0;
    are_anagrams = 0;
    while(sw[j] != '\n')
    {
      if(fw[i] == sw[j]){are_anagrams = 1;break;}j++;
    }
    if(are_anagrams == 0){ printf("The words are not anagrams");return 0; }i++;
  } 

  i = 0;
  while(sw[i] != '\n')
  {
    j = 0;
    are_anagrams = 0;
    while(fw[j] != '\n')
    {
      if(fw[i] == sw[j]){are_anagrams = 1; break;}j++;
    }
    if(are_anagrams == 0){ printf("The words are not anagrams");return 0; }i++;
  } 
  printf("The words are anagrams");
  return 0;
}