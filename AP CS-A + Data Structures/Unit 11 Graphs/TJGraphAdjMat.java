//name:   date:   
// resource classes and interfaces
// for use with Graphs0: Intro
//              Graphs1: Wardhall
//              Graphs2: Floyd
import java.util.*;
import java.io.*;

interface AdjacencyMatrix
{
   public void addEdge(int source, int target);
   public void removeEdge(int source, int target);
   public boolean isEdge(int from, int to);
   public void displayGrid();
   public int edgeCount();
   public List<Integer> getNeighbors(int source);
   
}

interface Warshall
{
   //User-friendly functionality
   public boolean isEdge(String from, String to);
   public Map<String, Integer> getVertices();     
   public void readNames(String fileName) throws FileNotFoundException;
   public void readGrid(String fileName) throws FileNotFoundException;
   public void displayVertices();
   //Actual Warshall Algorithm
   public void allPairsReachability();
}

interface Floyd
{
   public int getCost(int from, int to);
   public int getCost(String from, String to);
   public void allPairsWeighted(); 
}

public class TJGraphAdjMat implements AdjacencyMatrix //,Warshall,Floyd
{
   private int[][] grid = null;   //adjacency matrix representation
   private Map<String, Integer> vertices = null;   
     
   /*  enter your code here  */  
   
   
}
