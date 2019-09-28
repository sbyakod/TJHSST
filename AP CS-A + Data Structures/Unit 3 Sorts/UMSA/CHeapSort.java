/********************************************************	
 * File:			CHeapSort.java						*
 * Description:		Java class for running heap			*
 *					sort								*
 * Author:			Eric Torman (etorman@hotmail.com)	*
 * Date created:	July 20, 1999 (ET)					*
 * ******************************************************
 */

// Include utility header file (contains Java's Vector class)
import java.util.*;
 
// CHeapSort class is derived from CSortAlgorithm class
class CHeapSort extends CSortAlgorithm {	// Vector object for loading heap sort code		private Vector code     = new Vector();
	
	/****************************************************	
	* Function:		CHeapSort() -- Constructor			*
	* Description:	Simple constructor function.		*
	*				Initializes variables of this and	*
	*				derived (CSortAlgorithm) classes.	*
	*													*
	* Input:		Sorting applet object				*
	*				(SortApplet parent)					*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	Note that in Java there is no		*
	*				destructor. You can override		*
	*				protected void finalize() function,	*
	*				and it'll get called by Java's		*
	*				garbage	collector					*	
	* ***************************************************
	*/
	public CHeapSort(SortApplet parent)
	{		// Set the main applet object
		SetApplet(parent);
		// Build code for heap sort		BuildDebugCode();	}
		/****************************************************	
	* Function:		Perc_Down()							*
	* Description:	Function to build a heap from an	*
	*				array								*
	* 													*
	* Input:		Array to sort (int arr[])			*
	*				From where cell to start sorting	*
	*				(int i)								*
	*				Where to end sorting (int N)		*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE -- See any Data Structures		*
	*				book regarding Perc_Down function	*
	*				of heap sort						*
	*****************************************************
	*/
	private void Perc_Down(int a[], int i, int N)	{
		// Local variables		int j, k;
		
		// Select line from the debug window
		SelectLine(8); 							// Perc_Down code
		for(j = i, k = 2*j; k <= N; j= k, k = 2*j) 
		{
			// Select line from the debug window
			SelectLine(9); 						// Perc_Down code			// Compare a[k-1] with a[k].
			// NOTE: In addition to comparing two numbers,
			// Compare() function also animates comparision 
			// process (if necessary), updates number of 
			// comparisions and updates the text box with
			// new number of comparisions (if necessary)
			if (k < N && Compare(a, k-1, k) == FIRST_IS_SMALLER)
			{	// same as if (k < N && (a[k - 1] < a[k]))
				// Select line from the debug window
				SelectLine(10);				// Perc_Down code
				k++;
			}
			// Select line from the debug window
			SelectLine(11); 			
			// Perc_Down code			// Compare a[j-1] with a[k-1].
			// NOTE: In addition to comparing two numbers,
			// Compare() function also animates comparision 
			// process (if necessary), updates number of 
			// comparisions and updates the text box with
			// new number of comparisions (if necessary)
			if (Compare(a, j-1, k-1) == FIRST_IS_SMALLER)
			{	// same as if (a[j-1] < a[k-1])
				// Select line from the debug window
				SelectLine(12); 			
				// Perc_Down code				// NOTE: Swap() function also animates the 				// swapping process				Swap(a, j - 1, k - 1, true);
			}
			else
			{
				// Select line from the debug window
				SelectLine(13); 			
				// Select line from the debug window
				SelectLine(14); 			
				break;
			}
		}
	}
    	/****************************************************	
	* Function:		OnSort()							*
	* Description:	Function responsible for running	*
	*				actual heap sort algorithm			*
	* 													*
	* Input:		Array of numbers to sort			*
	*				(int arr[])							*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	Replaces the unsorted array by		*
	*				sorted array						*
	* ***************************************************
	*/
	protected void OnSort(int a[])	{
		// Length of the array 		int N = a.length;
		
		// Select line from the debug window				
		SelectLine(0); 
		// Heap sort code
		for (int i = N / 2; i > 0; i--) 		{			// Select line from debug window				
			SelectLine(1); 						// Heap sort code
			Perc_Down(a, i, N);		}				
		// Select line from debug window				
		SelectLine(2);		// Heap sort code
		for (int i = N; i > 1; i--)		{
			// Select line from the debug window
			SelectLine(3); 						
			// Heap sort code			// NOTE: Swap() function also animates the 			// swapping process
			Swap(a, i - 1, 0, true);

			// Select line from the debug window
			SelectLine(4); 						// Heap sort code
			Perc_Down(a, 1, i - 1);
			// Set the colors of the cell so that they are sorted			if (m_showAnimation)
				m_sortAnimator.ChangeColor(i - 1, i - 1, m_sortAnimator.SORTED_COLOR);  
		}		// Finally, set the color of the first so it's sorted		if (m_showAnimation)			m_sortAnimator.ChangeColor(0, 0, m_sortAnimator.SORTED_COLOR);
    }			
	/****************************************************	
	* Function:		BuildDebugCode()					*
	* Description:	Builds Java's vector object, which	*
	*				will be used for loading heap sort	*
	*				code to debug window				*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	private void BuildDebugCode()
	{		// Load, line by line, heap sort code to 
		// our Vector (code) object		code.addElement("for (int i = N / 2; i >= 0; i--)");
		code.addElement("   Perc_Down(a, i, N);");		code.addElement("for (int i = N; i >= 2; i--) {");
		code.addElement("   Swap( a[1], a[i]);"); 
		code.addElement("   Perc_Down(a, 1, i - 1);");		code.addElement("}");
		code.addElement("void Perc_Down(int a[], int i, int N)");
		code.addElement("{");		code.addElement("   for(j=i, k=2*j; k<=N; j=k, k=2*j) {"); 
		code.addElement("      if (k < N && a[k-1] < a[k])");
		code.addElement("         k++;");
		code.addElement("      if (a[j-1] < a[k-1])");
		code.addElement("         Swap(a[j - 1], a[k - 1]);");
		code.addElement("      else");
		code.addElement("         break;");
		code.addElement("   }");
		code.addElement("}");		
	}
		
	/****************************************************	
	* Function:		loadDebugCode()						*
	* Description:	Loads our main part of heap sort	*
	*				code to	debug's window list box		*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	public void loadDebugCode()
	{
		// Clear debug's window list box
		m_debugWindow.ClearList();		
		// Add a string to the debug's window list box
		for (int i = 0; i < code.size(); i++)
			m_debugWindow.AddLine((String)(code.elementAt(i))); 
	}
}
