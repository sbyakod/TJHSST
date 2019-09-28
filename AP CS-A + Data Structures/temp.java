import java.util.*;

public class temp
{
   public static void main(String[] args)
   {
   
   int[] intArray = {5, 2, 16,8,9,3,4,0};
   
      for (int q = 0; q < intArray.length-1; q++)
      
         if ( intArray[q] > intArray[q+1])
         
         {
         
            int temp = intArray[q];
         
            intArray[q] = intArray[q+1];
         
            intArray[q+1] = temp;
         
         }
      for(int i = 0; i < intArray.length; i++)
         System.out.print(intArray[i]);
   }
}