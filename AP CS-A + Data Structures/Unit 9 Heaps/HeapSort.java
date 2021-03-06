//Name: Sharath Byakod     Period: 6    Date: 5/15/17

public class HeapSort
{
   public static int SIZE;  //9 or 100
	
   public static void main(String[] args)
   {
   //Part 1: Given a heap, sort it. Do this part first. 
      SIZE = 9;  
      double heap[] = {-1,99,80,85,17,30,84,2,16,1};
      display(heap);
      sort(heap);
      display(heap);
      
   //Part 2:  Generate 100 random numbers, make a heap, sort it.
   //    SIZE = 100;
   //    double[] heap = new double[SIZE + 1];
   //    heap = createRandom(heap);
   //    display(heap);
   //    makeHeap(heap, SIZE);
   //    display(heap); 
   //    sort(heap);
   //    display(heap);
   }
   
	//******* Part 1 ******************************************
   public static void display(double[] array)
   {
      for(int k = 1; k < array.length; k++)
         System.out.print(array[k] + "    ");
      System.out.println("\n");	
   }
   
   public static void sort(double[] array)
   {
      int count = array.length - 1;
   
      while(count > 1)
      {
         swap(array, count, 1);
         heapDown(array, 1, count - 1);
         count--;
      } 
   }
   
   public static void swap(double[] array, int a, int b)
   {
      double temp = array[a];
      array[a] = array[b];
      array[b] = temp;
   }
   
   public static void heapDown(double[] array, int k, int size)
   {
      int l = 2 * k;
      int r = (2 * k) + 1;
      
      if(k > size || l > size)
         return;
      else if(r > size)
      {
         if(array[k] >= array[l])
            ;
         else
            swap(array, k, l);
      }
      else
      {
         int maxChild = (array[l] > array[r]) ? l : r;
         
         if(array[k] >= array[maxChild])
            ;
         else
         {
            swap(array, k, maxChild);
            heapDown(array, maxChild, size);
         }
            
      }      
   }
   
   // ****** Part 2 *******************************************

   //Generate 100 random numbers (between 1 and 100, formatted to 2 decimal places) 
   public static double[] createRandom(double[] array)
   {  
      array[0] = -1;   //because it will become a heap
      
      int count = 1;
      int temp;
      
      while(count <= SIZE)
      {
         do
            temp = (int)(Math.random() * 9000);
            while(temp % 10 == 0);
            
         array[count] =  temp / 100.0;
         count++;
      }
      
      return(array);
   }
   
   //turn the random array into a heap
   public static void makeHeap(double[] array, int size)
   {
      int temp = size / 2;
   
      while(temp >= 1)
      {
         heapDown(array, temp, size);
         temp--;
      }
   }
}

