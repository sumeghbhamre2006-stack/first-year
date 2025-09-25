// Develop a C program that takes integer as input and print its reverse
#include<stdio.h>;
int main() {
int rev=0,n,remainder;
printf(“Enter any number:”);
scanf(“%d&”,&n);
while(n>0)
{
remainder=n%10;
rev=rev*10+remainder;
n=n/10;
}
printf(“reverse number is %d” ,rev);
return 0;
}
