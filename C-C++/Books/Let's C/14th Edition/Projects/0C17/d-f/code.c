#include <stdio.h>
#define VALID_MAIN_CHOICES(x) (x>0 && x < 8)
#define VALID_YN(x) (x==1 || x==2)
#define  NOT_VALID() {printf("Error: choice not valid!!!\n");}
struct book{
  int number;
  char title[20];
  char author[30];
  float price;
  int issued;
};
void print_choices()
{
printf("1. Add book information\n");
printf("2. Display book information\n");
printf("3. List all books of given author\n");
printf("4. List the title of specific book\n");
printf("5. List the count of books in the library\n");
printf("6. List the books in the order of accession number\n");
printf("7. Exit\n");
}
int main(void)
{
  int choice = -1;int num_of_books;
 do
{
  print_choices();
  printf("Enter a choice: ");scanf("%i", &choice);
  if(VALID_MAIN_CHOICES(choice)){
  
  }else{
  NOT_VALID();
  }
}while(choice != 7);
return 0;
}