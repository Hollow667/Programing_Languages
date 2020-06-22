#include <stdio.h>
struct Student{
  int roll_No;
  char name[20];
  char departement[50];
  char course[25];
  int year;
};

void set_student(int roll_No,char name[20],char departement[50],char course[25],int year,struct Student *nex_student,struct Student *previous_student)
{


}

int main(void)
{
 int i = 0;
 struct Student S[100] = { {1,"name1", "department", "course", 1988}, {1,"name2", "department", "course", 1987}, {1,"name2", "department", "course", 1988}};
  while(S[i].year){if(S[i].year==1988){printf("name : %s\n", S[i].name);}i++;}
  return 0;
}