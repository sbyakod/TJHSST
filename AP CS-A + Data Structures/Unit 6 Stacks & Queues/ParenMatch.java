//Name: Sharath Byakod     Period: 6     Date: 1/22/16

import java.util.*;
public class ParenMatch
{
   public static final String left  = "([{<";
   public static final String right = ")]}>";
   public static void main(String[] args)
   {
      System.out.println("Parentheses Match");
      ArrayList<String> parenExp = new ArrayList<String>();
      
      /*parenExp.add("5+7");
      parenExp.add("(5+7)");
      parenExp.add(")5+7(");
      parenExp.add("((5+7)*3)");
      parenExp.add("<{5+7}*3>");
      parenExp.add("[(5+7)*]3");
      parenExp.add("(5+7)*3");
      parenExp.add("5+(7*3)");
      parenExp.add("((5+7)*3");
      parenExp.add("[(5+7]*3)");
      parenExp.add("[(5+7)*3])");
      parenExp.add("([(5+7)*3]");*/
                    
      for( String s : parenExp )
      {
         boolean good = checkParen(s);
         if(good)
            System.out.println(s + "\t good!");
         else
            System.out.println(s + "\t BAD");
      }
   }
   public static boolean checkParen(String exp)
   {
      Stack<String> expression = new Stack<String>();
      int count = 0;
      int nonsense = 0;
   
      while(count < exp.length())
      {
         if(left.contains("" + exp.charAt(count)))
            expression.push("" + exp.charAt(count));
         else if(right.contains("" + exp.charAt(count)))
         {
            if(expression.isEmpty())
               return(false);
            else
               nonsense++;
            if(right.indexOf(exp.charAt(count)) != left.indexOf(expression.pop()))
               return(false);
            else
               nonsense++;
         }
         
         count++;
      }
      
      if(expression.isEmpty())
         return(true);
      else
         return(false);
   }
}

/*
 Parentheses Match
 5+7	 good!
 (5+7)	 good!
 )5+7(	 BAD
 ((5+7)*3)	 good!
 <{5+7}*3>	 good!
 [(5+7)*]3	 good!
 (5+7)*3	 good!
 5+(7*3)	 good!
 ((5+7)*3	 BAD
 [(5+7]*3)	 BAD
 [(5+7)*3])	 BAD
 ([(5+7)*3]	 BAD
 */
