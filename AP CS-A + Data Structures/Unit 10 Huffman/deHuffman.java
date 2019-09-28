// Name: Sharath Byakod     Period: 6     Date: 5/24/17

import java.util.Scanner;
import java.io.*;

public class deHuffman
{
   public static void main(String[] args) throws IOException
   {
      Scanner keyboard = new Scanner(System.in);
      System.out.print("\nWhat binary message (middle part)? ");
      String middlePart = keyboard.next();
      Scanner sc = new Scanner(new File("message."+middlePart+".txt")); 
      String binaryCode = sc.next();
      Scanner huffLines = new Scanner(new File("scheme."+middlePart+".txt")); 
      	
      TreeNode root = huffmanTree(huffLines);
      String message = dehuff(binaryCode, root);
      System.out.println(message);
      	
      sc.close();
      huffLines.close();
   }
   
   public static TreeNode huffmanTree(Scanner huffLines)
   {
      TreeNode head = new TreeNode(null);
      
      while(huffLines.hasNext())
      {   
         String str = huffLines.nextLine();
         String curchar = str.substring(0,1);
         str = str.substring(1);
         TreeNode curr = head;
         
         while(str.length() != 0)
         {
            if(!str.substring(0,1).equals("0"))
            {
               if(curr.getRight() != null)
                  ;
               else
                  curr.setRight(new TreeNode(null));
                  
               curr = curr.getRight();
               str = str.substring(1);
            }
            else
            {
               if(curr.getLeft() != null)
                  ;
               else
                  curr.setLeft(new TreeNode(null));
                  
               curr = curr.getLeft();
               str = str.substring(1);
            }	
         }
         
         curr.setValue(curchar);
      }
      
      return(head);
   }
   
   public static String dehuff(String text, TreeNode root)
   {
      String s = "";
      TreeNode t = root;
      int x = 1;
      
      while(x <= text.length())
      {
         if(Integer.parseInt(text.substring(x - 1, x)) != 0)
            t = t.getRight();
         else
            t = t.getLeft();
         if(t.getValue() != null)
         {
            s += t.getValue();
            t = root;
         }
         
         x++;  
      }
      
      return(s);
   }
}

 /* TreeNode class for the AP Exams */
// class TreeNode
// {
   // private Object value; 
   // private TreeNode left, right;
//    
   // public TreeNode(Object initValue)
   // { 
      // value = initValue; 
      // left = null; 
      // right = null; 
   // }
//    
   // public TreeNode(Object initValue, TreeNode initLeft, TreeNode initRight)
   // { 
      // value = initValue; 
      // left = initLeft; 
      // right = initRight; 
   // }
//    
   // public Object getValue()
   // { 
      // return value; 
   // }
//    
   // public TreeNode getLeft() 
   // { 
      // return left; 
   // }
//    
   // public TreeNode getRight() 
   // { 
      // return right; 
   // }
//    
   // public void setValue(Object theNewValue) 
   // { 
      // value = theNewValue; 
   // }
//    
   // public void setLeft(TreeNode theNewLeft) 
   // { 
      // left = theNewLeft;
   // }
//    
   // public void setRight(TreeNode theNewRight)
   // { 
      // right = theNewRight;
   // }
// }