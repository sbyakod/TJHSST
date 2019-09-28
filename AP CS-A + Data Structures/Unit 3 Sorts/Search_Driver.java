//Name: Sharath Byakod    Period: 6   Date: 11/2/16

import java.io.*;      //the File 
import java.util.*;    //the Scanner 
import javax.swing.*;  //the JOptionPane

public class Search_Driver
{
   public static void main(String[] args) throws Exception
   {
      JFrame f = new JFrame("Search Driver");
      Comparable target = JOptionPane.showInputDialog("Enter target word");
   }
   
   public static String[] input(String filename) throws Exception
   {
      Scanner infile = new Scanner(new File(filename));
      String[] arin = new String[1325];
      
      for(int i = 0; i < arin.length; i++)
      {
         arin[i] = infile.next();
      }
      
      arin = sort(arin);
      
      return arin;
   }
   
   public static String[] sort(String[] array)
   {
      int len = array.length - 1; 
      
      while(len >= 0)
      {
         int max = findMax(array, len);
         
         if(array[max].compareTo(array[len]) > 0 )
            swap(array, max, len);
            
         len = len - 1;;
      }
      
      return array;
   }
   
   public static int findMax(String[] array, int upper)
   {
      String max = "A";
      int maxdex = 0;
      
      for(int i = 0; i < upper; i++)
      {
         if(array[i].compareTo(max) > 0)
         {
            maxdex = i;
            max = array[i];            
         }
      }
      
      return maxdex;
   }
   
   public static void swap(String[] array, int a, int b)
   {
      String temp = array[b];
      
      array[b] = array[a];
      array[a] = temp;
   }
}
/////////////////////////////////////////////////////////
class Searches
{
   public static int linearCount = 0;
   private static int binaryCount = 0;
         
   public static int binaryCount()
   {
      return binaryCount;
   }
   
   public static int linear(Comparable[] array, Comparable target)
   {
      for(int i = 0; i < array.length; i++)
      {
         linearCount++;
      
         if(array[i].equals(target))
            return("Linear Search found it at location " + i + " in " + linearCount + " comparisons.");
      }
   }
   
   public static int binary(Comparable[] array, Comparable target)
   {
      return(binaryhelper(array, target, 0, array.length));
   }
   
   private static int binaryhelper(Comparable[] array, Comparable target, int start, int end)
   {
   }
}