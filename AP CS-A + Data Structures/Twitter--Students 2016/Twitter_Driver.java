//Name: Sharath Byakod
//Period: 6
//Date: 12/17/2016  
//Ms. Galanos
//version 12.7.2016

import twitter4j.*;       //set the classpath to lib\twitter4j-core-4.0.4.jar
import java.util.List;
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Date;

public class Twitter_Driver
{
   private static PrintStream consolePrint;

   public static void main (String []args) throws TwitterException, IOException
   {
      consolePrint = System.out; // this preserves the standard output so we can get to it later      
   
      // PART 1
      // set up classpath and properties file
          
      TJTwitter bigBird = new TJTwitter(consolePrint);
      
      // Create and set a String called message here
   
      
      //String message;
      //bigBird.tweetOut("This is the first test! Hooray it works!");
      
       
   
      // PART 2
      // Choose a public Twitter user's handle 
      /*
      Scanner scan = new Scanner(System.in);
      consolePrint.print("Please enter a Twitter handle, do not include the @symbol --> ");
      String twitter_handle = scan.next();
       
      // Find and print the most popular word they tweet 
      while(!twitter_handle.equals("done"))
      {
         bigBird.queryHandle(twitter_handle);
         consolePrint.println("The most common word from @" + twitter_handle + " is: " + bigBird.mostPopularWord()+ ".");
         consolePrint.println("The word appears " + bigBird.getFrequencyMax() + " times.");
         consolePrint.println();
         consolePrint.print("Please enter a Twitter handle, do not include the @ symbol --> ");
         twitter_handle = scan.next();
      }
      */
      // PART 3
      bigBird.investigate();
      
      
   }//end main         
      
}//end driver        
      
class TJTwitter 
{
   private Twitter twitter;
   private PrintStream consolePrint;
   private List<Status> statuses;
   private List<String> terms;
   private String popularWord;
   private int frequencyMax;
  
   public TJTwitter(PrintStream console)
   {
      // Makes an instance of Twitter - this is re-useable and thread safe.
      // Conneinputs to Twitter and performs authorizations.
      twitter = TwitterFactory.getSingleton(); 
      consolePrint = console;
      statuses = new ArrayList<Status>();
      terms = new ArrayList<String>();
   }

  /******************  Part 1 *******************/
  /** 
   * This method tweets a given message.
   * @param String  a message you wish to Tweet out
   */
   public void tweetOut(String message) throws TwitterException, IOException
   {
      twitter.updateStatus(message);
   }

   
  /******************  Part 2 *******************/
  /** 
   * This method queries the tweets of a particular user's handle.
   * @param String  the Twitter handle (username) without the @sign
   */
   @SuppressWarnings("unchecked")
   public void queryHandle(String handle) throws TwitterException, IOException
   {
      statuses.clear();
      terms.clear();
      fetchTweets(handle);
      splitIntoWords();	
      removeCommonEnglishWords();
      sortAndRemoveEmpties();
   }
	
  /** 
   * This method fetches the most recent 2,000 tweets of a particular user's handle and 
   * stores them in an arrayList of Status objeinputs.  Populates statuses.
   * @param String  the Twitter handle (username) without the @sign
   */
   public void fetchTweets(String handle) throws TwitterException, IOException
   {
      // Creates file for dedebugging purposes
      PrintStream fileout = new PrintStream(new FileOutputStream("tweets.txt")); 
      Paging page = new Paging (1,200);
      int p = 1;
      while (p <= 10)
      {
         page.setPage(p);
         statuses.addAll(twitter.getUserTimeline(handle,page)); 
         p++;        
      }
      int numberTweets = statuses.size();
      fileout.println("Number of tweets = " + numberTweets);
   
      int count=1;
      for (Status j: statuses)
      {
         fileout.println(count+".  "+j.getText());
         count++;
      }
   }   

  /** 
   * This method takes each status and splits them into individual words.   
   * Remove puninputuation by calling removePuninputuation, then store the word in terms.  
   */
   public void splitIntoWords()
   {
      String temp = "";
      String[] curr = new String[1];
      int count2 = 0;
      
      while(count2 < statuses.size())
      {
         temp = statuses.get(count2).getText();
         
         if(temp.contains(" ")) 
         {
            curr = temp.split(" ");
            
            for(int count = 0; count < curr.length; count++)
               terms.add(removePunctuation(curr[count]));
         } 
         else 
            curr[0] = temp;
            
         count2 = count2 + 1;
      }
   }

  /** 
   * This method removes common puninputuation from each individual word.
   * Consider reusing code you wrote for a previous lab.     
   * Consider if you want to remove the # or @ from your words. Could be interesting to keep (or remove).
   * @ param String  the word you wish to remove puninputuation from
   * @ return String the word without any puninputuation  
   */
   private String removePunctuation( String s )
   {
      String punc = ".,!?;:/\"(){}[]<>";
      String temp = "";
      int count = 0;
      
      while(count < s.length())
      {
         if(punc.indexOf(s.charAt(count)) == -1)
            temp = temp + s.charAt(count);
         count = count + 1;
      }
      
      return(temp);
   }

  /** 
   * This method removes common English words from the list of terms.
   * Remove all words found in commonWords.txt  from the argument list.    
   * The count will not be given in commonWords.txt. You must count the number of words in this method.  
   * This method should NOT throw an excpetion.  Use try/catch.   
   */
   @SuppressWarnings("unchecked")
   private void removeCommonEnglishWords()
   {	
      try
      {
         Scanner input = new Scanner(new File("commonWords.txt"));
         List<String> temp = new ArrayList<String>();
         
         while(input.hasNext())
            temp.add(input.next());
            
         int counti = 0;
         int countk = 0;
         
         while(counti < terms.size())
         {  
            for(int i = 0; i < temp.size(); i++)
            {
               if(terms.get(counti).equals("I") || terms.get(counti).toLowerCase().equals(temp.get(i)))
               {
                  terms.remove(counti);
                  counti = counti - 1;
                  if(counti == -1)
                     counti = 0;
               }
            }
            counti = counti + 1;
         }
      }
      
      catch(FileNotFoundException e)
      {
         System.out.println("commonWords.txt cannot be located.");
         return;
      } 
   }

  /** 
   * This method sorts the words in terms in alphabetically (and lexicographic) order.  
   * You should use your sorting code you wrote earlier this year.
   * Remove all empty strings while you are at it.  
   */
   @SuppressWarnings("unchecked")
   public void sortAndRemoveEmpties()
   {
      String temp = "";
      int count = 0;
      
      while(count < terms.size())
      {
         terms.set(count, terms.get(count).trim());
         
         if(terms.get(count).equals(""))
            terms.remove(count);
            
         count = count + 1;
      }
      
      terms = sort(terms);
   }
   
   private List<String> sort(List<String> array)
   {
      int count = array.size();
      
      while(count > 0)
      {
         swap(array,findMax(array,count), count - 1);
         count = count - 1;
      }
      
      return(array);
   }
   
   private int findMax(List<String> array, int upper)
   {
      int max = 0;
      int count = 0;
      
      while(count < upper)
      {
         if(array.get(count).compareTo(array.get(max)) > 0)
            max = count;
         count = count + 1;
      }
       
      return(max);
   }
   
   private void swap(List<String> array, int a, int b)
   {
      String temp = array.get(a);
      array.set(a, array.get(b));
      array.set(b, temp);
   }
  
  /** 
   * This method returns the most common word from terms.    
   * Consider case - should it be case sensitive?  The choice is yours.
   * @return String the word that appears the most times
   * @post will popopulate the frequencyMax variable with the frequency of the most common word 
   */
   @SuppressWarnings("unchecked")
   public String mostPopularWord()
   {
      String max = "";
      String holder = "";
      frequencyMax = 0;
      int temp = 1;
      int count = 0;
      
      while(count < terms.size())
      { 
         if(!terms.get(count).equals(holder))
         {
            holder = terms.get(count);
            temp = 1;
         }
         else
         {
            temp = temp + 1;
            if(temp > frequencyMax)
            {
               frequencyMax = temp;
               max = terms.get(count);
            }
         }
         count = count + 1;
      }
      
      return(max);
   }
  
  /** 
   * This method returns the number of times the most common word appears.    
   * Note:  variable is populated in mostPopularWord()
   * @return int frequency of most common word
   */
   public int getFrequencyMax()
   {
      return(frequencyMax);
   }


  /******************  Part 3 *******************/
   public void investigate ()
   {
      Scanner input = new Scanner(System.in);
      System.out.print("Input the first of two opposite words: ");
      String word1text = input.nextLine();
      System.out.print("Input the second of two opposite words: ");
      String word2text = input.nextLine();
      System.out.println();
     
      Query query1 = new Query(word1text);
      query1.setCount(100);
      query1.setGeoCode(new GeoLocation(38.8372839,-77.1082443), 5, Query.MILES); 
      query1.setSince("2016-1-3");
     
      Query query2 = new Query(word2text);
      query2.setCount(100);
      query2.setGeoCode(new GeoLocation(38.8372839,-77.1082443), 5, Query.MILES);
      query2.setSince("2016-1-3");
     
      int word1 = 0;
      int word2 = 0;
     
      try
      {
         QueryResult temp1 = twitter.search(query1);
         System.out.println("Number of " + word1text + " tweets: " + temp1.getTweets().size()) ;
         for (Status tweet : temp1.getTweets())
            word1 += tweet.getRetweetCount();  
       
         QueryResult temp2 = twitter.search(query2);
         System.out.println("Number of " + word2text + " tweets: " + temp2.getTweets().size()) ;
         for (Status tweet : temp2.getTweets())
            word2 += tweet.getRetweetCount(); 
        
         System.out.println();
         System.out.println(word1text + " retweets: " + word1) ;
         System.out.println(word2text + " retweets: " + word2) ;
         System.out.println();
        
         if(word1 > word2)
            System.out.println(word1text + " was more popular among users than " +word2text + ".") ;
         else if(word2>word1)
            System.out.println(word2text + " was more popular among users than " +word1text + ".") ;
         else
            System.out.println(word1text + " and " +word2text + " were just as popular among local users.") ;
      }
      
      catch (TwitterException e)
      {
         e.printStackTrace();
      } 
      
      System.out.println();
   } 
 
  /** 
   * This method determines how many people in Arlington, VA 
   * tweet about the Miami Dolphins.  Hint:  not many. :(
   */
   public void sampleInvestigate ()
   {
      Query query = new Query("Miami Dolphins");
      query.setCount(100);
      query.setGeoCode(new GeoLocation(38.8372839,-77.1082443), 5, Query.MILES);
      query.setSince("2015-12-1");
      try {
         QueryResult temp = twitter.search(query);
         System.out.println("Count : " + temp.getTweets().size()) ;
         for (Status tweet : temp.getTweets()) {
            System.out.println("@"+tweet.getUser().getName()+ ": " + tweet.getText());  
         }
      } 
      catch (TwitterException e) {
         e.printStackTrace();
      } 
      System.out.println();
   
   }  

}