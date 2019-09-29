//Name: Sharath Byakod
//Date: 10/11/18
//Period: 7

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

typedef struct point
{
   int x;
   int y;
}point;

typedef struct Node
{
   point po[10];
   struct Node* next;
} Node;

int isFire(char forest[160][120])
{
   int count = 0; 
   for(int i = 0; i < 160; i ++)
   {
      for(int j = 0; j < 120; j++)
      {
         if(forest[i][j] == '-')
         {
            count = count+1;
         }
      }
   }
   return count;
}

void spread(char forest[160][120] )
{
   for(int i = 0; i < 160; i ++)
   {
      for(int j = 0; j < 120; j++)
      {
         if(forest[i][j] == '-')
         {
            forest[i][j] = ' ';
            if(i > 0 && forest[i-1][j] == '*')
            {
               forest[i-1][j] = 't';
            }
            if(j > 0 && forest[i][j-1] == '*')
            {
               forest[i][j-1] = 't';
            }
            if(j < 1919 && forest[i][j+1] == '*')
            {
               forest[i][j+1] = 't';
            }
            if(i < 2559 && forest[i+1][j] == '*')
            {
               forest[i+1][j] = 't';
            }
         }
      }
   }
   for(int i = 0; i < 160; i ++)
   {
      for(int j = 0; j < 120; j++)
      {
         if(forest[i][j] == 't')
         {
            forest[i][j] = '-';  
         }
      } 
   }
}

void print(char forest[160][120], int steps)
{
   for(int i = 0; i < 160; i ++)
   {
      for(int j = 0; j < 120; j++)
      {
         printf("%c", forest[i][j]);
      }
      printf("\n");
   }
   printf("Steps: ");
   printf("%d", steps);
   printf("\n");
   printf("\n");
   printf("\n");
}

int main()
{
   time_t t;
   
   /* Intializes random number generator */
   srand((unsigned) time(&t));
   //FILE *f = fopen("data.txt", "w");

   /* Print 5 random numbers from 0 to 49 */
   //int probability = 0;

      
   char forest[40][30];
   float avgsteps = 0.0;
   for(int probability = 0; probability <= 100; probability++)
   {
      for(int runs = 0; runs < 100; runs++)
      {
         int steps = 0;
         for(int i = 0; i < 40; i++)
         {
               for(int j = 0; j < 30; j++)
               {
                  int number = rand() % 100 + 1;
                  if(number > probability)
                     forest[i][j] = ' ';
                  else
                     forest[i][j] = '*';
               }
         }
         //print(forest, steps);
         
            for(int i = 0; i < 40; i ++)
            {
               forest[i][0] = '-';
            }
            steps += 1;
            //print(forest, steps);
            while(isFire(forest) != 0)
            {
               spread(forest);
               steps = steps + 1;
               //print(forest, steps);
            }
            //print(forest, steps);
            avgsteps = avgsteps + (float)steps;
      }
      
      //printf("Average Steps: ");
      avgsteps = avgsteps / 100;
      printf("%f", avgsteps);
      printf("\n");
      avgsteps = 0.0;
   }
}