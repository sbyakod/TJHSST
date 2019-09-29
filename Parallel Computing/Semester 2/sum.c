//Name: Sharath Byakod
//Date: 6/6/19
//Period: 7

#include <stdio.h>
#include <omp.h>
#include <math.h>

#define N 8
#define logN 3

int main(void)
{
  int rk, size=N, j;
  
  int d[N] = {1, 2, 3, 4, 5, 6, 7, 8};
  int i;
  printf("\nData: ");
  for(i = 0; i < N; i++)
    printf("%d ", d[i]);
  printf("\n");
  
  int tree[logN + 1][N];	    
  
  omp_set_num_threads(size);
  printf("\nSize: %d\n", size);
  
  #pragma omp parallel private(rk)
  {
    rk = omp_get_thread_num();    
    tree[logN][rk] = d[rk];  
  }
  printf("\n");
  
  j = logN -1;
  while(j >= 0)
  {
    size /= 2;
    omp_set_num_threads(size);
    
    #pragma omp parallel private(rk)
    {
      rk = omp_get_thread_num();
      tree[j][rk] = tree[j+1][2*rk] + tree[j+1][2*rk + 1];
    }
    j--;
  }
  printf("Sum: %d\n\n", tree[0][0]);
  
  return 0;
}