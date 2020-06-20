#include <stdio.h>

int main(void)
{
  float salary = 0;
  printf("Enter salary ($): ");
  scanf("%f", &salary); 
  // salary after dearness allowance and house rent allowence
  salary = (1 - 0.4 - 0.2) * salary;
  printf("The gross salary is: %.lf$", salary);
  return 0;
}