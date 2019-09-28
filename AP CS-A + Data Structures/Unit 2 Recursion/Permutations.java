//Name: Sharath Byakod Period: 6 Date: 10/2/16

import java.util.Scanner;

public class Permutations
{
   public static void main(String[] args)
   {
      Scanner sc = new Scanner(System.in);
      System.out.print("\nHow many digits? ");
      int n = sc.nextInt();
      leftRight("", n);          //when submitting, uncomment all of these
      //oddDigits("", n);
      //superprime(n);
   }

   public static void leftRight(String s, int n)
   {
      if(n == 0)
      {
         System.out.println(s);
      }
      else {
         leftRight(s + "L" , n - 1);
         leftRight(s + "R" , n - 1);
      }
   }


   public static void oddDigits(String s, int n)
   {
      if(s.length() == n)
      {
         System.out.println(s);
      }
      else if(s.length() < n)
      {
         oddDigits(s.concat("1"), n);
         oddDigits(s.concat("3"), n);
         oddDigits(s.concat("5"), n);
         oddDigits(s.concat("7"), n);
         oddDigits(s.concat("9"), n);
      }
   }
   public static void superprime(int n)
   {
      recur(2, n); //try leading 2, 3, 5, 7, i.e. all the single-digit primes
      recur(3, n); 
      recur(5, n);
      recur(7, n);
   }
   private static void recur(int k, int n)
   {
      if(String.valueOf(k).length() == n)
      {
         System.out.println(k);
      }
      else
      {
         int [] nums = {1, 2, 3, 5, 7, 9};
         for(int i = 0; i<nums.length; i++)
         {
            if(isPrime(k*10 + nums[i]))
               recur(k*10 + nums[i], n);             
         }
      
      }
   }
   private static boolean isPrime(int n)
   {
      boolean prime = true;
      for(int i = 1; i<n; i++)
      {
         if(n%i == 0 && i!= 1)
            prime = false;
      }
      return prime;
   }
}