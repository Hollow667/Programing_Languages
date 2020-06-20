#include <stdio.h>
#define IS_VOWEL(x) ((x=='a') || (x=='e') || (x=='i') || (x=='o') || (x=='u') || (x=='A') || (x=='E') || (x=='I') || (x=='U') || (x=='O'))

int strlen(char* str){int i=0;while(*(str+i)!='\0'){i++;}return i;}
char *remove_vowels(char* word)
{
  int i=0; int j=0;char* new_str;int len = strlen(word);
  new_str = (char *) malloc(len);
  while((i+j)<len){if(IS_VOWEL(*(word+j+i))){j++;continue;}*(new_str+i)=*(word+j+i);i++;}
  *(new_str+len) = '\0';
  return new_str;
}

int main(void)
{
  char str[100];int i=0;char c;
  // first way
  while((str[i]=getchar()) != '\n'){i++;}
   str[i] = '\0';
  printf("%s\n", remove_vowels(&str));

  //second way: while getting char make sure it is not vowel
  i = 0;
  while((c=getchar()) != '\n'){if(IS_VOWEL(c)){continue;}str[i]=c;i++;}str[i]='\0';
  printf("%s\n", str);
  return 0;
}