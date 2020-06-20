#include <stdio.h>
void print_choices(){printf("1Factorial of a number\n2 Prime or not\n3 Odd re even\n4 Exit\n");}
int valid_choice(int choice){if( choice == 1 || choice == 2 || choice == 3 || choice == 4){return 0;}return -1;}

int main(void)
{
  int choice = -1;
  while(choice != 4){print_choices();scanf("%i", &choice);
  if(valid_choice(choice) == -1){printf("Choice not valid\n");continue;}
  else{printf("not compeleted\n");}
  }
  return 0;
}