//Name: Sharath Byakod     Period: 6      Date: 11/9/16  

import java.io.*;      //the File class
import java.util.*;    //the Scanner class
   
public class Widget_Driver
{
   public static final int numberOfWidgets = 57;
      
   public static void main(String[] args) throws Exception
   {
      Comparable[] array = input("widget.txt");
      sort(array);
      print(array);
   }
          	
   public static Comparable[] input(String filename) throws Exception
   {
      Scanner infile = new Scanner(new File(filename));
      int numitems = numberOfWidgets;
      Comparable[] array = new Widget[numitems];
      int temp = 0;
      
      for(int k = 0; k < numitems; k++)
      {
         Widget wd = new Widget();
         
         wd.setPounds(infile.nextInt());
         wd.setOunces(infile.nextInt());
      
         array[k] = wd;
         wd = null;
      }
      
      infile.close();
      
      return array;
   }
   	  
   public static void print(Object[] mango)
   {
      for(int k = 0; k < mango.length; k++)
         System.out.println(mango[k].toString());
   }
   
   public static void sort(Comparable[] array)
   {
      int maxPos;
      for(int k = 0; k < array.length; k++)
      {
         maxPos = findMax(array, array.length - k);
         swap(array, maxPos, array.length - k - 1);
      }
   }

   public static int findMax(Comparable[] array, int upper) //what does "upper" do???
   {
      Widget highest = new Widget();
      highest = (Widget)array[0];
      int dmax = 0;
      for(int index = 1; index < upper; index++)
      {
         Widget wt = new Widget();
         wt = (Widget)array[index];
         if(wt.compareTo(highest) == 1 || wt.compareTo(highest) == 2)
         {
            highest = wt;
            dmax = index;
         }
         wt = null;
      }
      
      return(dmax);
   }
   
   public static void swap(Comparable[] array, int a, int b)//what are "a" and "b" for???
   {
      Widget temp = new Widget();
      temp = (Widget)array[b];
      array[b] = array[a];
      array[a] = temp;
      temp = null;
   }
}
   /////////////////////////////////////////////////////
	//Name: Sharath Byakod     Period: 6      Date: 11/9/16  

class Widget implements Comparable<Widget>
{   
   private int myPounds, myOunces;
   
   public Widget()
   {
      myPounds = myOunces = 0;
   }
   
   public Widget(int x, int y)
   {
      myPounds = x;
      myOunces = y;
   }
   
   public int getPounds()
   {
      return myPounds;
   }
   
   public int getOunces()
   {
      return myOunces;
   }
   
   public void setPounds(int x)
   {
      myPounds = x;
   }
   
   public void setOunces(int x)
   {
      myOunces = x;
   }
   
   public int compareTo(Widget w)
   {
      if(myPounds < w.getPounds())
         return -1;
      else if(myPounds > w.getPounds())
         return 1;
      else if(myOunces < w.getOunces())
         return -2;
      else if(myOunces > w.getOunces())
         return 2;
      else
         return 0;
   }
   
   public String toString()
   {
      return myPounds + " lbs. " + myOunces + " oz. ";
   }
}