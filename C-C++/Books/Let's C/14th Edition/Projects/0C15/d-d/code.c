#include <stdio.h>

int ati(char *str, int* num)
{
  int i = 0;
  *num = 0;
  while( (*(str+i) != '\0')){if((*(str+i) >= '0') && (*(str+i) <= '9')){*num = *num * 10; *num =*num + *(str+i) - '0';}else{return -1;}i++;}
  return 0;
}
int main(void)
{
  int i = 0;char str[100];
  while((str[i]=getchar())!='\n'){i++;}str[i]='\0';
  if(ati(str, &i) == 0){printf("%i", i);}else{printf("failed");}
  return 0;
}