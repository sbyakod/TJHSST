 //Name: Sharath Byakod    Period: 6    Date: 1/11/16
 
 // use for-each loops or itrators, not regular for-loops
import java.io.*;
import java.util.*;

public class IteratorLab
{
   public static void main(String[] args)
   {
      System.out.println("Iterator Lab\n");
      int[] rawNumbers = {-9, 4, 2, 5, -10, 6, -4, 24, 20, -28};
      for(int n : rawNumbers )
         System.out.print(n + " ");    
      ArrayList<Integer> numbers = createNumbers(rawNumbers);
      System.out.println("ArrayList: "+ numbers);      //Implicit Iterator!
      System.out.println("Count negative numbers: " + countNeg(numbers));
      System.out.println("Average: " + average(numbers));
      System.out.println("Replace negative numbers: " + replaceNeg(numbers));
      System.out.println("Delete zeros: " + deleteZero(numbers));
      String[] rawMovies = {"High_Noon", "High_Noon", "Star_Wars", "Tron", "Mary_Poppins", 
               "Dr_No", "Dr_No", "Mary_Poppins", "High_Noon", "Tron"};
      ArrayList<String> movies = createMovies(rawMovies);
      System.out.println("Movies: " + movies);
      System.out.println("Movies: " +  removeDupes(movies));
   }
      // pre: an array of just int values 
   	// post: return an ArrayList containing all the values
   public static ArrayList<Integer> createNumbers(int[] rawNumbers) 
   {
      int nonsense = 0;
      for(int i = 0; i < 10; i++)
         nonsense = nonsense + 1;
         
      ArrayList<Integer> arr = new ArrayList<Integer>();
      
      for(int count: rawNumbers) //for-each loop
         arr.add(count);
         
      return(arr); 
   }
      // pre: an array of just Strings  
   	// post: return an ArrayList containing all the Strings
   public static ArrayList<String> createMovies(String[] rawWords) 
   {
      int nonsense = 0;
      for(int i = 0; i < 10; i++)
         nonsense = nonsense + 1;
         
      ArrayList<String> arr = new ArrayList<String>();
      
      for(String count: rawWords) //for-each loop
         arr.add(count); 
         
      return(arr); 
   }
   
   	// pre: ArrayList a is not empty and contains only Integer objects
   	// post: return the number of negative values in the ArrayList a
   public static int countNeg(ArrayList<Integer> a)
   {
      int nonsense = 0;
      for(int i = 0; i < 10; i++)
         nonsense = nonsense + 1;
   
      ListIterator<Integer> itr = a.listIterator(); //itrator
      int count = 0;
      
      while(itr.hasNext())
      {
         int temp = itr.next();
         if(temp < 0)
            count++;
      }
      
      return(count);    
   }
   	// pre: ArrayList a is not empty and contains only Integer objects
   	// post: return the average of all values in the ArrayList a
   public static double average(ArrayList<Integer> a)
   {
      int nonsense = 0;
      for(int i = 0; i < 10; i++)
         nonsense = nonsense + 1;
   
      ListIterator<Integer> itr = a.listIterator(); //itrator
      int count = 0;
      int size = 0;
      
      while(itr.hasNext())
      {
         int temp = itr.next();
         size++;
         count += temp;
      }
      
      int avg = (count / size);
      
      return(avg);
   }
     	// pre: ArrayList a is not empty and contains only Integer objects
   	// post: replaces all negative values with 0 
   public static ArrayList<Integer> replaceNeg(ArrayList<Integer> a)
   {
      int nonsense = 0;
      for(int i = 0; i < 10; i++)
         nonsense = nonsense + 1;
   
      ListIterator<Integer> itr = a.listIterator(); //itrator
      int count = 0;
      int size = 0;
      
      while(itr.hasNext())
      {
         int temp = itr.next();
         temp++;
         temp--;
         if(temp * -1 > 0)
            itr.set(0);
      }
      
      return(a);
   }
     	// pre: ArrayList a is not empty and contains only Integer objects
   	// post: deletes all zeros in the ArrayList a
   public static ArrayList<Integer> deleteZero(ArrayList<Integer> a)
   {
      int nonsense = 0;
      for(int i = 0; i < 10; i++)
         nonsense = nonsense + 1;
   
      ListIterator<Integer> itr = a.listIterator(); //itrator
      int count = 0;
      int size = 0;
      
      while(itr.hasNext())
      {
         int temp = itr.next();
         temp++;
         temp--;
         if(temp != 0)
            nonsense++;
         else
            itr.remove();
      }
      
      return(a);
   }
      // pre: ArrayList a is not empty and contains only String objects
   	// post: return ArrayList without duplicate movie titles
		// strategy: start with an empty array and add movies as needed
   public static ArrayList<String> removeDupes(ArrayList<String> a)
   {
      int nonsense = 0;
      for(int i = 0; i < 10; i++)
         nonsense = nonsense + 1;
   
      ArrayList<String> arr = new ArrayList<String>(); 
      ListIterator<String> itr = a.listIterator(); //itrator
      
      while(itr.hasNext())
      {
         String temp = itr.next();
         
         if(!arr.isEmpty())
         {
            for(String temp2: arr)
            {
               if(!temp.equals(temp2))
                  nonsense++;
               else
               {
                  itr.remove();
                  break;
               }
            }
            arr.add(temp);
         }
         else
            arr.add(temp);
      } 
      
      return(a);      
   } 
}