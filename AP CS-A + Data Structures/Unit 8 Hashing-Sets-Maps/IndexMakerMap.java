// Name: Sharath Byakod    Period: 6   Date: 3/15/17

//  This program takes a text file, creates an index (by line numbers)
//  for all the words in the file and writes the index
//  into the output file.  The program prompts the user for the file names.

import java.io.*;
import java.util.*;

public class IndexMakerMap
{
   public static void main(String[] args) throws IOException
   {
      Scanner keyboard = new Scanner(System.in);
      System.out.print("\nEnter input file name: ");
      String infileName = keyboard.nextLine().trim();
      Scanner inputFile = new Scanner(new File(infileName));
      String outfileName = "fishIndex.txt";
      PrintWriter outputFile = new PrintWriter(new FileWriter(outfileName));
      indexDocument(inputFile, outputFile);
      inputFile.close(); 						
      outputFile.close();
      System.out.println("Done.");
   }

   public static void indexDocument(Scanner inputFile, PrintWriter outputFile)
   {
      DocumentIndex index = new DocumentIndex(); 	
      int lineNum = 0;
      
      while(inputFile.hasNextLine())
      {
         lineNum++;
         index.addAllWords(inputFile.nextLine(), lineNum);
      }
      
      String temp = "";
      
      for(String entry : index.keySet())
      {
         temp = entry + " " +  index.get(entry);
         temp = temp.replace("[", "");
         temp = temp.replace("]", "");
         outputFile.println(temp);
      }
         
      outputFile.close();    
   }
}

class DocumentIndex extends TreeMap<String, ArrayList<Integer>>
{
   //TreeMap<String, ArrayList<Integer>> tmap = new TreeMap<String, ArrayList<Integer>>(); 

   public void addWord(String word, int lineNum)
   {
      word = word.toUpperCase();
      
      if(this.containsKey(word) == false)
      {
         ArrayList<Integer> numsList = new ArrayList<Integer>();
         numsList.add(lineNum);
         this.put(word, numsList);   
      }
      else
      {
         ArrayList<Integer> numsList = this.get(word);
         numsList.add(lineNum);
         this.put(word, numsList);
      }
   }
   
 /** extracts all the words from str, skipping punctuation and whitespace 
 and for each word calls addWord(word, num).  A good way to skip punctuation 
 and whitespace is to use String's split method, e.g., split("[., \"!?]") */
   public void addAllWords(String str, int lineNum) 
   {
      String[] array = str.split("[., /\"!;:?]");
      int i = 0;
      
      while(i < array.length)
      {
         if(!array[i].equals(" ") && !array[i].equals(""))
            addWord(array[i], lineNum);
         i++;   
      }
   }
}