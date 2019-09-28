//Name: Sharath Byakod
//Period: 6
//Date: 9/20/2016  

import java.util.*;
import java.io.*;
import javax.swing.JOptionPane;
import java.util.Comparator;

public class PigLatin
{
   public static void main(String[] args) throws IOException
   {
      //part_1_using_pig();
      part_2_using_piglatenizeFile();
   }
   
   public static void part_1_using_pig()
   {
      Scanner sc = new Scanner(System.in);
      while(true)
      {
         System.out.print("\nWhat word? ");
         String s = sc.next();
         if (s.equals("-1")) 
            System.exit(0);
         String p = pig(s);
         System.out.println("***** " + p + " *****");
      }		
   }
   public static String pig(String word)
   {
      String tempword = word;
      boolean upcase = Character.isUpperCase(tempword.charAt(0));
      tempword = tempword.toLowerCase();
      boolean firstpunc = Character.isLetter(tempword.charAt(0));
      boolean lastpunc = Character.isLetter(tempword.charAt(tempword.length() - 1));
      
      String fpunc = "";
      String lpunc = "";
      
      if(firstpunc == false)
      {
         while(firstpunc == false)
         {
            fpunc = fpunc + Character.toString(tempword.charAt(0));
            tempword = tempword.substring(1);
            firstpunc = Character.isLetter(tempword.charAt(0));
         }
         firstpunc = false;
      }
      if(lastpunc == false)
      {
         while(lastpunc == false)
         {
            lpunc = lpunc + Character.toString(tempword.charAt(tempword.length() - 1));
            tempword = tempword.substring(0,tempword.length() - 1);
            lastpunc = Character.isLetter(tempword.charAt(tempword.length() - 1));
         }
         lastpunc = false;
         String lpuncorder = "";
         int k = 0;
         for(int i = 0; i <= lpunc.length(); i++)
         {
            lpuncorder =  lpuncorder + Character.toString(lpunc.charAt(lpunc.length() - 1));
            lpunc = lpunc.substring(0,lpunc.length() - 1);
         }
         lpunc = lpuncorder + lpunc;
      }
   
      int fvplace, tempcnt, breaker;
      String tempstr, finword, chartostr, tempunc;
      char fv, tempchar;
      char[] vowel = {'a', 'e', 'i', 'o', 'u'};
      char[] vowely = {'a', 'e', 'i', 'o', 'u', 'y'};
      char[] punc = {'.', '!', '?', ',', ':', ':', '/'};
      
      fv = 'a';
      fvplace = 0;
      breaker = 0;
     
      for(int i = 0; i < tempword.length(); i++)
      {
         for(int k = 0; k < vowely.length; k++)
         {
            if(tempword.charAt(i) == vowely[k])
            {
               fv = tempword.charAt(i);
               breaker = 1;
               break;
            }
         }
         if(breaker == 1)
            break;
         fvplace++;
      }
      
      if(fvplace == 0 && fv != 'y')
      {
         finword = tempword + "way";
         if(upcase == true)
            finword = Character.toUpperCase(finword.charAt(0)) + finword.substring(1);
         if(firstpunc == false)
         {
            
            finword = fpunc + finword;
         }
         if(lastpunc == false)
         {
            finword = finword + lpunc;
         }
      }
      else if(fvplace == 0 && fv == 'y')
      {
         breaker = 0;
         
         for(int i = 0; i < tempword.length(); i++)
         {
            for(int k = 0; k < vowel.length; k++)
            {
            
               if(tempword.charAt(0) == vowel[k])
               {
                  breaker = 1;
                  break;
               }
            }
            if(breaker == 1)
               break;
               
            tempstr = tempword.substring(1);
            tempchar = tempword.charAt(0);
            chartostr = Character.toString(tempchar);
            tempword = tempstr + chartostr;
         }
         
         finword = tempword;
         if(upcase == true)
            finword = Character.toUpperCase(finword.charAt(0)) + finword.substring(1);
         
         if(finword.equals(word))
            finword = "INVALID";
         else
            finword = finword + "ay";
            
         if(firstpunc == false)
         {
            
            finword = fpunc + finword;
         }
         if(lastpunc == false)
            finword = finword + lpunc;
      }
      else if(fv == 'y')
      {
         breaker = 0;
         
         for(int i = 0; i < tempword.length(); i++)
         {
            for(int k = 0; k < vowely.length; k++)
            {
            
               if(tempword.charAt(0) == vowely[k])
               {
                  breaker = 1;
                  break;
               }
            }
            if(breaker == 1)
               break;
               
            tempstr = tempword.substring(1);
            tempchar = tempword.charAt(0);
            chartostr = Character.toString(tempchar);
            tempword = tempstr + chartostr;
         }
         
         finword = tempword;
         if(upcase == true)
            finword = Character.toUpperCase(finword.charAt(0)) + finword.substring(1);
         
         if(finword.equals(word))
            finword = "INVALID";
         else
            finword = finword + "ay";
            
         if(firstpunc == false)
         {
            
            finword = fpunc + finword;
         }
         if(lastpunc == false)
         {
            
            finword = finword + lpunc;
         }
      }
      else if(fv == 'u' && tempword.charAt(fvplace - 1) == 'q')
      {
         breaker = 0;
         
         for(int i = 0; i < tempword.length(); i++)
         {
            for(int k = 0; k < vowel.length; k++)
            {
            
               if(tempword.charAt(0) == vowel[k])
               {
                  breaker = 1;
                  break;
               }
            }
            if(breaker == 1)
               break;
               
            tempstr = tempword.substring(1);
            tempchar = tempword.charAt(0);
            chartostr = Character.toString(tempchar);
            tempword = tempstr + chartostr;
         }
         
         tempstr = tempword.substring(1);
         tempchar = tempword.charAt(0);
         chartostr = Character.toString(tempchar);
         tempword = tempstr + chartostr;
         
         finword = tempword;
         if(upcase == true)
            finword = Character.toUpperCase(finword.charAt(0)) + finword.substring(1);
         
         if(finword.equals(word))
            finword = "INVALID";
         else
            finword = finword + "ay";
            
         if(firstpunc == false)
         {
            
            finword = fpunc + finword;
         }
         if(lastpunc == false)
         {
            
            finword = finword + lpunc;
         }
      }
      else
      {
         breaker = 0;
         
         for(int i = 0; i < tempword.length(); i++)
         {
            for(int k = 0; k < vowel.length; k++)
            {
            
               if(tempword.charAt(0) == vowel[k])
               {
                  breaker = 1;
                  break;
               }
            }
            if(breaker == 1)
               break;
               
            tempstr = tempword.substring(1);
            tempchar = tempword.charAt(0);
            chartostr = Character.toString(tempchar);
            tempword = tempstr + chartostr;
         }
         
         finword = tempword;
         if(upcase == true)
            finword = Character.toUpperCase(finword.charAt(0)) + finword.substring(1);
         
         if(finword.equals(word))
            finword = "INVALID";
         else
            finword = finword + "ay";
            
         if(firstpunc == false)
         {
            
            finword = fpunc + finword;
         }
         if(lastpunc == false)
         {
            
            finword = finword + lpunc;
         }
      }
     
      return(finword);
   }

   public static void part_2_using_piglatenizeFile() throws IOException 
   {
      try
      {
         Scanner sc = new Scanner(System.in);
         System.out.print("Input Filename (Including .txt)? Example: PigLatin.txt:");
         String filename = sc.next();
         Scanner infile = new Scanner(new File(filename));  //PigLatin.txt
         System.out.print("Output Filename (Including .txt)? Example: PigLatinOut.txt:");
         String filenameOut = sc.next();
         piglatenizeFile( infile, filenameOut );
         System.out.println("Piglatin done!");
         sc.close();
      }
      catch(FileNotFoundException e)
      {
         System.out.println("File does not exist. Please try again");
         System.exit(0);
      }
   }
   
   public static void piglatenizeFile(Scanner infile, String filename) throws IOException
   {
      try
      {
         PrintStream fw = new PrintStream(new File (filename));
         
         while (infile.hasNextLine())
         {
            String line = infile.nextLine();
            if (line.isEmpty() || line.trim().equals("") || line.trim().equals("\n"))
            {
               fw.println("");
            }
            else
            {
               String[] splits = line.split(" ");
                
               for (String s : splits)
                  fw.print(pig(s)+ " ");
                
               fw.println();  
            }
         }
         fw.close();
      }
      catch(FileNotFoundException e)
      {
         JOptionPane.showMessageDialog(null,"The file could not be found.");
         System.exit(0);
      }
   
   }
}
