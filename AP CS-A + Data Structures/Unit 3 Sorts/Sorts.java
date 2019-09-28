    /* M.L. Billington, 10/02/2006.
    Uses the helper classes Selection and Insertion. 
	 Students are to write the Selection and Insertion classes.
    */
    
import java.util.*;
import java.io.*;

public class Sorts
{
   public static void main(String[] args) throws Exception
   {
        //Part 1, for doubles
      
      int n = (int)(Math.random()*100);    
      double[] array = new double[n];
      for(int k = 0; k < array.length; k++)
         array[k] = Math.random();	
      print(array);
      System.out.println("*************  *************");
       
      array = Selection.sort(array);
      array = Insertion.sort(array);
      print(array);
      
      	//Part 2, for Strings
      
      int size = 100;
      Scanner sc = new Scanner(new File("declaration.txt"));
      
      
      Comparable[] arrayStr = new String[size];
      for(int k = 0; k < arrayStr.length; k++)
         arrayStr[k] = sc.next();	
      print(arrayStr);
      System.out.println("*************  *************");
      arrayStr = Selection.sort(arrayStr);
      arrayStr = Insertion.sort(arrayStr);
      print(arrayStr);
   }
   
   public static void print(double[] a)
   {
      // for(int k = 0; k < a.length; k++)    //old style
      //       System.out.println(a[k]);
      for(double d : a)                      // for-each loop     
         System.out.println(d);
      System.out.println();
   }
   
   public static void print(Object[] papaya)
   {
      for(Object item : papaya)     //for-each
         System.out.println( item );
   }
}
   //*******************************************************************
  //Name: Sharath Byakod   Period: 6   Date: 10/31/2016
  //The Selection class will have methods sort(), findMax() and swap().
  //Three versions of each method will have to be written, to work 
  //for doubles, Strings, and Comparables.
  
class Selection
{
   public static double[] sort(double[] array)
   {
      int len = array.length - 1;
       
      while(len >= 0)
      {
         int max = findMax(array, len);
         
         if(array[len] < array[max] )
            swap(array, max, len);
         
         len = len - 1;;
      }
      
      return array;
   }
   
   private static int findMax(double[] array, int n)
   {
      double max = Math.pow(2, -1074);
      int maxdex = 0;
      
      for(int i = 0; i < n; i++)
      {
         if(max > array[i])
         {
            maxdex = i;
            max = array[i];            
         }
      }
      
      return maxdex;
   }
   
   private static void swap(double[] array, int a, int b)
   {
      double temp = array[b];
      
      array[b] = array[a];
      array[a] = temp;
   }
   	/***************************************************
   	  for Strings
   	  ***********************************************/
        
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
   
   	/***************************************************
   	 for Comparables,
   	      Swap() is for Objects.
   	      make sure that print() is for Objects, too.
   	  ***********************************************/

   @SuppressWarnings("unchecked")//this removes the warning for Comparable
   public static Comparable[] sort(Comparable[] array)
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
   
   @SuppressWarnings("unchecked")
   public static int findMax(Comparable[] array, int upper)
   {
      Object max = array[0];
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
   
   public static void swap(Object[] array, int a, int b)
   {
      Object temp = array[b];
      
      array[b] = array[a];
      array[a] = temp;
   }
 
}   

//**********************************************************
  //Name: Sharath Byakod   Period: 6   Date: 10/31/2016
  //The Insertion class 
  //write enough methods to handle doubles and Comparables.
  
class Insertion
{
   
   public static double[] sort(double[] array)
   { 
    //Algorithm:
         //loop from i - 1 to moveval backwards
         //move everything up
         //place temp in index moveval
      for(int i = 1; i < array.length; i++)
      {
         double temp = array[i];
         int moveval = move(array, i, temp);
      
         for(int j = i - 1; j >= moveval; j--)
            array[j + 1] = array[j];
        
         array[moveval] = temp; 
      }
      
      return array;
   }
   
   private static int move(double[] array, int index, double value)
   {
      int slindex = index - 1;
      int count = 0;
      
      for(int i = slindex; i >= 0; i--)
      {
         if(value >= array[i])
         {
            count = i + 1;
            break;
         }
      }
      
      return count;
   }
   
   @SuppressWarnings("unchecked")
    public static Comparable[] sort(Comparable[] array)
   { 
      for(int i = 1; i < array.length; i++)
      {
         Comparable temp = array[i];
         int moveval = move(array, i, temp);
      
         for(int j = i - 1; j >= moveval; j--)
            array[j + 1] = array[j];
        
         array[moveval] = temp; 
      }
      
      return array;
   }
   
   @SuppressWarnings("unchecked")
    private static int move(Comparable[] array, int index, Comparable value)
   {
      int slindex = index - 1;
      int count = 0;
      
      for(int i = slindex; i >= 0; i--)
      {
         if(value.compareTo(array[i]) >= 0)
         {
            count = i + 1;
            break;
         }
      }
      
      return count;
   }
}
