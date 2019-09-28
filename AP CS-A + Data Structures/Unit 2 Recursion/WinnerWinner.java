  // name:     date:    
   public class WinnerWinner
   {
      public static void main(String[] args)
      {
         Board b = new Board(3,3,"W-S-----X"); 
         System.out.println("Shortest path is " + b.win());   //2
         b = new Board(3,3,"S-W-----X"); 
         System.out.println("Shortest path is " + b.win());   //4
         b = new Board(3,3,"X-W-----S"); 
         System.out.println("Shortest path is " + b.win());   //4
         b = new Board(3,3,"----X--S-"); 
         System.out.println("Shortest path is " + b.win());   //1
         b = new Board(3,3,"SWW---WWX");
         System.out.println("Shortest path is " + b.win());   //4
         b = new Board(3,3,"SWW-W-W-X");        //no path exists
         System.out.println("Shortest path is " + b.win());   //-1
      }
   }

   class Board
   {
      private char[][] board;  
      private int maxPath;
   
      public Board(int rows, int cols, String line)  
      {
      
      }
   
   	/**	returns the length of the longest possible path in the Board   */
      public int getMaxPath()		
      {  
         return maxPath; 
      }	
   
   
   /**	checks to calculate the shortest path from S to X   */
      public int check(int r, int c)
      {	
      
      }
      
   /** precondition:  S and X exist in board
       postcondition:  returns either the length of the path
                       from S to X, or -1, if no path exists. */
      public int win()
      {
      
      }
   }

/*  output:

    Shortest path is 2
    Shortest path is 4
    Shortest path is 4
    Shortest path is 1
    Shortest path is 4
    Shortest path is -1
    */