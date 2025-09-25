// Develop a quiz application that asks multiple-choice questions and calculates the score 
#include <stdio.h>

int main() {
   char ans;
   int score = 0;

  
   printf("What is the square of 3?\n a:1 b:2 c:6 d:9\n");
   scanf(" %c", &ans);  
   if (ans == 'd') {  
       score = score + 1;
   }

   
   printf("What is the cube of 2?\n a:3 b:6 c:8 d:12\n");
   scanf(" %c", &ans);  
   if (ans == 'c') {  
       score = score + 1;
   }

   printf("Calculate value of 4!.\n a:12 b:24 c:8 d:22\n");
   scanf(" %c", &ans);  
   if (ans == 'b') {  
       score = score + 1;
   }

   
   printf("What is 28/7?\n a:4 b:3 c:2 d:5\n");
   scanf(" %c", &ans);  
   if (ans == 'a') {  
       score = score + 1;
   }

   
   printf("What is 45+45?\n a:90 b:89 c:92 d:88\n");
   scanf(" %c", &ans);  
   if (ans == 'a') {  
       score = score + 1;
   }

   
   printf("Score is %d\n", score);  
   return 0;
}
