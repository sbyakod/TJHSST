/* name: 
   date: 
	 */
public class Card_Driver_shell
{
   public static void main(String[] args)
   {
            
   }
}

 class CardDeck 
{
   private ListNode myCards;
   
   public CardDeck() 
   {
      for (int suit = Card.CLUBS; suit <= Card.SPADES; suit++)
         for (int rank = Card.ACE; rank <= Card.KING; rank++) 
         {    
            Card card = new Card(suit, rank);
            putAtEnd(card);
         }
   }  
      /*  returns the top card from the deck.
   		 reassigns a pointer to the new top card.
   		 */
   public Card getTopCard() 
   {  
   }
      /*  helper method to put a card at the end of the deck.
   	 	 */
   private void putAtEnd(Card c)
   {
   }
   public void printDeck()
   {
   }
   	
   	/*  splits this deck into two almost equal halves;
   		 chooses the split point randomly at 26 +- 10; 
   	    the first half remains in this deck in the same order;
   		 the second half is placed into a separate linked list in the same order;
   		 @return a reference to the list that refers to the second half of the deck
   		*/
   private ListNode split()
   {
   }
      
      /*  combines the cards from cards1 and cards2 into one list.
   		 takes one card from cards1, the next from cards2, the third
   		 from cards1, and so on, alternating decks;  if there are cards
   		 left over, all the rest of those cards are copied into the combined list.
   		 @return a reference to the first node of the combined list.
   		 */
   private ListNode combine(ListNode cards1, ListNode cards2)
   {
   }
      
      
      /*  splits the deck, then combines the 2 halves;
   	    this operation is repeated numTimes number of times.
   		*/
   public void shuffle(int numTimes)
   {
   }
}

class Card 
{
   public static final int CLUBS  = 0;     //for playing Bridge 
   public static final int DIAMONDS = 1;
   public static final int HEARTS = 2;
   public static final int SPADES = 3;
    
   public static final int ACE = 1;		   //Aces are always low
   public static final int JACK = 11;
   public static final int QUEEN = 12;
   public static final int KING = 13;
      
   private int rank;
   private int suit;
      
   private String[] rankList = {"","Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"};
   private String[] suitList = {"Clubs","Diamonds","Hearts","Spades"};
     
   public Card(int s, int r) {
      if ((ACE <= r) && (r <= KING))
         this.rank = r;
      else
         throw new RuntimeException
                ("Invalid rank in Card constructor: " + rank);
        
      if ((CLUBS <= s) && (s <= SPADES))
         this.suit = s;
      else
         throw new RuntimeException
                ("Invalid suit in Card constructor: " + suit);
   }
   
   public int getRank() 
   { 
      return rank; 
   }
    
   public int getSuit() 
   { 
      return suit; 
   }
    
   public String getRankAsString() 
   { 
      return rankList[rank]; 
   }
    
   public String getSuitAsString() 
   { 
      return suitList[suit]; 
   }
         
   public String toString()
   {
      return ( getRankAsString()+" of "+getSuitAsString() );
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