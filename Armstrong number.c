 //Design a C program to check whether a given number is an Armstrong 
#include <stdio.h>
#include <math.h>
int digits=0,temp=0,sum=0,num=0,fsum=0;
int counter(int num);
int sumfinal(int x);
int main() {
    printf("Enter number that you want to check: ");
    scanf("%d",&num);
counter(num);
sumfinal(num);
    if(num==fsum){
        printf("Armstrong Number.");
    }
    else{
        printf("Not an Armstrong number.");
    }
    return 0;
}

int counter(int num){
        while(num!=0){
        num/=10;
        digits++;
        }
        return digits;
}

int sumfinal(int num){
        while(num!=0){
        temp=num%10;
        for (int i=0;i<digits;i++){
        sum=pow(temp,digits);
        }
        num/=10;
        fsum+=sum;
    }
    printf("Final sum is:%d\n",fsum);
    return fsum;
}
