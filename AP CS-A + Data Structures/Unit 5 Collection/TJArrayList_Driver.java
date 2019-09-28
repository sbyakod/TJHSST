//  name:        date: 
//  implements the List interface with a backing array of Objects. 
//	 also overrides toString().
    
public class TJArrayList_Driver
{  
   public static void main(String [] args)
   {
      TJArrayList myList = new TJArrayList();	
   
      myList.add("Apple");
      myList.add("Banana");
      myList.add("Fig");
      myList.add(2, "Cucumber");
      myList.add(3, "Dates");
      System.out.println(myList);
      System.out.println("Size is " + myList.size());
      try
      {
         myList.add(12, "Peach");
      }
      catch(IndexOutOfBoundsException e)
      {
         System.out.println(e);
      }
      System.out.println("Get 2: " + myList.get(2));
      System.out.print("Set at 2: ");
      myList.set(2, "Cherry");
      System.out.println(myList);
      Object obj = myList.remove(2);
      System.out.println("Removed " + obj+ " from " + myList);
      System.out.println("Size is " + myList.size());
      System.out.print("Add too many items: ");
      for(int i = 3; i <= 10; i++)
         myList.add(new Integer(i));
      System.out.println(myList);
      System.out.println("Size is " + myList.size());   	
      System.out.println("Contains \"Breadfruit\"?  " + myList.contains("Breadfruit"));
      System.out.println("Contains \"Banana\"?  " + myList.contains("Banana"));
   }
}
   
class TJArrayList
{
   private int size;							//stores the number of objects
   private Object[] myArray;
   
   public TJArrayList()                //default constructor makes 10 cells
   {
      myArray = new Object[10];
      size = 0;
   }
   
   public int size()
   {
      return(size);
   }
 	/* appends obj to end of list; increases size;
         must be an O(1) operation when size < array.length, 
            and O(n) when it doubles the length of the array.
	      @return true  */
   public boolean add(Object obj)
   {
      size++;
      
      if(size >= myArray.length)
      {
         Object[] temp = new Object[myArray.length * 2];
         for(int i = 0; i < myArray.length; i++)
            temp[i] = myArray[i];
         temp[myArray.length] = obj;
      }
      else
         myArray[size - 1] = obj;
         
      return(true);     
   }
      /* inserts obj at position index.  increments size. 
   		*/
   public void add(int index, Object obj) throws IndexOutOfBoundsException  //this the way the real ArrayList is coded
   {
      if(index > size || index < 0)
         throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
      
      
      
   }
      /* return obj at position index.  
   		*/
   public Object get(int index)
   {
      return(myArray[index]);  
   }
    /* replaces obj at position index.  
   		*/
   public void set(int index, Object obj)
   {
      myArray[index] = obj;
   }
    /*  removes the node from position index. shifts elements 
        to the left.   Decrements size.
   	  @return the object at position index.
   	  */
   public Object remove(int index)
   {
      Object temp = null;
   /*if(index = 0)
      for(int i = 0; i < size)
   else
      
   for(int i = 0; i < index; i++)
   */
      
      
   }
	 /*
      this method compares objects and should use .equals(), not ==
     	*/
   public boolean contains(Object obj)
   {
      boolean flag = false;
   
      for(int i = 0; i < size; i++)
         if(obj.equals(myArray[i]))
         {
            flag = true;
            break;
         }  
      
      return(flag); 
   }
      /*returns a String of Objects in the array with square brackets and commas
        	*/
   public String toString()
   {
      String printer = "[";
      if(size > 0)
      {
         for(int i = 0; i < size - 1; i++)
            printer = printer + myArray[i] + ", ";
         printer = printer + myArray[size - 1] + "]";
      }
      else
         printer = printer + "]";
   
      return(printer);  
   }
}