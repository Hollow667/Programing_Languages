#include <stdio.h>

void print(int num)
{
int i=0;int j;int len;
int nums[100];
//printf("%i", num);
while(num>0){nums[i]=num-(num/10)*10;num=num/10;i++;}nums[i]='\0';
len=i-1;
//printf("%i %i-%i\n",len, nums[0], nums[len-1]);

//------------------------------------------------------------------------
printf("\n");
for(j=0;j<8;j++)
{
for(i=0;i<=len;i++)
{
switch(nums[len-i])
{
case 1:
  if(j==1){printf(" ##  ");}else if(j==7){printf("#####");}else{printf("  #  ");}break;
case 2:
  if(j==0||j==3||j==7){printf("#####");}else if(j==1||j==2){printf("    #");}else{printf("#    ");}break;
case 3:
  if(j==0||j==3||j==7){printf("#####");}else{printf("    #");}break;
case 4:
  if(j==3){printf("#####");}else if(j<3){printf("#   #");}else{printf("    #");}break;
case 5:
  if(j==0||j==3||j==7){printf("#####");}else if(j==1||j==2){printf("#    ");}else{printf("    #");}break;
case 6:
   if(j==0||j==7||j==3){printf("#####");}else if(j<3){printf("#    ");}else{printf("#   #");}break;
case 7:
   if(j==0){printf("#####");}else if(j==1||j==2){printf("    #");}else if(j==3||j==4){printf("   # ");}else if(j==5||j==6){printf("  #  ");}else{printf(" #   ");}break;
case 8:
  if(j==0||j==3||j==7){printf("#####");}else{printf("#   #");}break;
case 9:
   if(j==0||j==7||j==3){printf("#####");}else if(j<3){printf("#   #");}else{printf("    #");}break;
case 0:
   if(j==0||j==7){printf("#####");}else{printf("#   #");}break;
}
printf(" ");}printf("\n");}} 
  
int main(void)
{
  int num;
  printf("Enter a number: ");
  scanf("%i", &num);
  printf("Number is: %i (make sure not to enter 0 first)\n");
  print(num);
  return 0;
}