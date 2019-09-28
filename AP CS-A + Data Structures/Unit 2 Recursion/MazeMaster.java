//Name: Sharath Byakod   Period: 6   Date: 10/24/16

import java.util.*;
import java.io.*;

public class MazeMaster
{
   public static void main(String[] args) throws FileNotFoundException
   {
      Scanner sc = new Scanner(System.in);
      System.out.print("Enter the maze's filename: ");
      char[][] retArr = buildCharArr(sc.next());
      Maze m = new Maze(retArr);
      m.display();
      System.out.println("Options: ");
      System.out.println("1: Mark all paths.");
      System.out.println("2: Mark all paths, and display the count of all steps.");
      System.out.println("3: Show only the correct path.");
      System.out.println("4: Show only the correct path. If no path exists, display 'No path exists'.");
      System.out.println("5: Show only the correct path, and display the count of steps.");
      System.out.print("Please make a selection: ");
      m.solve(sc.nextInt());
      m.display();  
   } 
   //take in a filename, and return a char[][]
   public static char[][] buildCharArr(String fileName) throws FileNotFoundException
   {
      char[][] charar;
           
      Scanner infile = new Scanner(new File(fileName));
      String[] tempar = infile.nextLine().split(" ");
      
      int rows = Integer.parseInt(tempar[0]);
      int cols = Integer.parseInt(tempar[1]);
      charar = new char[rows][cols];
         
      for(int i = 0; i < charar.length; i++)
      {
         String line = infile.nextLine();
         for(int j = 0; j < charar[0].length; j++)
         {
            charar[i][j] = line.charAt(j);
            char temp = line.charAt(j);
         }
      }
      
      return(charar);
   }
}

class Maze
{
   //Constants
   private final char WALL = 'W';
   private final char PATH = '.';
   private final char START = 'S';
   private final char EXIT = 'E';
   private final char STEP = '*';
   //fields
   private char[][] maze;
   private int startRow, startCol;
   private boolean S_Exists=false, E_Exists=false;
   //constructor initializes all the fields
   
   public Maze(char[][] inCharArr)    
   {
      int row = inCharArr.length;
      int col = inCharArr[0].length;
      
      maze = new char[row][col];
      
      for(int i = 0; i < row; i++)
      {
         for(int j = 0; j < col; j++)
         {
            maze[i][j] = inCharArr[i][j];
         }
      }
      
      for(int i = 0; i < row; i++)
      {
         for(int j = 0; j < col; j++)
         {
            if(maze[i][j] == EXIT)
            {
               E_Exists = true;
            }
            if(maze[i][j] == START)
            {
               startRow = i;
               startCol = j;
               S_Exists = true;
            }
         }
      }
      
      if((S_Exists == false) || (E_Exists = false))
      {
         System.out.println("Invalid Submission.");
         System.exit(0);
      }
   }
   
   public void display()
   {
      if(maze == null) 
         return;
         
      for(int i = 0; i <maze.length; i++)
      {
         for(int j = 0; j <maze[0].length; j++)
         {
            System.out.print(maze[i][j]);
         }
         System.out.println("");
      }
      System.out.println("");
   }
   
   public void solve(int n)
   {
      if(n == 1)
      {
         markAllPaths(startRow, startCol);
      }
      else if(n == 2)
      {
         int count = markAllPathsAndCountStars(startRow, startCol);
         System.out.println("Number of steps = " + count);
      }
      else if(n == 3)
      {
         displayTheCorrectPath(startRow, startCol);
      }
      else if(n == 4)   //use maze3 here
      {
         if(!displayTheCorrectPath(startRow, startCol) )
            System.out.println("No path exists");   
      }     
      else if(n == 5)
      {
         displayCorrectPathAndCountStars(startRow, startCol, 0);
      }
      else System.out.println("Invalid Submission");
   }
   
   private void markAllPaths(int r, int c)
   {
      if(r >= 0 && r < maze.length && c >= 0 && c < maze[0].length && (maze[r][c] == PATH || maze[r][c] == START || maze[r][c] == EXIT))
      {
         maze[r][c] = STEP;
         markAllPaths(r, c + 1);
         markAllPaths(r, c - 1);
         markAllPaths(r + 1, c);
         markAllPaths(r - 1, c);
      }  
   }
        
   private int markAllPathsAndCountStars(int r, int c)
   {
      
      if(r >= 0 && r < maze.length && c >= 0 && c < maze[0].length && (maze[r][c] == PATH || maze[r][c] == START || maze[r][c] == EXIT))
      {
         
         maze[r][c] = STEP;
         return(1 + markAllPathsAndCountStars(r, c + 1) + markAllPathsAndCountStars(r, c - 1) + markAllPathsAndCountStars(r + 1, c) + markAllPathsAndCountStars(r - 1, c));  
      }
        
      return 0;
   }

   private boolean displayTheCorrectPath(int r, int c)
   {
      if(r >= 0 && r < maze.length && c >= 0 && c < maze[0].length)
      {
         
         if(maze[r][c] == 'E')
         { 
            return true;
         }
         else if(maze[r][c] == PATH || maze[r][c] == START )
         {
            maze[r][c] = 'i';
            if(displayTheCorrectPath(r - 1, c) || displayTheCorrectPath(r, c-1) || displayTheCorrectPath(r + 1, c)|| displayTheCorrectPath(r, c + 1))
            {
               maze[r][c] = STEP;
               return true;
            }
            else
            {
               maze[r][c] = PATH;
               return false;
            }
         }
      }
      
      return false;
   }
   
   private boolean displayCorrectPathAndCountStars(int r, int c, int count)
   {
   
      if(r >= 0 && r < maze.length && c >= 0 && c < maze[0].length)
      {
         
         if(maze[r][c] == 'E')
         {
            System.out.println("Number of steps = " + count);
            return true;
         }
         else if(maze[r][c] == PATH || maze[r][c] == START )
         {
            maze[r][c] = 'i';
            if(displayCorrectPathAndCountStars(r - 1, c, count + 1) || displayCorrectPathAndCountStars(r, c-1, count + 1) || displayCorrectPathAndCountStars(r + 1, c, count + 1)|| displayCorrectPathAndCountStars(r, c + 1, count + 1))
            {
               maze[r][c] = STEP;
               return true;
            }
            else
            {
               maze[r][c] = PATH;
               return false;
            }
         }
      }
      
      return false;
   }
   
   //This is for testing purposes. Do not change or remove this method.
   public char[][] getMaze()
   {
      return maze;
   }
}
