#include <stdio.h>

int main(void)
{
  float item;float price;
  //char date[11];

  printf("Enter item number: ");
  scanf("%f", &item);
  printf("Enter unit price: ");
  scanf("%f", &price);
  //printf("Enter purchase date (mm/dd/yyyy): ");
  //scanf("%s", date);

  printf("Item\t\tUnit\t\tPurchase\n\t\t\t\tPrice\t\t\t\tDate");

  return 0;
}