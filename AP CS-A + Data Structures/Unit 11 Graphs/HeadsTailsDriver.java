//name:   date:  
//for use with Graphs11: State Graphs, Heads-Tails-Heads
import java.util.*;
import java.io.*;

class HeadsTailsDriver
{
   public static void main(String[] args) throws FileNotFoundException
   {
      System.out.println("Type in sequence of three: Heads and Tails");
      Scanner in=new Scanner(System.in);
      Vertex v=makeGraph(in.next());
   	
      System.out.println("Type in wanted sequence of three: Heads and Tails");
      v=findBreadth(v, in.next());
      String s="";
      while(v.previous!=null){
         s=v+"\n"+s;
         v=v.previous;
      }
      System.out.println(s+"Success\n");
   }
   public static Vertex makeGraph(String s)
   {
   
   }
   public static Vertex findBreadth(Vertex v, String goal)
   {
      
   }
}
class Vertex
{
   private final boolean[] state;
   private List<Vertex> edges = new ArrayList<Vertex>();
   public Vertex previous;
   
   
}