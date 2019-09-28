//mlbillington@fcps.edu, May 2014
//graph manipulation, lesson #0

import java.util.*;
import java.io.*;
public class AdjMatDriver
{
   public static void main(String[] args)throws FileNotFoundException
   {
      Scanner kb = new Scanner(System.in);
      System.out.print("Enter size of adjacency matrix: "); 
      int size = kb.nextInt();
      TJGraphAdjMat g = new TJGraphAdjMat(size);
      System.out.println("Adjacency Matrix");
      g.displayGrid();
      System.out.println("Add edges, source<space>target<enter>.  Enter -1 to end.");
      while(true)
      {
         int source = kb.nextInt();
         if( source == -1 ) 
            break;
         int target = kb.nextInt();
         if( !g.isEdge(source, target) )
            g.addEdge(source, target);
         g.displayGrid();
      }
      g.displayGrid();
      System.out.print("Remove an edge? ");
      if( kb.next().equalsIgnoreCase("Y"))
      {  
         while(true)
         {
            System.out.print("Remove which edge?  ");
            int source = kb.nextInt();
            if( source == -1 ) 
               break;
            int target = kb.nextInt();
            if( g.isEdge(source, target) )
               g.removeEdge( source, target );
            else 
               System.out.println("That's not an edge");
            g.displayGrid();
         }
      }	
      System.out.println("Number of edges: " + g.edgeCount());
      System.out.println("The neighbors of each vertex: ");
      for(int i=0; i<size; i++)
      {
         System.out.println(i + ": " +g.getNeighbors(i));
      }
   }
}