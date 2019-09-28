//mlbillington@fcps.edu       July 2014
//lesson:  Graphs3: EdgeList
//uses TJGraphAdjList

   import java.util.*;
   import java.io.*;
    
   public class EdgeListDriver
   {  
      public static void main(String[] args)throws FileNotFoundException
      {
         System.out.println("Edge List Representation! ");
         TJGraphAdjList g = new TJGraphAdjList();
         g.addVertex("A");      //if it's not there, add it.
         g.addVertex("B");
         g.addEdge("A", "C"); // <-- warning!  Be sure to add all the Vertices first; 
                              // or else deal with it. 
         g.addVertex("C");
         g.addVertex("D");
         g.addEdge("B", "A");
         g.addEdge("C", "C");
         g.addEdge("C", "D");
         g.addEdge("D", "C");
         g.addEdge("D", "A");
         System.out.println(g.toString());  //let's look at it first
      }
   }