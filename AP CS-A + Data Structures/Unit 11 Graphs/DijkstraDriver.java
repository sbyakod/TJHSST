//Retrieved and adapted from: http://en.literateprograms.org/Dijkstra's_algorithm_(Java)?oldid=15444
//modified by Ethan Lowman on 5.29.2014 to create a TJGraphAdjListWeighted class
//further modified by mlbillington@fcps.edu on 6.12.2014

//uses TJGraphAdjListWeighted, wVertex, Edge

import java.util.*;
import java.io.*;
public class DijkstraDriver 
{
   public static void main(String[] args) throws FileNotFoundException 
   {
      	/* Day 1 (Graphs 6):  hard-coded A-B-C-D   	*/
   //       TJGraphAdjListWeighted graph = new TJGraphAdjListWeighted();
   //       graph.addVertex("A");
   //       graph.addVertex("B");
   //       graph.addVertex("C");
   //       graph.addVertex("D"); 
   //       graph.addEdge("A","B", 9); 
   //       graph.addEdge("A","C", 3); 
   //       graph.addEdge("C","B", 5); 
   //       graph.addEdge("C","D", 2);
   //       graph.addEdge("D","B", 1);    	
   //       Scanner key = new Scanner(System.in);
   //       System.out.print("Enter start: " );
   //       String source = key.next(); 
   //       graph.minimumWeightPath(source);   //runs Dijkstra's Algorithm
   //       for (wVertex v : graph.getVertices()) {
   //          System.out.println("Distance to " + v + ": " + v.getMinDistance());
   //       }
      	
      	/*Day 2 (Graphs 7):  cities and path, read from the data file   */
      TJGraphAdjListWeighted g = new TJGraphAdjListWeighted();
      g = g.graphFromEdgeListData(new File("cities.txt"), new File("cityEdgeListWeighted.txt"));
      Scanner key = new Scanner(System.in);      
      System.out.print("Enter start: " );
      String source = key.next(); 
      g.minimumWeightPath(source);  //runs Dijkstra's Algorithm
      for (wVertex v : g.getVertices()) {
         System.out.println("Distance to " + v + ": " + v.getMinDistance());
         List<wVertex> path = g.getShortestPathTo(v);
         System.out.println("                   Path: " + path);
      }
   }
}
