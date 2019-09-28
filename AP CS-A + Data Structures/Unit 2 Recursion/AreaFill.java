//Name: Sharath Byakod
//Date: 10/12/16
//Period: 6

import java.util.*;
import java.io.*;

public class AreaFill
{
   public static char[][] grid = null;
   public static String filename = null;
      
   public static void main(String[] args) throws FileNotFoundException
   {
      Scanner sc = new Scanner(System.in);
      while(true) 
      {
         System.out.print("Filename: ");
         filename = sc.next();
         if(filename.equals("-1"))
         {
            sc.close();
            System.out.println("Good-bye");
            System.exit(0);
         }
         grid = read(filename);
         System.out.println( display(grid) );
         System.out.print("\nEnter ROW COL to fill from: ");
         int row = sc.nextInt();
         int col = sc.nextInt(); 
         grid = fill(grid, row, col, grid[row][col]);
         System.out.println( display(grid) );
      //  Extension
      // int count = fillAndCount(grid, row, col, grid[row][col]);
      // System.out.println( display(grid) );
      // System.out.println("count = " + count);
         System.out.println();
      }
   }
   public static char[][] read(String filename)throws FileNotFoundException
   {  
      Scanner infile = new Scanner(new File(filename));
      String line = infile.nextLine();
      
      String[] parameters = line.split(" ");
      char[][] matrix = new char[Integer.parseInt(parameters[0])][Integer.parseInt(parameters[1])];
      
      while (infile.hasNextLine())
      {
         for(int i = 0; i < matrix.length; i++)
         {
            line = infile.nextLine();
            for(int j = 0; j < matrix[i].length; j++)
            {
               matrix[i][j] = line.charAt(j);
            }
         }
      }
      
      return matrix;
   }
   
   public static String display(char[][] g)
   {    
      for (int i = 0; i < g.length; i++)
      {
         for (int j = 0; j < g[i].length; j++)
         {
            System.out.print(g[i][j]);
         }
         System.out.println();
      }
      return ""; 
   }
   
   public static char[][] fill(char[][] g, int r, int c, char ch) //recursive method
   {  
      if(r >= 0 && r < g.length && c >= 0 && c < g[0].length && ch == g[r][c])
      {
         g[r][c] = '*';
         g = fill(g, r + 1, c, ch);
         g = fill(g, r - 1, c, ch);
         g = fill(g, r, c + 1, ch);
         g = fill(g, r, c - 1, ch);
      }
         
      return g;
   }
	
	// Extension-- count and return the number of asterisks
   public static int fillAndCount(char[][] g, int r, int c, char ch)
   {
      return 0; 
   }
}