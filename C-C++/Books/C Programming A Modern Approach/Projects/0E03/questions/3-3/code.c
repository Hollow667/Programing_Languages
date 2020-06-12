#include <stdio.h>

int main()
{
  int i,j,k; float f,g;


  printf("%%d");
  scanf("%d", &i);
  printf("%d\n", i);

  printf(" %%d");
  scanf(" %d", &i);
  printf("%d\n", i);

 
  printf("%%d-%%d-%%d");
  scanf("%d-%d-%d", &i, &j, &k);
  printf("%d-%d-%d\n", i, j, k);

  printf("%%d -%%d -%%d");
  scanf("%d -%d -%d", &i, &j, &k);
  printf("%d-%d-%d\n", i, j, k);


  printf("%%f");
  scanf("%f", &f);
  printf("%f\n", f);

  printf("%%f ");
  scanf("%f ", &f);
  printf("%f\n", f);


  printf("%%f,%%f");
  scanf("%f,%f", &f, &g);
  printf("%f,%f\n", f, g);

 printf("%%f, %%f");
  scanf("%f, %f", &f, &g);
  printf("%f, %f\n", f, g);

  return 0;
}