// Design a C program that calculates the factorial of a given number using both iterative and
//recursive methods.
//RECURSIVE METHOD:
#include<stdio.h>
 int fact(int n);
int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    printf("Factorial of %d = %ld", n, fact(n));
    return 0;
}

 int fact(int n) {
    if (n>=1)
        return n*fact(n-1);
    else
        return 1;
}
//ITERATIVE METHOD

int main() {
    int n, i;
    unsigned long long fact = 1;  
    
    printf("Enter an integer: ");
    scanf("%d", &n);

   
    if (n < 0)
        printf("Error! Factorial of a negative number doesn't exist.\n");
    else {
       
        for (i = 1; i <= n; ++i) {
            fact *= i;
        }
        printf("Factorial of %d = %llu\n", n, fact);  
    }

    return 0;
}

