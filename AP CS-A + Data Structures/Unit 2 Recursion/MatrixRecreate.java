// Name: Sharath Byakod   Period: 6   Date: 10/17/16

import java.util.*;

public class MatrixRecreate
{
   public static void main(String[] args)
   {
      int[][] matrix = TheMatrix.create();
      int[] rowcount = new int[matrix.length];
      int[] colcount = new int[matrix[0].length];
      TheMatrix.count(matrix, rowcount, colcount);
      TheMatrix.display(matrix, rowcount, colcount);
      System.out.println();
      TheMatrix.re_create(rowcount, colcount);
      TheMatrix.display(TheMatrix.getRecreatedMatrix(), rowcount, colcount);
   
   }
}

class TheMatrix
{
	//do not instantiate recreatedMatrix yet. Only instantiate and set that in recur.
   private static int[][] recreatedMatrix;
   
   public static int[][] getRecreatedMatrix()
   {
      return recreatedMatrix;
   }
   
   public static int[][] create()
   {
      Random rand = new Random();
      
      int rows = 2+rand.nextInt(5);
      int cols = 2+rand.nextInt(5);
      
      
      int [][] matrix = new int [rows][cols];
      
      for(int i = 0; i < matrix.length; i++)
      {
         for(int j = 0; j < matrix[0].length; j++)
         {
               matrix[i][j] = rand.nextInt(2);
         }
      }
      
      return matrix;
   }
   
   public static void count(int[][] matrix, int[] rowcount, int[] colcount)
   {  
      //count rows
      for(int i = 0; i < matrix.length; i++)
      {
         for(int j = 0; j < matrix[0].length; j++)
         {
            rowcount[i] = rowcount[i] + matrix[i][j];
         }
      }
      //count columns
      for(int i = 0; i < matrix[0].length; i++)
      {
         for(int j = 0; j < matrix.length; j++)
         {
            colcount[i] = colcount[i] + matrix[j][i];
         }
      }
   }
   
   public static void display(int[][] matrix, int[] rowcount, int[] colcount)
   {
      System.out.print("  ");
      
      for(int i = 0; i < colcount.length; i++)
         System.out.print(colcount[i] + " ");
         
      System.out.println();
      System.out.print("  ");
      
      for(int i = 0; i< colcount.length; i ++)
      {
         if(i == colcount.length-1)
            System.out.print("-");
         else
            System.out.print("--");
      }
      
      System.out.println();
      
      for(int i = 0; i< matrix.length; i++)
      {
         System.out.print(rowcount[i] + "|");
         for(int j = 0; j< matrix[0].length; j++)
         {
            System.out.print(matrix[i][j] + " ");
         }
         System.out.println();
      }
   }
   
	//should call recur.
   public static void re_create(int[] rowcount, int[] colcount)
   {
      int [][] matrix = new int [rowcount.length][colcount.length];
      recur(matrix, rowcount, colcount, 0, 0);
   }
   
   private static void recur(int[][] m, int[] rowcount, int[] colcount, int row, int col)
   {
   
      if(compare(m, rowcount, colcount))    //base case: if new matrix works, then copy over to recreatedMatrix
      {
      	//copy over from m to recreatedMatrix (not just references)
         recreatedMatrix = new int[m.length][];
         for(int i = 0; i < m.length; i++)
         {
            recreatedMatrix[i] = new int[m[i].length];
            for (int j = 0; j < m[i].length; j++)
            {
               recreatedMatrix[i][j] = m[i][j];
            }
         }    //we're done!   
      }
      else
      {
         if(col < m[0].length && row < m.length)
         {
         //recur with 1
            m[row][col] = 1;
            recur(m, rowcount, colcount, row, col+1);
         //recur with 0
            m[row][col] = 0;
            recur(m, rowcount, colcount, row, col+1);
         }
         else if(row == rowcount.length-1)
         {
            if(col > colcount.length-1)
            {
               return;
            }
         }
         else
            recur(m, rowcount, colcount, row + 1, 0);
      }           
   }
   
   private static boolean compare(int[][] m, int[] rowcount, int[] colcount)
   {
      //count everything in m and then compare to rowcount
      int[] new_rowcount = new int [m.length];
      int[] new_colcount = new int [m[0].length];
      
      for(int i = 0; i < m.length; i++)
      {
         for(int j = 0; j < m[0].length; j++)
         {
            new_rowcount[i] = new_rowcount[i] + m[i][j];
         }
      }
      //count columns
      for(int i = 0; i < m[0].length; i++)
      {
         for(int j = 0; j < m.length; j++)
         {
            new_colcount[i] = new_colcount[i] + m[j][i];
         }
      }
      
      //check if arrays are equal
      boolean checker = true;
      for(int i = 0; i < rowcount.length; i++)
      {
         if(rowcount[i] != new_rowcount[i])
            checker = false;
      }
      for(int i = 0; i < colcount.length; i++)
      {
         if(colcount[i] != new_colcount[i])
            checker = false;
      }
      return checker;
      
   }
}