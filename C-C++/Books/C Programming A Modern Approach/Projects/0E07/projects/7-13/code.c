#include <stdio.h>

int main(void)
{
  char st[100];
  int wc = 0;int lc = 0;int i = 0;
  printf("Enter a sentence:" );
  scanf("%s", &st);
  printf("\n%s\n", st); 
  while(st[i] != '\0')
	{  printf("\n%c\n", st[i]); 
	if( (st[i] >= 'a' && st[i] <= 'z') || (st[i] >= 'A' && st[i] <= 'Z') ){ lc++;}
	if( st[i] ==  ' ' ) {wc++;} 
	i++;}
  printf("Average word length: %i %i %f", lc, wc, (float) lc / wc);
  printf("\nletters");
  // for(i  = 'A'; i<= 'z'; i++){ printf("\n%c", i); }
  return 0;
}