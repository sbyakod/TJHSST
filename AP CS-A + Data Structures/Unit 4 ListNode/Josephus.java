// name:     date:  

import java.util.*;
import java.io.*;
import javax.swing.JOptionPane;

public class Josephus
{
   private static String WINNER = "Josephus";
   public static void main(String[] args) throws FileNotFoundException
   {
      /* run it first with J_numbers.txt  */
      ListNode p = null;
      int n = Integer.parseInt(JOptionPane.showInputDialog("How many names (2-20)?"));
      File f = new File("J_numbers.txt");
      p = readNLinesOfFile(n, f);
      int countOff = Integer.parseInt(JOptionPane.showInputDialog("How many names to count off each time?"));
      countingOff(p, countOff, n);
      
   	/* run it next with J_names.txt  */
      System.out.println("\n ****  Now start all over.  Enter the winning position in the JOptionPane.  *** \n");
      p = readNLinesOfFile(n, new File("J_names.txt"));
      int winPos = Integer.parseInt(JOptionPane.showInputDialog("Enter Josephus's preferred position."));
      replaceAt(p, WINNER, winPos);
      countingOff(p, countOff, n);
      System.out.println(WINNER + " wins!");    
   }
   /* reads the names, builds the linked list.
	  */
   public static ListNode readNLinesOfFile(int n, File f) throws FileNotFoundException
   {

   }
  /* Runs a Josephus game, counting off and removing each name. Prints after each removal.
     Ends with one remaining name, who is the winner. 
	  */
   public static void countingOff(ListNode p, int count, int n)
   {

   }
   /* removes the node after counting off count-1 nodes.
	  */
   private static ListNode remove(ListNode p, int count)
   {

   }
   /* prints the circular linked list.
	  */
   public static void print(ListNode p)
   {
   
   }
 /* helper method to build the list.  Creates the node, then
    inserts it in the circular linked list.
	 */
   private static ListNode insert(ListNode p, Object obj)
   {
   
   }

	/* replaces the value (the string) at the winning node.
	   */
   private static void replaceAt(ListNode p, Object obj, int pos)
   {
   
   }
}

  //the College Board's standard ListNode class
class ListNode
{
   private Object value;
   private ListNode next;
   public ListNode(Object v, ListNode n)
   {
      value=v;
      next=n;
   }
   public Object getValue()
   {
      return value;
   }
   public ListNode getNext()
   {
      return next;
   }
   public void setValue(Object newv)
   {
      value=newv;
   }
   public void setNext(ListNode newn)
   {
      next=newn;
   }
}