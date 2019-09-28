/********************************************************	
 * File:			CQuickSort.java						*
 * Description:		Java class for running quick sort	*
 * Author:			Eric Torman (etorman@hotmail.com)	*
 * Date created:	July 20, 1999 (ET)					*
 * ******************************************************
 */

// Include utility header file (contains Java's Vector class)
import java.util.*;
 
// CQuickSort class is derived from CSortAlgorithm class
class CQuickSort extends CSortAlgorithm {	// Vector object for loading shell sort		private Vector code = new Vector();
		/****************************************************	
	* Function:		CQuickSort() -- Constructor			*
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
	public CQuickSort(SortApplet parent)
	{		// Set the main applet object
		SetApplet(parent);
		// Build quick sort code		BuildCode();	}
	    
	/****************************************************	
	* Function:		OnSort()							*
	* Description:	Function responsible for running	*
	*				actual sorting algorithm			*
	* 													*
	* Input:		Array of numbers to sort			*
	*				(int arr[])							*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	Replaces the unsorted array by		*
	*				sorted array						*
	* ***************************************************
	*/
	protected void OnSort(int a[])	{		QuickSort(a, 0, a.length - 1);
		if (m_showAnimation)
			m_sortAnimator.ChangeColor(0, a.length - 1, m_sortAnimator.SORTED_COLOR);  	}					/****************************************************	
	* Function:		QuickSortSort()						*
	* Description:	Function that actually performs the *
	*				quick sort							*
	* 													*
	* Input:		Array of numbers to sort			*
	*				(int arr[])							*
	*				Left index  (int lo0)				*
	*				Right index (int ho0)				*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	The function is recursive			*
	*				See any Data Structures book for	*
	*				explanation of QuickSort algorithm	*
	*				NOTE: This implementation of quick	*
	*				sort uses middle point as pivot.	*
	*****************************************************
	*/
	private void QuickSort(int a[], int lo0, int hi0)
	{
		// Variables of quick sort		int lo = lo0;
		int hi = hi0;
		int mid;
	
		// Select line from the debug window
		SelectLine(3);
		// Quick sort code
		if (lo0 >= hi0) 			return;				// Select line from the debug window
		SelectLine(4);		
		// Establish pivot in the middle		mid = a[ ( lo0 + hi0 ) / 2 ];

		// Select line from the debug window		SelectLine(5);
				// loop through the array until indices cross
		while( lo <= hi ) 		{
			// Select line from the debug window			SelectLine(6);
						// find the first element that is greater than or equal to 
			// the partition element starting from the left Index.
			while( a[lo] < mid ) 
			{				// Select '++lo' line				SelectLine(7);
				lo++;			}

			// Select 'while (a[hi] > mid)' line
			SelectLine(8);
			while( a[hi] > mid ) 
			{
				// Select '--hi' line				SelectLine(9);				hi--;			}

			// Select 'if (lo <= hi)' line			SelectLine(10);

			// Compare a[lo] with a[hi] 
							// NOTE: In addition to comparing two numbers,
			// Compare() function also animates comparisons 
			// process (if necessary), updates number of 
			// comparisons and updates the text box with
			// new number of comparisons (if necessary)			
			Compare(a, lo, hi);
			if( lo <= hi ) {
				// Select 'Swap(a[lo], a[hi])' line				SelectLine(11);
				// Finally, swap
				Swap(a, lo, hi, true);
				// Select '++lo' line				SelectLine(12);				++lo; 				// Select '--hi' line				SelectLine(12);				--hi;
			}
		}

		// Select 'QuickSort(a, lo0, hi)' line		SelectLine(15);				// Sort left partition
		QuickSort( a, lo0, hi );
		// Change color of cells to sorted		if (m_showAnimation)
			m_sortAnimator.ChangeColor(lo0, hi, m_sortAnimator.SORTED_COLOR);  
		// Select 'QuickSort(a, lo, hi0)' line		SelectLine(16);
				// Sort right partition
		QuickSort( a, lo, hi0 );		// Change color of cells to sorted
		if (m_showAnimation)
			m_sortAnimator.ChangeColor(lo, hi0, m_sortAnimator.SORTED_COLOR);  	}
		
	/****************************************************	
	* Function:		BuildCode()							*
	* Description:	Builds Java's vector object, which	*
	*				will be used for loading quick sort	*
	* 				to debug window						*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	private void BuildCode()
	{
		// Load, line by line, quick sort code to 
		// our Vector (code) object		code.addElement("void QuickSort(int a[], int lo0, int hi0)");
		code.addElement("{");
		code.addElement("   int lo = lo0, hi = hi0;");
		code.addElement("   if ( lo0 >= hi0) return;");		code.addElement("   int mid = a[lo0 + hi0) / 2];");		code.addElement("   while(lo <= hi) {");		code.addElement("      while(a[lo] < mid)");		code.addElement("      lo++;");		code.addElement("      while(a[hi] > mid)");		code.addElement("      hi--;");		code.addElement("      if (lo <= hi) {");		code.addElement("         Swap(a[lo], a[hi])");
        code.addElement("         lo++; hi--;");
		code.addElement("      }");		code.addElement("   }");			
        code.addElement("   QuickSort(a, lo0, hi);");
        code.addElement("   QuickSort(a, lo, hi0);");
		code.addElement("}");			
	}
	
	/****************************************************	
	* Function:		loadDebugCode()						*
	* Description:	Loads our quick sort code to		*
	*				debug's window list box				*
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
	}	}
