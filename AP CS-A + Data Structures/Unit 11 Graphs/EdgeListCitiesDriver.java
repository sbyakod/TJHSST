//mlbillington@fcps.edu       May 2014
//lesson:  Graphs5: EdgeListCities
//uses TJGraphAdjList

import java.util.*;
import java.io.*;
 
public class EdgeListCitiesDriver
{  
   public static void main(String[] args)throws FileNotFoundException
   {
      System.out.println("Edge List with Cities! ");
      Scanner kb = new Scanner(System.in);
      System.out.print("Enter file of cities and edges: "); 
   											             //cityEdgeList
      String fileOfCities = kb.next()+".txt";
      Scanner sc = new Scanner(new File(fileOfCities));
      TJGraphAdjList g = new TJGraphAdjList();
      g.graphFromEdgeListData(fileOfCities);
     
      System.out.println("\nAdjacency List");
      System.out.println(g.toString());
   	
      System.out.println("Number of edges: " + g.edgeCount());
      
      System.out.print("\nIs this graph connected? " + g.isConnected() );
      
      while(true)
      {
         System.out.print("\nIs it reachable?  Enter start city (-1 to exit): ");
         String from = kb.next();
         if(from.equals("-1"))
            break;
         System.out.print("                    Enter end city: "); 
         String to = kb.next();  
         System.out.println( g.isReachable(from, to) );
      }
   
   }  
}