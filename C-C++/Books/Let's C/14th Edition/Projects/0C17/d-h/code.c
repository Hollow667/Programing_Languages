#include <stdio.h>
struct node{
int id;
struct node *next;
struct node *prev;
};
int main(void)
{
  struct node *n1, *n2, *n3; 
  n1->id=1;n2->id=2;n3->id=3;
  (n1->next) = n2;(n2->next) = n3;
  (n2->prev) = n1;(n3->prev) = n2;
  printf("next node id for n1: %i", &(n1->next).id);
  return 0;
}