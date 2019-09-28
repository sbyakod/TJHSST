//Name: Sharath Byakod     Period: 6      Date: 9/30/16

import java.util.*;

public class StringCoderDriver
{
   public static void main(String[] args)
   {
      StringCoder sc = new StringCoder("sixtyzipperswerequicklypickedfromthewovenjutebag"); 
      StringPart[] sp = sc.encodeString("overeager");
      for(int i=0; i<sp.length; i++)
         System.out.print(sp[i]+", ");   // (37, 3), (14, 2), (46, 2), (9, 2),
      System.out.println();
      String s = sc.decodeString(sp);
      System.out.println(s);             // overeager
   
      StringPart[] sp2 = sc.encodeString("kippers");
      for(int i=0; i<sp2.length; i++)
         System.out.print(sp2[i]+", ");  // (20, 1), (6, 6),  
      System.out.println();
      String s2 = sc.decodeString(sp2);
      System.out.println(s2);            // kippers
   
      StringPart[] sp3 = sc.encodeString("colonials");
      for(int i=0; i<sp3.length; i++)
         System.out.print(sp3[i]+", ");  // (19, 1), (31, 1), (21, 1), (31, 1), (40, 1), (1, 1), (46, 1), (21, 1), (0, 1), 
      System.out.println();
      String s3 = sc.decodeString(sp3);
      System.out.println(s3);            // colonials
   
      StringPart[] sp4 = sc.encodeString("werewolf");
      for(int i=0; i<sp4.length; i++)
         System.out.print(sp4[i]+", ");   // (12, 4), (36, 2), (21, 1), (29, 1),
      System.out.println();
      String s4 = sc.decodeString(sp4);
      System.out.println(s4);             // werewolf
   }
}

  
class StringCoder
{
   private String masterString;

   public StringCoder(String master)
   {
      masterString = master; 
   }

   public String decodeString(StringPart[] parts)
   {
      int start = 0;
      int length = 0;
      String word = new String("");
      for(int k = 0; k < parts.length; k++)
      {
         start = parts[k].getStart();
         length = parts[k].getLength();
         word = word + masterString.substring(start, start + length);
      }
      return word;
   }

   private StringPart findPart(String str)
   { 
      int x = 0;
      String s = str.substring(0, x);
      while( masterString.contains(s) )
      {
         x++;
         if(x > str.length())
            break;
         s = str.substring(0, x);
      }     
      s = str.substring(0, x - 1);
      int start = masterString.indexOf(s);
      StringPart sp = new StringPart(start, s.length());
      return sp;
   }

   public StringPart[] encodeString(String word)
   {
      StringPart[] tempar = new StringPart[100];
      
      int i = 0;
      int ending = 0;
      
      String part = "";
      
      while(i < tempar.length)
      {
         if(i == 0)
         {
            tempar[i] = findPart(word);
            ending = tempar[i].getLength();
            i++;
         }
         else
         {
            part = word.substring(ending);
            tempar[i] = findPart(part);
            ending = ending + tempar[i].getLength();
            i++;
         }
      }
      
      int size = 0;
      
      while(tempar[size].getLength() != 0)
      {
         size++;
      }
      
      StringPart[] ecparts = new StringPart[size];
      
      for(int k = 0; k < ecparts.length; k++)
      {
         ecparts[k] = tempar[k];
      }
      
      return(ecparts);
   }
}


class StringPart
{

   private int myStart, myLength;
   
   public StringPart(int start, int length)
   {
      myStart = start;
      myLength = length;
   }

   public int getStart()
   { 
      return myStart;
   }

   public int getLength()
   { 
      return myLength;
   }
   public String toString()
   {
      return "(" + myStart + ", " + myLength + ")";
   }
}


/****************  output  ****************
(37, 3), (14, 2), (46, 2), (9, 2), 
overeager
(20, 1), (6, 6), 
kippers
(19, 1), (31, 1), (21, 1), (31, 1), (40, 1), (1, 1), (46, 1), (21, 1), (0, 1), 
colonials
(12, 4), (36, 2), (21, 1), (29, 1), 
werewolf

*****************************************/