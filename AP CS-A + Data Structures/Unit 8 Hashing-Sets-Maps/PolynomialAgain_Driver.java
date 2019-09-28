/* Name:       Date:
 modeling a polynomial using a hashMap
*/ 
import java.util.*;
public class PolynomialAgain_Driver
{
   public static void main(String[] args)
   {
      PolynomialAgain poly = new PolynomialAgain();
      poly.makeTerm(1, -4);
      poly.makeTerm(3, 2);
      poly.makeTerm(0, 2);
      System.out.println(poly.toString());
      System.out.println(poly.evaluateAt(2.0));
   	
      PolynomialAgain poly2 = new PolynomialAgain();
      poly2.makeTerm(1, -5);
      poly2.makeTerm(4, 2);
      poly2.makeTerm(0, -3);
      poly2.makeTerm(2, 1); 
      System.out.println(poly2.toString());
   	
      System.out.println(poly.add(poly2));
      //System.out.println(poly.multiply(poly2));
   }
}
interface PolynomialAgainInterface
{
   public void makeTerm(Integer exp, Integer coef);
   public double evaluateAt(double x);
   public PolynomialAgain add(PolynomialAgain other);
   //public PolynomialAgain multiply(PolynomialAgain other);
   public String toString();
}

class PolynomialAgain implements PolynomialAgainInterface
{
   private HashSet<Term> poly;
   public PolynomialAgain()
   {
     
   }
   public void makeTerm(Integer exp, Integer coef)
   {
      
   }
   public String toString()
   {
     
   }
   
   public double evaluate(double x)
   {
     
   }
   public PolynomialAgain add(PolynomialAgain other)
   {
    
   }
}

class Term 
{
   public int power;    //public is easier to access!
   public int coef;
				
   public Term(int p, int c)
   {
      power = p;
      coef = c;
   }
   public int hashCode()  // based on power
   { 
      return ((Integer)power).hashCode();    //surprise!
   }
   public boolean equals(Object obj)  //based on power
   {
      return power == ((Term)obj).power; 
   }
   public String toString()
   {
      if( power == 0 )
         return ""+coef;
      if( power == 1 )
         return coef+"x";
      if( coef == 1)
         return "x^"+power;   
      return coef+"x^"+power;
   }
}

/*  
expected output
   2x^3 + -4x + 2
   10.0
   2x^4 + 1x^2 + -5x + -3
   2x^4 + 2x^3 + 1x^2 + -9x + -1
 */