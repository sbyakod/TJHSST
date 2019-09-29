//Name: Sharath Byakod
//Date: 11/9/18
//Period: 7

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "mpi.h"
#include <sys/time.h>

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

//
double gettime()
{
   double t ;
   //
   struct timeval* ptr = (struct timeval*)malloc( sizeof(struct timeval) ) ;
   //
   gettimeofday( ptr , NULL ) ; // second argument is time zone... NULL
   //
   t = ptr->tv_sec * 1000000.0 + ptr->tv_usec ;
   //
   free( ptr ) ;
   //
   return t / 1000000.0 ;
}
//
int main( int argc , char* argv[] )
{
   //
   // MPI variables
   //
   int        rank    ;
   int        size    ;
   MPI_Status status  ;
   int        tag = 0 ;
   //
   // other variables
   //
   int        k , j  ;
   double     prob , nbt ;
   double     tic  , toc ;
   //
   // boilerplate
   //
   MPI_Init(      &argc          , &argv ) ;
   MPI_Comm_size( MPI_COMM_WORLD , &size ) ; // same
   MPI_Comm_rank( MPI_COMM_WORLD , &rank ) ; // different
   //
   // manager has rank = 0
   //
   if( rank == 0 )
   {
      printf( "\n" ) ;
      //
      prob = 0.60 ; // everyone gets the same probability
      //
      for( j = 1 ; j < size ; j++ )
      {
         MPI_Send( &prob , 1 , MPI_DOUBLE , j , tag , MPI_COMM_WORLD ) ;
      }
      //
      for( k = 1 ; k < size ; k++ )
      {
         MPI_Recv( &nbt , 1 , MPI_DOUBLE , MPI_ANY_SOURCE , tag , MPI_COMM_WORLD , &status ) ;
         //
         j = status.MPI_SOURCE ;
         //
         printf( "%d %d %20.16f\n" , j , size , nbt ) ;
      }
      //
      printf( "\n" );
   }
   //
   // workers have rank > 0
   //
   else
   {
      tic = gettime() ;
      //
      MPI_Recv( &prob , 1 , MPI_DOUBLE , 0 , tag , MPI_COMM_WORLD , &status ) ;
      //
      time_t t;
   
   /* Intializes random number generator */
   srand((unsigned) time(&t));
   //FILE *f = fopen("data.txt", "w");

   /* Print 5 random numbers from 0 to 49 */
   //int probability = 0;

      
   char forest[160][120];
   float avgsteps = 0.0;
   for(int probability = 0; probability <= 100; probability++)
   {
      for(int runs = 0; runs < 100; runs++)
      {
         int steps = 0;
         for(int i = 0; i < 160; i++)
         {
               for(int j = 0; j < 120; j++)
               {
                  int number = rand() % 100 + 1;
                  if(number > probability)
                     forest[i][j] = ' ';
                  else
                     forest[i][j] = '*';
               }
         }
         //print(forest, steps);
         
            for(int i = 0; i < 160; i ++)
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
      //
      MPI_Send( &nbt , 1 , MPI_DOUBLE , 0 , tag , MPI_COMM_WORLD ) ;
      //
      toc = gettime() ;
      //
      printf( "*** %d of %d - time = %0.16f seconds\n" , rank , size , toc - tic ) ;
   }
   //
   // boilerplate
   //
   MPI_Finalize() ;
   //
   return 0;
}