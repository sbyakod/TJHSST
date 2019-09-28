   //name:      date:
 import java.util.*;
 import java.io.*;
       
public class TreePriorityQueue_Driver
{
   private static TreePriorityQueue tpq = null;
   public static void main(String[] args)
   {
      tpq = new TreePriorityQueue();
      int[] array = {13, 11, 14, 11, 15, 14, 14};
       //	int[] array = {4, 6, 5, 7}; 
      //  int[] array = {7, 6, 4, 5}; 
         //int[] array = {7, 6, 4, 5, 4, 4};
      //   int[] array = {4, 5, 4, 4, 7, 6, 7, 7};
        
      tpq = build( tpq, array );      
      System.out.println("Peek min: " + tpq.peekMin());
      System.out.println("Removing");
      while( !tpq.isEmpty() )
         System.out.println( "     " + tpq.removeMin() );
   }
   
   public static TreePriorityQueue build( TreePriorityQueue tpq, int[] array )
   {
      for( int x : array )
         tpq.add(x);
      return tpq;
   }
}

class TreePriorityQueue
{
   private TreeNode root;
   
   public TreePriorityQueue()
   {   root = null;  }
   
   //postcondition:  returns true if the priority queue is empty;
   //					  otherwise, returns false
   public boolean isEmpty()
   {  
      return root == null;
   }
   
   //postcondition:  obj has been added to the priority queue
   public void add(Object obj)
   {	
      root = addHelper((Comparable) obj, root);  
   }
   
   //postcondition:  obj has been added to the subtree rooted at t;
   //					  the updated subtree is returned
   private TreeNode addHelper(Comparable obj, TreeNode t)
   {
      if(t == null)
         return(new TreeNode(new Item(obj), null, null));
      
      if(obj.compareTo(((Item)(t.getValue())).getData()) < 0)
         t.setLeft((addHelper(obj, t.getLeft()))); 
      else if(obj.compareTo(((Item)(t.getValue())).getData()) > 0)
         t.setRight((addHelper(obj, t.getRight())));
      else
      {
         Item temp = (Item)t.getValue();
         temp.incrementCount();
         t.setValue(temp);
      }
      
      return(t);       
   }
   			
   					
   //precondition:  the priority queue is not empty
   //postcondition:  a data value of smallest priority has been 
   //						removed and returned
   public Object removeMin()
   { 
   String target = peekMin();
      TreeNode current = root;
      TreeNode parent = null;
      boolean isRight = false;
      while(current !=null)
      {
         int compare = target.compareTo((String)current.getValue());
        // ------->  your code goes here
         if(compare == 0 && parent == null) //base case (if target is root)
         {
            if(current.getLeft() == null && current.getRight() == null) //just root
            {
               root = null;
               current = null;
            }
            else if(current.getLeft() != null && current.getRight() == null) //root has left child
            {
               root = current.getLeft();
               current = null;
            }
            else if(current.getLeft() == null && current.getRight() != null) //root has right child
            {
               root = current.getRight();
               current = null;
            }
            else //root has both left and right children
            {
               TreeNode hold = current;
               TreeNode holdParent = parent;
               parent = current;
               current = current.getLeft();
               isRight = false;
               boolean onlyLeft = true;
            
               while(current.getRight() != null) //cycle to max value of left sub-tree
               {
                  parent = current;
                  current = current.getRight();
                  isRight = true;
                  onlyLeft = false;
               }
            
               hold.setValue(current.getValue());
               
               if(onlyLeft == true)
                  hold.setLeft(current.getLeft());
               else
               {
                  if(current.getLeft() == null)
                     parent.setRight(null);
                  else
                     parent.setRight(current.getLeft());
               }  
                   
               current = null;
            }  
            break;   
         }
        
         if(compare < 0) //target is less than current
         {
            parent = current;
            current = current.getLeft();
            isRight = false;
         }
         else if(compare > 0) //target is greater than current
         {
            parent = current;
            current = current.getRight();
            isRight = true;
         }
         else
         {
            if(current.getLeft() == null && current.getRight() == null) //if target node is leaf
            {
               if(isRight == false)
               {
                  parent.setLeft(null);
                  current = null;
               }
               else
               {
                  parent.setRight(null);
                  current = null;  
               } 
            }
            else if(current.getLeft() != null && current.getRight() == null) //if target node has 1 left child
            {
               if(isRight == false)
               {
                  parent.setLeft(current.getLeft());
                  current = null;
               }
               else
               {
                  parent.setRight(current.getLeft());
                  current = null;
               }
            }
            else if(current.getLeft() == null && current.getRight() != null) //if target node has 1 right child
            {
               if(isRight == false)
               {
                  parent.setLeft(current.getRight());
                  current = null;
               }
               else
               {
                  parent.setRight(current.getRight());
                  current = null;
               }
            }
            else //if node has left and right children
            {
               TreeNode hold = current;
               TreeNode holdParent = parent;
               parent = current;
               current = current.getLeft();
               isRight = false;
               boolean onlyLeft = true;
            
               while(current.getRight() != null) //cycle to max value of left sub-tree
               {
                  parent = current;
                  current = current.getRight();
                  isRight = true;
                  onlyLeft = false;
               }
               
               hold.setValue(current.getValue());
               
               if(onlyLeft == true)
                  hold.setLeft(current.getLeft());
               else
               {
                  if(current.getLeft() == null)
                     parent.setRight(null);
                  else
                     parent.setRight(current.getLeft());
               }  
                   
               current = null;
            }
         }
      }
      
      return(root); //return updated tree
   }
   
   //precondition:   the priority queue is not empty
   //postcondition: a data value of smallest priority if returned; 
   //					 the priority queue is unchanged
   public Object peekMin()
   {	
      if(root == null)
         return(root);
        
      TreeNode temp = root;
      while(temp.getLeft() != null)
         temp = temp.getLeft();
        
      return(temp.getValue());
   }
   
   public String display()
   {
      return display( root, 0 );
   }
   private String display( TreeNode t, int level )							
   {
      String toRet = "";
      if(t == null)
         return "";
      toRet += display(t.getRight(), level + 1); //recurse right
      for(int k = 0; k < level; k++)
         toRet += "\t";
      toRet += t.getValue() + "\n";
      toRet += display(t.getLeft(), level + 1); //recurse left
      return toRet;
   }
}
  
class Item
{
   private Comparable data;
   private int count;
   public Item(Comparable d)
   {  
      data = d; 
      count = 1;  
   }
   public void incrementCount()
   {	
      count++; 
   }
   //precondition:  the count of this item is greater than 0;
   public void decrementCount()
   {  
      count--;  
   }
   public int getCount()
   {	
      return count;  
   }
   public Comparable getData()
   {  
      return data;  
   }
   public String toString()
   {
      return(data + "");
   }
}