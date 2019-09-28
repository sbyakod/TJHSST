 //Name: Sharath Byakod      Period: 6     Date: 9/13/16   
import java.text.DecimalFormat;
public class SmartCard_Driver
{
   public static void main(String[] args) 
   {
      /*Station downtown = new Station("Downtown", 1);
      Station center = new Station("Center City", 1);
      Station uptown = new Station("Uptown", 2);
      Station suburbia = new Station("Suburb", 4);
     
      SmartCard jimmy = new SmartCard(20.00); //what
      jimmy.board(center);            		    //boarded in zone 1
      jimmy.disembark(suburbia);					 //disembark in zone 4
      jimmy.disembark(uptown);*/
   
      int[] s = {1, 2, 3, 4, 5};
      //System.out.println(isProcessedX(5, s));
      //lots more test cases!
   }
   public static boolean isProcessedX(int n, int[] v)
   {
      if(n >= 2 && isProcessedX(n-1, v))
      {
         v[n-1] = v[n-2];
         return true;
      }
      else
         return false;
   } 
}




































class SmartCard
{
   private double myBalance, myCost;
   private boolean ontrain = false;
   private int myStart, myEnd, myCurrent, temp;
   private String startCity, endCity; 
   public SmartCard(double balance)
   {
      myBalance = balance;
   }
    
   public void addMoney(double money)
   {
      myBalance = myBalance + money;
   }
   
   public double getBalance()
   {
      return myBalance;
   }
   
   public boolean isBoarded()
   {
      return ontrain;
   }
   
   public void board(Station start)
   {
      myStart = start.getZone();
      startCity = start.getCity();
      if(ontrain == false && myBalance >= .50)
         ontrain = true;
      else if(ontrain == false && myBalance < .50)
      {
         System.out.println("Not of enough fare to ride again! Purchase another Smartcard or add balance to your current one.");
         System.exit(0);
      }
      else
      {
         System.out.println("You are still on the subway! Please disembark before trying to board.");
         System.exit(0);
      }
   }
   
   public void cost(Station current)
   {
      temp = 0;
      myCost = 0.0;
      myCurrent = current.getZone();
      temp = myStart - myCurrent;
      temp = java.lang.Math.abs(temp);
      myCost = (.75 * temp) + .50;
      System.out.println("To disembark at your current location, a price of $" + myCost + " will be deducted from your SmartCard balance.");
   }
   
   public void disembark(Station end)
   {
      temp = 0;
      myCost = 0.0;
      myEnd = end.getZone();
      endCity = end.getCity();
      temp = myStart - myEnd;
      temp = java.lang.Math.abs(temp);
      myCost = (.75 * temp) + .50;
      myBalance = myBalance - myCost;
      
      if(myBalance < 0.0)
      {
         myBalance = myBalance + myCost;
         System.out.println("You do not have balance to pay this fare. You have $" + myBalance + " left, and this fare costs $" + myCost + ".");
         System.exit(0);
      }
      
      if(ontrain == true)
      {
         System.out.println("Your fare from " + startCity + " to " + endCity+ " is $" + myCost + ". Your current balance is $" + myBalance + ".");
         ontrain = false;
      }
      else
      {
         System.out.println("You are not currently not on a subway. Please board before trying to disembark.");
         System.exit(0);
      }     
   }
}

class Station
{
   private String myCity;
   private int myZone;

   public Station(String city, int zone)
   {
      myCity = city;
      myZone = zone;
   }
   
   public int getZone()
   {
      return myZone;
   }
   
   public String getCity()
   {
      return myCity;
   }
}

 
