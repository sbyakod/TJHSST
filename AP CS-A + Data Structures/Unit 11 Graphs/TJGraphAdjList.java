//name:    date:
//resource classes and interfaces
//for use with Graphs3: EdgeList
//             Graphs4: DFS-BFS
//             Graphs5: EdgeListCities

import java.io.*;
import java.util.*;
/*********************  Graphs 3:  EdgeList *******************************/
interface VertexInterface
{
   public String toString();     //just return the name
   public String getName();
   public ArrayList<Vertex> getAdjacencies();
   public void addEdge(Vertex v);
}  

interface TJGraphAdjListInterface 
{ 
   public List<Vertex> getVertices();
   public Vertex getVertex(int i) ;
   public Vertex getVertex(String vertexName);
   public Map<String, Integer> getVertexMap();
   public void addVertex(String v);
   public void addEdge(String source, String target);
   public String toString();
  
}

  
   /*********************Graphs 4:  DFS and BFS ****************************/
interface DFSAndBFS
{
   public List<Vertex> depthFirstSearch(String name);
   public  List<Vertex> breadthFirstSearch(String name);
   public  List<Vertex> depthFirstRecur(String name);
}

   /****************Graphs 5:  EdgeList with Cities  *********/
interface EdgeListWithCities
{
   public void graphFromEdgeListData(String fileName) throws FileNotFoundException;
   public int edgeCount();
   public boolean isReachable(String source, String target);
   public boolean isConnected();
}
/***********************************************************/
class Vertex implements VertexInterface 
{
   private final String name;
   private ArrayList<Vertex> adjacencies;
  
  /* enter your code here  */
  
}  
/*******************************************************/
public class TJGraphAdjList implements TJGraphAdjListInterface//, DFSAndBFS, EdgeListWithCities
{
   private ArrayList<Vertex> vertices = new ArrayList<Vertex>();
   private Map<String, Integer> nameToIndex = new HashMap<String, Integer>();
  
 /* enter your code here  */
       
}


