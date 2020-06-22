#include <stdio.h>

#define IS_VOWEL(x) (x=='a' || x=='i' || x=='o' || x=='u' || x=='e' || x=='A' || x=='I' || x=='O' || x=='U' || x=='E')

int count_double_vowel(char stat[])
{
  int i=0;int count=0;
  while(stat[i]!='\0'){if(IS_VOWEL(stat[i])){if(IS_VOWEL(stat[i+1])){count++;}}i++;}
  return count;
}
int main(void)
{
  char stat[100]; int i=0; 
  while((stat[i]=getchar()) != '\n'){i++;}stat[i]='\0';
  //printf("%s", stat);
  printf("\ndouble vowel count: %i",count_double_vowel(stat) );
  return 0;
}