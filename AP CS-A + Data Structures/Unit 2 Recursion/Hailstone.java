//Author: Sharath Byakod
//Date: 10/5/16
//Period: 6
    
import java.util.*;
  
public class Hailstone
{
   public static void main(String[] args)
   {
      System.out.println("Hailstone Numbers!");
      System.out.print("Enter the start value: ");
      Scanner sc = new Scanner(System.in);
      int start = sc.nextInt();
      int count = hailstone(start);
      System.out.println(" takes " + count + " steps." );
      int count2 = hailstone(start, 1);
      System.out.println(" takes " + count2 + " steps." );
   }
      //recursive, counts the steps with a variable
   public static int hailstone(int n, int count)
   {
      while(n != 1)
      {
         if (n % 2 == 0)
            n = n / 2;
         else
            n = (3 * n) + 1;
         count++;
      }
      return count;
   }
		//recursive, counts the steps without a variable
   public static int hailstone(int n)
   {
   
      if (n != 1)
      {
         if (n % 2 == 0) 
            return 1 + hailstone(n / 2);
         else 
            return 1 + hailstone((3 * n) + 1);
      }
      else 
         return n;
   }
}