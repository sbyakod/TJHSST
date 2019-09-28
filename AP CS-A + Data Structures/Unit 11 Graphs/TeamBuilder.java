//Name: Sharath Byakod     Period: 6    Date: 6/20/17

public class TeamBuilder
{
   public static void main(String[] args) 
   {
      /*String[] path = {"010", "000", "110"};	   
      //String[] path = {"0010", "1000", "1100", "1000"};
      //String[] path = {"01000", "00100", "00010", "00001", "10000"};
      //String[] path = {"0110000", "1000100", "0000001", "0010000", "0110000", "1000010", "0001000"};
        
      int[] ret = specialLocations(path);
         
      System.out.println("{" + ret[0] + ", " + ret[1] + "}");*/
      
      Queue<Comparable> temp = new Queue<Comparable>();
      temp.add("A");
   }
   
   public TreeNode queueToTree( Queue<Comparable> q )
   {
      if( q.isEmpty() )
         return null;
      Queue<Comparable> q1 = new LinkedList<Comparable>();
      Queue<Comparable> q2 = new LinkedList<Comparable>();
      Comparable x, y;
      x = q.remove();
      while( !q.isEmpty() )
      {
         y = q.remove();
         if( y.compareTo(x) < 0 )
            q1.add( y );
         else
            q2.add( y );
      }
      return new TreeNode( x, queueToTree(q1), queueToTree(q2) );
   }
   
   public static int[] specialLocations(String[] paths)
   {
      final int size = paths.length;
      int[][] ar = new int[size][size];
      int z = 0;
      
      while(z < size)
      {
         for(int j = 0; j < size; j++)
         {
            ar[z][j] = paths[z].charAt(j) - '0';
         }
         
         z++;
      }
      
      int x = 0;
      int y = 0;
      
      while(x < size)
      {
         for(int i = 0; i < size; i++)
         {
            while(y < size)
            {
               if(ar[i][y] == 0 && ar[i][x] == 1 && ar[x][y] == 1)
                  ar[i][y] = 1;
                  
               y++;
            }
            
            y = 0;
         }
         
         y = 0;
         x++;
      }
      
      int toRet1 = 0;
      int toRet2 = 0;
      int v = 0;
      
      while(v < size)
      {
         boolean bool1 = true;
         boolean bool2 = true;
         
         for(int j = 0; j < size; j++)
         {
            if(v == j)
               continue;
            else
               ;   
               
            if(ar[v][j] != 0)
               ;
            else
               bool1 = false;
               
            if(ar[j][v] != 0)
               ;
            else
               bool2 = false;
         }
         
         if(bool1 != false)
            toRet1++;
         else
            ;
            
         if(bool2 != false)
            toRet2++;
         else
            ;
            
         v++;   
      }
      
      int[] toRetar = {toRet1, toRet2};
      
      return(toRetar);
   }
}