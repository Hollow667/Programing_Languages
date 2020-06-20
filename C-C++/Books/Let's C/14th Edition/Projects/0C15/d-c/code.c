#include <stdio.h>
char * sub(char *main_str, char *sub_str, int from, int to)
{
 int i;int j=0;
 for(i=from;i<to;i++,j++){*(sub_str+j)=*(main_str+i);}
 *(sub_str+j)='\0';
 return sub_str;
}
int main(void)
{
  char str[100]="";int i=0;char sub_str[100];
  while(str[i-1]!='\n'){str[i++]=getchar();} 
  str[i-1]='\0';
  printf("%s %s", str, sub(str, sub_str, 1, 5));
  return 0;
}