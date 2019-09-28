//Name: Sharath Byakod     Period: 6     Date: 1/22/16
   
import java.util.*;
public class Postfix
{
   public static void main(String[] args)
   {
      System.out.println("Postfix  -->  Evaluate");
      ArrayList<String> postExp = new ArrayList<String>();
      /*postExp.add("345*+");
      postExp.add("34*5+");
      postExp.add("45+53*-");
      postExp.add("34+56+*");
      postExp.add("345+*2-5/");
      postExp.add("812*+93/-");*/
      
      for( String pf : postExp )
      {
         System.out.println(pf + "\t\t\t\t\t" + eval(pf));
      }
   }
   
   public static int eval(String postfix)
   {
      Stack<Integer> expression = new Stack<Integer>();
      int count = 0;
      
      while(count < postfix.length())
      {
         if(!isOperator(postfix.charAt(count))) 
            expression.push(Integer.parseInt("" + postfix.charAt(count)));
         else
         {
            int first = expression.pop();
            int second = expression.pop();
            expression.push(eval(first, second, postfix.charAt(count)));
         }
            
         count++;
      }
      
      return(expression.peek());
   }
   
   public static int eval(int a, int b, char ch)
   {
      if(ch == '+') 
         return(a+b);
      else if(ch == '-')
         return(b-a);
      else if(ch == '*')
         return(a*b);
      else if(ch == '/')
         return(b/a);
      else
         return((int)Math.pow(a, b));         
   }
   
   public static boolean isOperator(char ch)
   {
      String[] operators = {"+", "-", "*", "/", "^"};
      boolean flag = false;
      
      for(int i = 0; i < operators.length; i++)
         if(operators[i].equals(Character.toString(ch)))
            flag = true;
      
      return(flag);
   }
}

/*
 Postfix  -->  Evaluate
 345*+		23
 34*5+		17
 45+53*-		-6
 34+56+*		77
 345+*2-5/		5
 812*+93/-		7  
 */