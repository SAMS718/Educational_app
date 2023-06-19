#include <stdio.h>
#include "CSPSP.h"
int main()
{
  printf("\e[0;103m");
  printf("                    Welcome to COOL CAB SERVICES\n""\e[4;31m");
  int fare=0;
  float distance;
  char ch;
  printf("enter the distance\n");
  scanf("%f",&distance);
// Distance should be in km.

  if(distance<=5)
  {
    fare=50;
  }
  else if(distance<=15)
  {
    fare = 100 + (distance-5)*10;
  }
  else if(distance<=25)
  {
    fare = 200 + (distance-15)*8;
  }
  else
  {
    fare = distance*4.2;
  }

  printf("The fare for taxi: %d", fare);
  printf("\n");
  printf("shall we proceed the payment ?");
  printf("\n");
  while(1)
  {
    ch = getch();
    if(ch == 115)
    {
      printf("\n");
      printf("Have a safe journey(YOUR BOOKING IS CONFIRMED 👍)");
      printf("\n");
      printf("🚕 -------------------🚙 -------------------🚗");
    }
    else if(ch == 110)
    {
      printf("\n");
      printf("Thanks for using our cool cab services(YOUR PAYMENT WAS DECLINED !!)");
      printf("\n");
      printf("🚕 -------------------🚙 -------------------🚗");
    }
    else
    {

    }
  }

  return 0;


  // Project people:
  //   VU22CSEN0100349(sriram).
  //   VU22CSEN0100427(jathin).
  //   VU22CSEN0100427(kashyap).
  //   VU22CSEN0400281(subash).

}
