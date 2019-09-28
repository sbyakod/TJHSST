
/********************************************************	
 * File:			CShellSort.java						*
 * Description:		Java class for running shell sort	*
 * Author:			Eric Torman (etorman@hotmail.com)	*
 * Date created:	July 20, 1999 (ET)					*
 * ******************************************************
 */

// Include utility header file (contains Java's Vector class)
import java.util.*;
 
// CShellSort class is derived from CSortAlgorithm class
class CShellSort extends CSortAlgorithm {	// Vector object for loading shell sort		private Vector code = new Vector();
		/****************************************************	
	* Function:		CShellSort() -- Constructor			*
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
	public CShellSort(SortApplet parent)
	{		// Set the main applet object
		SetApplet(parent);
		// Build shell debug code		BuildCode();	}
	    
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
	protected void OnSort(int a[])	{
		// Local variables of shell sort algorithm		int j, temp; 
		
		// Length of the array
		int N = a.length; 

		// Select line from debug window
		SelectLine(0);
		// Outer for loop statement
		for (int inc = N / 2; inc > 0; inc /= 2)  
		{
			// Select line from debug window
			SelectLine(2);
			for (int i = inc; i < N; i++) 
			{
				// Select line from debug window
				SelectLine(4);
				temp = a[i];
				// Select line from debug window
				SelectLine(5);
				// Shell sort code
				j = i;
				// Select line from debug window
				SelectLine(6);
	            for (Compare(a, j, j - inc); j >= inc && (temp < a[j - inc]); j -= inc)
				{
					// Compare a[j] with a[j-inc] ONLY if we didn't					// use Compare function in the above 'for' loop.
									// NOTE: In addition to comparing two numbers,
					// Compare() function also animates comparisons 
					// process (if necessary), updates number of 
					// comparisons and updates the text box with
					// new number of comparisons (if necessary)					if (i != j)
						Compare(a, j, j - inc);
					// Select line from debug window
					SelectLine(8);
					// Shell sort code
					a[j] = a[j-inc]; 
					// Animate swapping a[j] and a[j-inc] BUT 
					// don't actually swap the items in the array.
					// This appears to be the only way to show
					// animation for shell sort!
					Swap(a, j, j-inc, false); 
					// Select line from debug window
					SelectLine(9);
				}
				// Select line from debug window
				SelectLine(11);
				// Shell sort code
				a[j] = temp;
			}
		}
		// Color sorted cells		if (m_showAnimation)
			m_sortAnimator.ChangeColor(0, N - 1, m_sortAnimator.SORTED_COLOR); 		
	}				
	/****************************************************	
	* Function:		BuildCode()							*
	* Description:	Builds Java's vector object, which	*
	*				will be used for loading shell sort	*
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
		// Load, line by line, shell sort code to 
		// our Vector (code) object		code.addElement("for (int inc=N/2; inc>0; inc/=2)");
		code.addElement("{");		code.addElement("   for (int i = inc; i < N; i++)");		code.addElement("   {");		code.addElement("      tmp = a[i];");
		code.addElement("      j = i;");				code.addElement("      while(j>=inc && tmp<a[j-inc])");
		code.addElement("      {");				code.addElement("         a[j] = a[j - inc];");
		code.addElement("         j -= inc;");
		code.addElement("      }");				code.addElement("      a[j] = tmp;"); 
		code.addElement("   }");
		code.addElement("}");
	}
	
	/****************************************************	
	* Function:		loadDebugCode()						*
	* Description:	Loads our shell sort code to		*
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
		//m_debugWin
		// Clear debug's window list box
		m_debugWindow.ClearList();		
		// Add a string to the debug's window list box
		for (int i = 0; i < code.size(); i++)
			m_debugWindow.AddLine((String)(code.elementAt(i))); 
	}
}