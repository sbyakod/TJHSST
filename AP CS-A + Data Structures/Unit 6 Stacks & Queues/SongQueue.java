///name:    date:
//first program on queues.
import java.io.*;
import java.util.*;
public class SongQueue
{
   private static Scanner infile;
   private static Queue<String> songQueue;
   
   public static void main(String[] args) throws Exception
   {
      fillPlayList();
      printSongList();
      infile = new Scanner(System.in);
      String prompt = "\tAdd song (A), Play song (P), Delete song (D), Quit (Q):  ";
      System.out.print(prompt);
      String str = infile.next().toUpperCase();
      while(!str.equals("Q"))
      { 
         processRequest( str );
         System.out.print(prompt);
         str = infile.next().toUpperCase();;
      } 
      System.out.println();
      System.out.println("No more music for you today.  Goodbye!");
      infile.close();
   }
   public static void fillPlayList()throws IOException
   {
   }
   public static void processRequest(String str)
   {
   }
   public static void add()
   {
   }
   public static void play()
   {
   }
   public static void delete()
   {
   }
   public static void printSongList()
   {
   }
}