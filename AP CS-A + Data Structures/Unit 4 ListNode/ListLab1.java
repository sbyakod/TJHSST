//Name: Sharath Byakod     Period: 6     Date: 11/23/16
  
import java.util.*;

public class ListLab1
{
   public static void main(String[] args)
   {
      ListNode head = new ListNode("hello", null);
      head = new ListNode("foo", head);
      head = new ListNode("boo", head);
      head = new ListNode("nonsense", head);
      head = new ListNode("computer",
         	new ListNode("science",
         		new ListNode("java",
         			new ListNode("coffee", head)
         		)
         	)
         );
      print(head);
      print(head);
      
      /**** uncomment the code below for ListLab1 Extension  ****/
      
      ListNode zz = copyList(head);
      print(head);
      
      
      System.out.println("First = " + first(head));
      System.out.println("Second = " + second(head));
      ListNode p = pointerToLast(head);
      System.out.println("Pointer to Last = " + p.getValue()+ " at " + p);
      ListNode c = copyOfLast(head);
      System.out.println("Copy of Last =    " + c.getValue()+ " at " + c);
   	 	
      Scanner in = new Scanner(System.in);
      System.out.print("Insert what? ");
      String x = in.next();
      head = insertFirst(head, x);
      
      
      print(head);
      
      
      head = insertLast(head, x);
      print(head);
   }
   
   public static void print(ListNode head)
   {
      System.out.print("[");
      while(head != null)
      {
         System.out.print(head.getValue());
         head = head.getNext();
         if(head != null)
            System.out.print(", ");
      }
      System.out.println("]");
   }
   
   private static ListNode copyNode(ListNode arg)
   {
      ListNode temp = new ListNode(arg.getValue(), arg.getNext());
      return temp;
   }
   
   private static ListNode copyList(ListNode arg)
   {
      if(arg.getNext() != null)
         return(null);
      else
         return(new ListNode(arg.getValue(), copyList(arg.getNext())));
   }
   
   private static ListNode rest(ListNode h)
   {
      if(h.getNext() == null)
         return(null);
      else
         return(new ListNode(h.getNext().getValue(), rest(h.getNext())));
   }
   
   public static Object first(ListNode head)
   {
      if(head.getValue() == null)
         return(null);
      else
         return(head.getValue());
   }

   public static Object second(ListNode head)
   {
      ListNode temp = rest(head);
      return(temp.getValue());
   }
   
   public static ListNode pointerToLast(ListNode head)
   {
      while(head.getNext() != null)
         head = head.getNext();
      return(head);
   }
   
   public static ListNode copyOfLast(ListNode head)
   {
      while(head.getNext() != null)
         head = head.getNext();
      return(copyNode(head));
   }
   
   public static ListNode insertFirst(ListNode head, Object arg)
   {
      if(head == null)
         return(null);
      else
      {
         ListNode temp = new ListNode(arg, head);
         return temp;  
      }
   }
   
   public static ListNode insertLast(ListNode head, Object arg)
   {
   
      ListNode temp = head;
      if(temp == null)
         return(new ListNode(arg, null));
      while(temp.getNext() != null)
         temp = temp.getNext();
      temp.setNext(new ListNode(arg, null));
      return(head);
   }
}
