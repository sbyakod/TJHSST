//Name: Sharath Byakod     Period: 6      Date: 9/22/16  
public class Sentence_Driver
{
   public static void main(String[] args)
   {
      System.out.println("PALINDROME TESTER");
      Sentence s = new Sentence( "\"Hello there!\" she said." );
      System.out.println( s.getSentence() );
      System.out.println( s.getNumWords() );
      System.out.println( s.isPalindrome() );
      System.out.println();
      
      s = new Sentence( "A Santa lived as a devil at NASA." );
      System.out.println( s.getSentence() );
      System.out.println( s.getNumWords() );
      System.out.println( s.isPalindrome() );
      System.out.println();
     
   
      s = new Sentence( "Flo, gin is a sin! I golf." );
      System.out.println( s.getSentence() );
      System.out.println( s.getNumWords() );
      System.out.println( s.isPalindrome() );
      System.out.println();
      
   
      s = new Sentence( "Eva, can I stab bats in a cave?" );
      System.out.println( s.getSentence() );
      System.out.println( s.getNumWords() );
      System.out.println( s.isPalindrome() );
      System.out.println();
   
      s = new Sentence( "Madam, I'm Adam." );
      System.out.println( s.getSentence() );
      System.out.println( s.getNumWords() );
      System.out.println( s.isPalindrome() );
      System.out.println();
      
   // Lots more test cases.  Test every line of code.  Test
   // the extremes, test the boundaries.  How many test cases do you need?
   
   }
}
class Sentence
{
   private String mySentence;
   private int myNumWords;
   private static String[] wordar;
   private  static Boolean flag = false; 
   
   //Constructor.  Creates sentence from String str.
   //						Finds the number of words in sentence.
   //Precondition:  Words in str separated by exactly one blank.
   public Sentence( String str )
   { 
      mySentence = str;
      wordar = mySentence.split(" ");
      myNumWords = wordar.length;
      System.out.println(myNumWords);
   }
   
   public int getNumWords()
   {  
      return myNumWords;  
   }
   
   public String getSentence()
   {
      return mySentence; 
   }
   
   //Returns true if mySentence is a palindrome, false otherwise.
   public boolean isPalindrome()
   {
      String tempstr = mySentence;
      
      tempstr = removeBlanks(tempstr);
      tempstr = lowerCase(tempstr);
      tempstr = removePunctuation(tempstr);
      
      return(isPalindrome(tempstr, 0, tempstr.length()));
   }
   //Precondition: s has no blanks, no punctuation, and is in lower case.
   //Returns true if s is a palindrome, false otherwise.
   private static boolean isPalindrome( String s, int start, int end )
   {
      
      String tempstr = s;         
      int first = start;
      int last = end;
       
      if(first >= last)
      {
         flag = true;
         return flag;
      }
      else
      {
         if(tempstr.charAt(first) == tempstr.charAt(last - 1))
         {
            first = first + 1;
            last = last - 1;
            if (flag == false) 
            {
               isPalindrome(tempstr, first, last);
            }
         }
      }
      
      return flag;
   }
   //Returns copy of String s with all blanks removed.
   //Postcondition:  Returned string contains just one word.
   private static String removeBlanks( String s )
   {  
      String temp = "";
      for(int i = 0; i < wordar.length; i++)
         temp = temp + wordar[i];
      return(temp);
   }
   
   //Returns copy of String s with all letters in lowercase.
   //Postcondition:  Number of words in returned string equals
   //						number of words in s.
   private static String lowerCase( String s )
   {  
      return(s.toLowerCase());
   }
   
   //Returns copy of String s with all punctuation removed.
   //Postcondition:  Number of words in returned string equals
   //						number of words in s.
   private static String removePunctuation( String s )
   { 
      boolean temp = false;
      String tempstr = "";
      for(int i = 0; i < s.length(); i++)
      {
         temp = Character.isLetter(s.charAt(i));
         if(temp == true || Character.toString(s.charAt(i)).equals(" "))
            tempstr = tempstr + Character.toString(s.charAt(i));
      }
      
      return(tempstr);
   }
}
