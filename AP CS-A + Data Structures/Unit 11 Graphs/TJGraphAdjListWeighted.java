//name:   date: 
//for use with Graphs6: Dijkstra
//             Graphs7: Dijkstra with Cities

import java.io.*;
import java.util.*;

class Edge {
   public final wVertex target;
   public final double weight;
   
   public Edge(wVertex argTarget, double argWeight) {
      target = argTarget;
      weight = argWeight;
   }
}

class wVertex implements Comparable<wVertex>, wVertexInterface
{
   private final String name;
   private ArrayList<Edge> adjacencies;
   private double minDistance = Double.POSITIVE_INFINITY;
 
    /*  enter your code here   */ 
    
      
}

interface wVertexInterface 
{
   public String toString();
   
   public String getName();
   
   public double getMinDistance();
   
   public void setMinDistance(double m);
   
   // public wVertex getPrevious();         //Graphs 7
    
   // public void setPrevious(wVertex v);   //Graphs 7
   
   public ArrayList<Edge> getAdjacencies();
   
   public int compareTo(wVertex other);
}


public class TJGraphAdjListWeighted implements TJGraphAdjListWeightedInterface
{
   private ArrayList<wVertex> vertices = new ArrayList<wVertex>();
   private Map<String, Integer> nameToIndex = new HashMap<String, Integer>();
  
   /*  enter your code here   */ 
   
   
}    
interface TJGraphAdjListWeightedInterface 
{
   public List<wVertex> getVertices();
   
   public wVertex getVertex(int i);
   
   public wVertex getVertex(String vertexName);
   
   public void addVertex(String v);
   
   public void addEdge(String source, String target, double weight);
     
   public void minimumWeightPath(String vertexName);   //Dijkstra's
   
   /*  Graphs 7 */
       
//  public List<wVertex> getShortestPathTo(wVertex v);
    
//  public TJGraphAdjListWeighted graphFromEdgeListData(File vertexNames, File edgeListData) throws FileNotFoundException 
 
}