#include <stdio.h>
#define Max_Customers 100
struct customer{
  char account_number[10];
  char name[25];
  float balance;
};

int main(void)
{
  int i;
  struct customer customers [Max_Customers] = {{"0001", "name1", 1}, {"0002", "name2", 2}};
  for(i=0; i< Max_Customers; i++){if(customers[i].balance < 100 && customers[i].balance > 0){printf("name: %s\n", customers[i].name);}}
  return 0;
}