// Name: Sharath Byakod    Period: 6   Date: 3/20/17

import java.util.*;

public class Hailstone_Driver
{
   public static void main(String[] args)
   {
      Hailstone hs = new Hailstone();
        
      Scanner keyboard = new Scanner(System.in);
      System.out.print("Enter Hailstone starting number:  ");
      int startNum = keyboard.nextInt();
      do{
         long startTime = System.nanoTime();
         hs.hailstoneMaps(startNum);
         int time = (int)(System.nanoTime() - startTime);
         System.out.println(Hailstone.steps.get(startNum) +" steps.");
         System.out.println(Hailstone.sequence.get(startNum));
         System.out.println("Nanoseconds:  "+ time);
         System.out.println();
        
         System.out.print("Enter Hailstone starting number:  ");
         startNum = keyboard.nextInt();
      }while( startNum != -1);
      System.out.println("Goodbye.");
   }
} 

class Hailstone
{
   public static HashMap<Integer, Integer> steps = new HashMap<Integer, Integer>();
   public static HashMap<Integer, String> sequence = new HashMap<Integer, String>();

   public int hailstoneMaps(int k) //we talked in class, and you said doing helper methods that calcuated each part individually was okay, as long as they are "short-circuiting" which they are
   {
      String temp = hailseq(k);
      
      return(hailsteps(k));
   }
   
   public static int hailsteps(int n)
   {
      int count = 0;
   
      if(steps.containsKey(n))
         return(steps.get(n));
   
      if(n == 1)
         ; //do nothing
      else if(n % 2 == 0)
         count += 1 + hailsteps(n / 2);
      else
         count += 1 + hailsteps(3 * n + 1);
   
      steps.put(n, count);
   
      return(count);         
   }
   
   public static String hailseq(int n)
   {
      String temp = "";
   
      if(sequence.containsKey(n))
         return(sequence.get(n));
      
      if(n == 1)
         temp = "1";
      else if(n % 2 == 0)
         temp = n + ", " + hailseq(n / 2); 
      else
         temp = n + ", " + hailseq(3 * n + 1);
         
      sequence.put(n, temp);
      
      return(temp);
   }
}

/*********************************

  ----jGRASP exec: java Hailstone_teacher
 Enter Hailstone starting number:  16
 4 steps.
 16, 8, 4, 2, 1
 Nanoseconds:  726799
 
 Enter Hailstone starting number:  16
 4 steps.
 16, 8, 4, 2, 1
 Nanoseconds:  12661
 
 Enter Hailstone starting number:  16
 4 steps.
 16, 8, 4, 2, 1
 Nanoseconds:  6843
 
 Enter Hailstone starting number:  8
 3 steps.
 8, 4, 2, 1
 Nanoseconds:  6843
 
 Enter Hailstone starting number:  5
 5 steps.
 5, 16, 8, 4, 2, 1
 Nanoseconds:  23611
 
 Enter Hailstone starting number:  5
 5 steps.
 5, 16, 8, 4, 2, 1
 Nanoseconds:  6501
 
 Enter Hailstone starting number:  199
 119 steps.
 199, 598, 299, 898, 449, 1348, 674, 337, 1012, 506, 253, 760, 380, 190, 95, 286, 143, 430, 215, 646, 323, 970, 485, 1456, 728, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
 Nanoseconds:  1348206
 
 Enter Hailstone starting number:  598
 118 steps.
 598, 299, 898, 449, 1348, 674, 337, 1012, 506, 253, 760, 380, 190, 95, 286, 143, 430, 215, 646, 323, 970, 485, 1456, 728, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
 Nanoseconds:  8212
 
 Enter Hailstone starting number:  299
 117 steps.
 299, 898, 449, 1348, 674, 337, 1012, 506, 253, 760, 380, 190, 95, 286, 143, 430, 215, 646, 323, 970, 485, 1456, 728, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
 Nanoseconds:  7870

 Enter Hailstone starting number:  -1
 Goodbye. 
  ----jGRASP: operation complete.
  **********************************************/