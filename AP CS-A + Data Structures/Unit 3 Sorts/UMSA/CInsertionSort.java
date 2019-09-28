/********************************************************	
 * File:			CInsertionSort.java					*
 * Description:		Java class for running insertion	*
 *					sort								*
 * Author:			Eric Torman (etorman@hotmail.com)	*
 * Date created:	July 20, 1999 (ET)					*
 * ******************************************************
 */
// Include utility header file (contains Java's Vector class)
import java.util.*;
 
// CInsertionSort class is derived from CSortAlgorithm class
public class CInsertionSort extends CSortAlgorithm 
{
	// Vector object for loading insertion sort code
	// NOTE: Vector object in Java is similar to 	// linked list in C++.
	private Vector code  = new Vector();
	
	/****************************************************	
	* Function:		CInsertionSort() -- Constructor		*
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
	public CInsertionSort(SortApplet parent)
	{
		// Set the main applet object
		SetApplet(parent);
		// Build debug code for insertion sort		BuildDebugCode();	}
	
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
	protected void OnSort(int a[])
	{
		// Variables of the insertion sort algorithm
		int temp, j;
		
		// Select line in debug window
		SelectLine(0);
		// Insertion sort code
		for (int i = 1; i < a.length; i++)
        {
			// Select line in debug window
			SelectLine(2);
			// Insertion sort code
          	temp = a[i];
			// Select line in debug window
			SelectLine(3);
						
			// Insertion sort code
            for (j = i, Compare(a, j, j - 1); j > 0 && (temp < a[j - 1]); j--)
            {
				// Compare a[j] with a[j-1] ONLY if we didn't				// use Compare function in the above 'for' loop.
								// NOTE: In addition to comparing two numbers,
				// Compare() function also animates comparisons 
				// process (if necessary), updates number of 
				// comparisons and updates the text box with
				// new number of comparisons (if necessary)
				
				if (i != j)
					Compare(a, j, j - 1);
				// Select line in debug window
				SelectLine(4);
				// Insertion code
				a[j] = a[j-1];
								// Insert a[j - 1] to a[j] cell -- part of insertion sort
				// algorithm.
				// Insert() function animates insertion 
				// process (if necessary), updates number of 
				// exchanges and updates the text box with
				// new number of exchanges (if necessary)
				Insert(a, j, j-1);				
            }
			// Select line in debug window
			SelectLine(5);
			// Insertion code
            a[j] = temp;			
		}
		// Once everything is sorted, change color of the cells
		// to a sorted color
		if (m_showAnimation)
			m_sortAnimator.ChangeColor(0, a.length - 1, m_sortAnimator.SORTED_COLOR); 		
	}
	
	/****************************************************	
	* Function:		BuildDebugCode()					*
	* Description:	Builds Java's vector object, which	*
	*				will be used for loading insertion	*
	*				code to debug window				*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	private void BuildDebugCode()
	{
		// Load, line by line, insertion code to 
		// our Vector (code) object		code.addElement("for (int i = 1; i < N; i++)");
		code.addElement("{");
		code.addElement("   tmp = a[i];");		code.addElement("   for (j = i; j > 0 && tmp < a[j]; j--)");		code.addElement("      a[j] = a[j - 1];"); 
		code.addElement("   a[j] = tmp;");		code.addElement("}");	
	}
	
	/****************************************************	
	* Function:		loadDebugCode()						*
	* Description:	Loads our insertion code to	debug's *
	*				window list box						*
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
