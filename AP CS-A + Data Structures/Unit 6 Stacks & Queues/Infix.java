  //Name: Sharath Byakod     Period: 6     Date: 1/22/16
  
import java.util.*;
public class Infix
{
   public static void main(String[] args)
   {
      System.out.println("Infix  -->  Postfix  -->  Evaluate");
      ArrayList<String> infixExp = new ArrayList<String>();
      
      // infixExp.add("3+4*5");
//       infixExp.add("3*4+5");
//       infixExp.add("(4+5)-5*3");
//       infixExp.add("(3+4)*(5+6)");
//       infixExp.add("(3*(4+5)-2)/5");
//       //infixExp.add("((4+5))");
//       infixExp.add("8+1*2-9/3");
       
      for( String s : infixExp )
      {
         String pf = infixToPostfix(s);
         System.out.println(s + "       " + pf + "       " + Postfix.eval(pf));
      }
   }
   
   public static String infixToPostfix(String infix)
   {
      String result = "";
      String nonsense = "";
      Stack<String> expression = new Stack<String>();
   
      for(int i = 0; i < infix.length(); i++)
      {
         if(infix.charAt(i) == '(')
            expression.push("" + infix.charAt(i));
         else if(infix.charAt(i) == ')')
         {
            while(expression.size() > 1)
            {
               if(expression.peek().equals("("))
                  nonsense += expression.pop();
               while((!expression.peek().equals("(")) && (expression.size() != 1))
                  result += expression.pop();   
            }
         }
         else if(Postfix.isOperator(infix.charAt(i)) == false)
            result += Character.toString(infix.charAt(i));
         else
         {
            int count = 0;
            
            while(count == 0)
            {
               if(expression.isEmpty())
                  break;
               else if((expression.peek().equals("(")) || (isLower(expression.peek().toCharArray()[0], infix.charAt(0))))
                  break;
               else
                  result += expression.pop(); 
            } 
            
            expression.push("" + infix.charAt(i));  
         }    
      }
     
      while(!expression.isEmpty())
      {
         result += expression.pop();
      }
      
      StringBuilder sb = new StringBuilder(result);
      
      for(int i = 0; i < sb.length(); i++)
         if(sb.charAt(i) == '(')
            sb.deleteCharAt(i);
      
      result = sb.toString(); 
     
      return(result);
   }
   
	//returns true if c1 has strictly lower precedence than c2
   public static boolean isLower(char c1, char c2)
   {
      if(c1 == '*')
         return(false);
      else if(c1 == '/')
         return(false);
      else if((c1 == '*') && (c2 == '+'))
         return(false);
      else if((c1 == '*') && (c2 == '-'))
         return(false);
      else if((c1 == '/') && (c2 == '+'))
         return(false);
      else if((c1 == '/') && (c2 == '-'))
         return(false);
      else
         return(true);
   }
}
	
	/*
 Infix  -->  Postfix  -->  Evaluate
 3+4*5       345*+       23
 3*4+5       34*5+       17
 (4+5)-5*3       45+53*-       -6
 (3+4)*(5+6)       34+56+*       77
 (3*(4+5)-2)/5       345+*2-5/       5
 8+1*2-9/3       812*+93/-       7
	*/
