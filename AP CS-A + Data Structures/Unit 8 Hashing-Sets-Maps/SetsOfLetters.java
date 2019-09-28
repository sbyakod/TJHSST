// Name: Sharath Byakod    Period: 6   Date: 3/15/17

import java.util.*;
import java.io.*;

public class SetsOfLetters
{
   public static void main(String[] args) throws FileNotFoundException
   {
   //Scanner sc = new Scanner(System.in);
   //System.out.print("Enter the file name: ");
   //String fileName = sc.next();
      String fileName = "declarationLast.txt";
      fillTheSets(fileName);
   }
   
   public static void fillTheSets(String fn) throws FileNotFoundException
   {
      int count = 0;
   
      Set<Character> set = new TreeSet<Character>();
      Scanner infile = new Scanner(new File(fn));
      
      while(infile.hasNext())
      {
         Set<Character> tempset = new HashSet<Character>();
         String str = infile.nextLine();
         
         int i = 0;
         while(i < str.length())
         {
            tempset.add(str.charAt(i));
            i++;
         }
         
         Set<Character> set2 = new TreeSet<Character>(tempset);
         
         if(count != 0)
            set.retainAll(set2);  
         else
            set = set2;
         
         System.out.println(str);
         
         Set<Character> lcase = new TreeSet<Character>();
         Set<Character> ucase = new TreeSet<Character>();
         Set<Character> other = new TreeSet<Character>();
         
         for(char x: set2)
         {
            if(!Character.isLetter(x))
               other.add(x);
            else if(Character.isLowerCase(x))
               lcase.add(x);
            else if(Character.isUpperCase(x))
               ucase.add(x);;
         }
         
         System.out.println("Lower case: " + lcase);
         System.out.println("Upper case: " + ucase);
         System.out.println("Other: " + other);
         System.out.println();
         
         count++;
      }
   
      Set<Character> lcase2 = new TreeSet<Character>();
      Set<Character> ucase2 = new TreeSet<Character>();
      Set<Character> other2 = new TreeSet<Character>();
         
      for(char x: set)
      {
         if(!Character.isLetter(x))
            other2.add(x);
         else if(Character.isLowerCase(x))
            lcase2.add(x);
         else if(Character.isUpperCase(x))
            ucase2.add(x);;
      }
      
      System.out.println("Common Lower Case: " + lcase2);
      System.out.println("Common Upper Case: " + ucase2);
      System.out.println("Common Other: " + ucase2);
   }
}