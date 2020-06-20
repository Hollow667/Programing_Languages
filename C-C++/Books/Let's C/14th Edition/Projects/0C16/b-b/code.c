#include <stdio.h>
int strlen(char* str){int i  = 0;while(*(str+i) != '\0'){i++;}return i;}

void str_rev(char *str){
  int i = 0; int len = strlen(str);char c;
  while(i<len/2){c=*(str+i);*(str+i)=*(str+len-i-1);*(str+len-i-1)=c;i++;}
}

int main(void)
{
  char str[100]={'a', 'b', 'c', 'd','e', '\0'};
  str_rev(str);
  return 0;
}