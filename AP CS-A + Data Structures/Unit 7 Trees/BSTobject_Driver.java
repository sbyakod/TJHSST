 //name:    date:  
import java.util.*;
import java.io.*;

public class BSTobject_Driver
{
   public static BSTobject<String> tree = null;
   public static BSTobject<Widget> treeOfWidgets = null;
   public static int numberWidgets = 10;
   public static void main( String[] args ) 
   {
   //day one 
      tree = new BSTobject<String>();
      tree = build(tree, "T");
      System.out.print(tree);
      System.out.println("Size: " + tree.size());
      System.out.println("Is empty: "+ tree.isEmpty());
   		
   	//day two
   	//	Your assignment the second day is to finish the BSTobject class.  
   	//	Specifically, prompt the user for a string, put the characters into a BST, 
   	//	call toString on this tree, and print the size of the tree.
   	
      
      //day two, Widgets			
   	//	Next, fill your BST with 57 Widget objects from widgets.txt.  Display the tree. 
   	//	Then prompt the user to enter pounds and ounces.  If the tree contains that 
   	//	Widget, delete it, of course restoring the BST order. Display the new tree 
   	// and its size. If the tree does not contain that Widget, print "Not found".
   
   		
      //day three -- AVL tree  -----------------------
      
   }
   // build the tree for Strings, Day 1
   public static BSTobject<String> build(BSTobject<String> tree, String str)
   {
     /* your code goes here */
         
   }
   //build the tree for Widgets, Day 2
   public static BSTobject<Widget> build(BSTobject<Widget> tree, File file)
   {
      Scanner infile = null;
      try{
         infile = new Scanner( file  );
      }
      catch (Exception e)
      {
         System.exit(0);
      }
      for(int i = 0; i < 10; i++)   
      {
      /* your code goes here */
      
      }
     
   }
}

//////////////////////////////////
interface BSTinterface<E extends Comparable<E>>
{
   public E add( E element );     //returns the object
   public boolean contains( E element );
   public boolean isEmpty();
   public E delete( E element );  //returns the object, not a Node<E>
   public int size();
   public String toString();
}
//////////////////////////////////

class BSTobject <E extends Comparable<E>> implements BSTinterface<E>
{ 
    // 2 fields 
    // 1 default constructor
      
      
   //instance methods
   public E add( E obj )
   {
      root = add( root, obj );
      size++;
      return obj;
   }
    //recursive helper method
   private Node<E> add( Node<E> t, E obj )
   {
         
   }
   /* implement the interface here.  Use TreeNode as an example,
    but root is a field. You need add, contains, isEmpty, 
    delete, size, and toString.  */



    
    /***************************private inner class **************/  
   private class Node<E>
   {
      // 3 fields 
         
      // 2 constructors, one-arg and three-arg
         
         
         
         
      //methods--Use TreeNode as an example. See the cheat sheet.
   
   }
}
