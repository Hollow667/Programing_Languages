#include <stdio.h>

int main(void)
{
  int s[100];int key = 0; int i = -1;
  printf("Enter message to be encrybted: ");
  do{  i++; s[i] = getchar();}while(s[i] != '\n');
  printf("Enter shift amount (1-25): ");
  scanf("%i", &key);
  printf("Encrypted message: ");
  i = 0;
  while(s[i] != '\n')
  {
    if((s[i] >= 'a' && s[i] <= 'z'))
    {
      printf("%c", ((s[i] - 'a') + key) % 26 + 'a');
    }
    else if((s[i] >= 'A' && s[i] <= 'Z'))
    {
      printf("%c", ((s[i] - 'A') + key) % 26 + 'A');
    }
    else
    {
      printf("%c",s[i]);
    }
    i++;
  }
  return 0;
}