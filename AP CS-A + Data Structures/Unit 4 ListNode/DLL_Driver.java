// Name: Sharath Byakod    Period: 6   Date: 12/7/16
public class DLL_Driver
{
   public static void main(String args[])
   {
      DLL list = new DLL();	
   
      list.addLast("Apple");
      list.addLast("Banana");
      list.addLast("Cucumber");
      list.add("Durian");
      list.add("Eggplant");
      
      System.out.println("The list is " + list);
      System.out.println("Size: " + list.size());
      Object obj = list.remove(2);
      System.out.println("Remove index 2: "+ obj);
      System.out.println("The list is " + list);
      System.out.println("Size: " + list.size());
   
      list.add(2,"Carrot");
      System.out.println("Add Carrot at index 2:   " + list);
      
      try
      {
         list.add(16,"Kiwi");    //out-of-bounds
      }
      catch(IndexOutOfBoundsException e)
      {
         System.out.println(e);
      }
       
       
      System.out.println("Get values at index 0 and First: " + list.get(0)+" and " + list.getFirst());
      System.out.println("No change in list: " +list);
         
      list.removeFirst();
      System.out.println( "Remove the First:  " + list); 
       
      list.addFirst("Artichoke");
      System.out.println("Add First:  " + list);
      System.out.println("Size: " + list.size());
       
      list.set(1, "Broccoli");
      System.out.println("Set value at index 1:  " + list);
   }
}

//////////////////////////////////////////////////////////
    
class DLL        //DoubleLinkedList
{
   private int size;
   private DLNode head = new DLNode(); //dummy node--very useful--simplifies the code
   
   public int size()
   {
      return(size);
   }
   
  /* appends obj to end of list; increases size;
   	  @return true  */
   public boolean add(Object obj)
   {
      addLast(obj);
      return true;   
   }
   
   /* inserts obj at position index.  increments size. 
   	*/
   public void add(int index, Object obj) throws IndexOutOfBoundsException  //this the way the real LinkedList is coded
   {
      if(index > size || index < 0)
         throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
      else
      {
         DLNode temp = head.getNext();
         
         for(int i = index; i > 0; i--)
            temp = temp.getNext();
            
         DLNode temp2 = new DLNode(obj, temp.getPrev(), temp);
         temp.getPrev().setNext(temp2);
         temp.setPrev(temp2);
         
         size = size + 1;
      }               
   }
   
   /* return obj at position index.  
   	*/
   public Object get(int index)
   {
      DLNode temp = head.getNext();
      int i = 0;
      
      while(i < index)
      {
         temp = temp.getNext();
         i = i + 1;
      }
      
      return(temp.getValue());
   }
   
   /* replaces obj at position index.  
   		*/
   public void set(int index, Object obj)
   {
      DLNode temp = head.getNext();
      int i = 0;
      
      while(i < index)
      {
         temp = temp.getNext();
         i = i + 1;
      }
      
      temp.setValue(obj);
   }
   
   /*  removes the node from position index.  decrements size.
   	  @return the object at position index.
   	 */
   public Object remove(int index)
   {
      DLNode temp = head.getNext();
      int i = 0;
      
      while(i < index)
      {
         temp = temp.getNext();
         i = i + 1;
      }
         
      Object tempval = temp.getValue();
      temp.getNext().setPrev(temp.getPrev());
      temp.getPrev().setNext(temp.getNext());
      size = size - 1;
      
      return(tempval);
   }
   
  /* inserts obj at front of list; increases size;
     */
   public void addFirst(Object obj)
   {
      DLNode temp = new DLNode(obj, head.getPrev(), head);
      head.getNext();
      
      size =  size + 1;
   }
   
   /* appends obj to end of list; increases size;
       */
   public void addLast(Object obj)
   {
      DLNode temp = new DLNode(obj, head.getNext(), head);
      head.getPrev().setNext(temp);
      head.setPrev(temp);
      
      size =  size + 1;
   }
   
   public Object getFirst()
   {
      return(head.getNext().getValue());
   }
   
   public Object getLast()
   {
      return(head.getPrev().getValue());
   }
   
   public Object removeFirst()
   {
      return(remove(0));
   }
   
   public Object removeLast()
   {
      return(remove(size - 1));
   }
   
   public String toString()
   {
      String printer = "[";
      DLNode temp = head;
      head = head.getNext();
   
      while(head.getNext() != temp)
      {
         printer = printer + head.getValue() + ", ";
         head = head.getNext();
      }
      
      printer = printer + head.getValue();
      printer = printer + "]";
      return(printer);   
   }
}
	
//////////////////////////////////////

class DLNode 
{
   private Object value;
   private DLNode prev;
   private DLNode next;
   public DLNode(Object arg, DLNode p, DLNode n)
   {
      value=arg;
      prev=p;
      next=n;
   }
   public DLNode()
   {
      value=null;
      next=this;
      prev=this;
   }
   public void setValue(Object arg)
   {
      value=arg;
   }
   public void setNext(DLNode arg)
   {
      next=arg;
   }
   public void setPrev(DLNode arg)
   {
      prev=arg;
   }
   public DLNode getNext()
   {
      return next;
   }
   public DLNode getPrev()
   {
      return prev;
   }
   public Object getValue()
   {
      return value;
   }
}