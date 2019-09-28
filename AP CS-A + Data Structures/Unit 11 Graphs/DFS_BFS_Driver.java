//mlbillington@fcps.edu      June 2014
//lesson:  Graphs4: DFS_BFS
//uses TJGraphAdjList

import java.util.*;
import java.io.*;
 
public class DFS_BFS_Driver
{  
   public static void main(String[] args)throws FileNotFoundException
   {
      System.out.println("Edge List Representation! ");
      TJGraphAdjList g = new TJGraphAdjList();
      g.addVertex("A");      //if it's not there, add it.
      g.addVertex("B");
      g.addEdge("A", "C"); // <-- warning!  Be sure to add all the Vertices first, 
                           // or else deal with it. 
      g.addVertex("C");
      g.addVertex("D");
      g.addEdge("B", "A");
      g.addEdge("C", "C");
      g.addEdge("C", "D");
      g.addEdge("D", "C");
      g.addEdge("D", "A");
      System.out.println(g.toString());      //let's look at it first
   	    
      System.out.println("\nDepth First Search");
      for (String name : g.getVertexMap().keySet() )
         System.out.println( name + " ---> " + g.depthFirstSearch(name) );
         
      System.out.println("\nBreadth First Search");
      for (String name : g.getVertexMap().keySet() )
         System.out.println( name + " ---> " + g.breadthFirstSearch(name) );
      
      
      /*  Extension  */   
      // System.out.println("\nDepth First Search (Recursive)");
      // for (String name : g.getVertexMap().keySet() )
      // System.out.println ( name + " ---> " + g.depthFirstRecur(name) );
   }   
}