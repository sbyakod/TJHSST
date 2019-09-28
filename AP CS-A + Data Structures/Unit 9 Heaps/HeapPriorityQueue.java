//Name: Sharath Byakod     Period: 6    Date: 5/22/17
 
 //implement the API for java.util.PriorityQueue
 //test this class by using it in McRonaldPQ_working.java.
 //add(E) and remove()  must work in O(log n) time
 
import java.util.*;

public class HeapPriorityQueue<E extends Comparable<E>> 
{
   private ArrayList<E> myHeap;
   private int size;
   
   public HeapPriorityQueue()
   {
      myHeap= new ArrayList<E>();
      myHeap.add(null);
      size = myHeap.size()-1;
   }
   
   public boolean add(E obj)
   {
      myHeap.add(obj);
      size++;
      heapUp(myHeap);
      
      return(true);
   }
   
   public E remove()
   {
      swap(myHeap,1,size);
      E temp = myHeap.remove(size);
      size--;
      heapDown(myHeap,1);
      
      return(temp);
   }
   
   public E peek()
   {
      if(this.isEmpty())
         return(null);
   
      return(myHeap.get(1));
   }
   
   public boolean isEmpty()
   {
      if(size == 0)
         return(true);
    
      return(false);
   }
   
   public void swap(ArrayList<E> array, int a, int b)
   {
      E temp = array.get(b);
      array.set(b, array.get(a));
      array.set(a,temp);
   } 
   
   public void heapUp(ArrayList<E> array)
   {
      int k = size;
   
      while(k / 2 >= 1)
      {
         if(array.get(k / 2).compareTo(array.get(k)) > 0) //case statement
         {
            swap(array, k, k / 2);
            k = k / 2;
         }
         else
            break;   
      }
   }
   
   public void heapDown(ArrayList<E> array, int k)
   {
      if(k * 2 > size)
         return;
      else if(k * 2 == size)
      {
         if(array.get(k).compareTo(array.get(k * 2)) <= 0)
            /*int troll = 45*/;
         else
         {
            swap(array, k, k * 2);
            heapDown(array, 2 * k);
         }
      }
      else if(array.get(k).compareTo(array.get(2*k))<=0 && array.get(k).compareTo(array.get((2*k)+1)) <= 0)
         return;
      else if(array.get(k).compareTo(array.get(2 * k)) > 0 && array.get(k).compareTo(array.get(2 * k + 1)) > 0)
      {
         if(array.get(2 * k).compareTo(array.get(2 * k + 1)) > 0)
         {
            swap(array, k, 2 * k + 1);
            heapDown(array, 2 * k + 1);
         }
         else
         {
            swap(array, k, k * 2);
            heapDown(array, 2 * k);
         }
      }
      else if(array.get(k).compareTo(array.get(2 * k)) > 0)
      {
         boolean temp = true;
      
         if(temp == true)
         {
            swap(array, k, k * 2);
            heapDown(array, 2 * k);
         }
         else
            ;
      }
      else if (array.get(k).compareTo(array.get(2 * k + 1)) > 0)
      {
         boolean temp = true;
      
         if(temp == true)
         {
            swap(array, k, 2 * k + 1);
            heapDown(array, 2 * k + 1);
         }
         else
            ;
      }
      else
         ;
   }
   
   public String toString()
   {
      String temp = "";
      
      for(int i = 1; i < myHeap.size(); i++)
         temp = temp + (myHeap.get(i) +  ", ");
         
      if(temp.length() > 2)
         temp = temp.substring(0, temp.length() - 2);
         
      temp += "]";
      
      return(temp);	
   }
}