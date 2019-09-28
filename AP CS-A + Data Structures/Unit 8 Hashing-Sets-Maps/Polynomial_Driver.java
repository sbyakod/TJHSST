 //Name:   Date:
 //modeling a polynomial using a treeMap
import java.util.*;
public class Polynomial_Driver
{
   public static void main(String[] args)
   {
      Polynomial poly = new Polynomial();
      poly.makeTerm(1, -4);
      poly.makeTerm(3, 2);
      poly.makeTerm(0, 2);
      System.out.println(poly.toString());
      double evaluateAt = 2.0;
      System.out.println("Evaluated at "+ evaluateAt +": " +poly.evaluateAt(evaluateAt));
   	   	
      Polynomial poly2 = new Polynomial();
      poly2.makeTerm(1, -5);
      poly2.makeTerm(4, 2);
      poly2.makeTerm(0, -3);
      poly2.makeTerm(2, 1); 
      System.out.println(poly2.toString());
   	
      System.out.println(poly.add(poly2));
      System.out.println(poly.multiply(poly2));
   }
}
interface PolynomialInterface
{
   public void makeTerm(Integer exp, Integer coef);
   public double evaluateAt(double x);
   public Polynomial add(Polynomial other);
   public Polynomial multiply(Polynomial other);
   public String toString();
}

class Polynomial implements PolynomialInterface
{
   TreeMap<Integer, Integer> tmap;

   public Polynomial()
   {
      tmap = new TreeMap<Integer, Integer>();
   }
   
   public void makeTerm(Integer exp, Integer coef)
   {
      makeTermHelper(exp, coef);
   }
   public void makeTermHelper(Integer exp, Integer coef)
   {
      tmap.put(exp, coef);
   }
   
   public double evaluateAt(double x)
   {
      return(evalHelper(x));
   }
   public double evalHelper(double x)
   {
   double answer = 0.0;
   
      for(Map.Entry<Integer, Integer> entry : tmap.entrySet())
      {
         Integer exp = entry.getKey();
         Integer coef = entry.getValue();
      
         answer += coef * Math.pow(x, exp);
      }
      
      return(answer);
   }
   
   public Polynomial add(Polynomial other)
   {
      return(addHelper(other));
   }
   public Polynomial addHelper(Polynomial other)
   {
      
   }
}
/*  
expected output
   2x^3 + -4x + 2
   10.0
   2x^4 + x^2 + -5x + -3
   2x^4 + 2x^3 + x^2 + -9x + -1
   4x^7 + -6x^5 + -6x^4 + -10x^3 + 22x^2 + 2x + -6
 */