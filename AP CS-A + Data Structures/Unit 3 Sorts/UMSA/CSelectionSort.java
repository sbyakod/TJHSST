/********************************************************	
 * File:			CSelectionSort.java					*
 * Description:		Java class for running selection	*
 *					sort								*
 * Author:			Eric Torman (etorman@hotmail.com)	*
 * Date created:	July 20, 1999 (ET)					*
 * ******************************************************
 */

// Include utility header file (contains Java's Vector class)import java.util.*;

// CSelectionSort class is derived from CSortAlgorithm class
public class CSelectionSort extends CSortAlgorithm
{
	// Vector object for loading selection sort code
	// NOTE: Vector object in Java is similar to 	// linked list in C++.
	private Vector code  = new Vector();
	
	/****************************************************	
	* Function:		CSelectionSort() -- Constructor		*
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
	public CSelectionSort(SortApplet parent)
	{
		// Set the main applet object
		SetApplet(parent);
		// Build debug code for selection sort		BuildDebugCode();	}	
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
		// Cell index - part of selection sort code
		int min;
 
		// Select line of debug window		SelectLine(0);
		// Part of selection sort code
		for (int i = 0; i < a.length; i++)
		{
			// Select line of debug window			SelectLine(2); 			
			// Set minimum cell index
			min = i;
				
			// Select line of debug window			SelectLine(3); 			
			// Part of selection sort code
			for (int j = i+1; j < a.length; j++)
			{
				// Select line of debug window				SelectLine(4); 			
				// Compare a[j] with a[min] -- part of selection				// sort algorithm.
				// NOTE: In addition to comparing two numbers,
				// Compare() function also animates comparison 
				// process (if necessary), updates number of 
				// comparisons and updates the text box with
				// new number of comparisons (if necessary)

				if (Compare(a, j, min) == FIRST_IS_SMALLER)
				{	// Same as if (a[j] < a[min])
	
					// Select line of debug window					SelectLine(5);
					// Set minimum index
					min = j;
				}
				// Select line of debug window				SelectLine(3);
			}
			// Select line of debug window
			SelectLine(6); 			

			// Swap a[i] with a[min] -- part of selection sort
			// algorithm.
			// NOTE: In addition to swapping two numbers,
			// Swap() function also animates swapping 
			// process (if necessary), updates number of 
			// exchanges and updates the text box with
			// new number of exchanges (if necessary)
			Swap(a, i, min, true);

			// Change the color of the cell a[i] so it looks like			// it's sorted	
			if (m_showAnimation)
				m_sortAnimator.ChangeColor(i, i, m_sortAnimator.SORTED_COLOR);  
		}
	}
	
	/****************************************************	
	* Function:		BuildDebugCode()					*
	* Description:	Builds Java's vector object, which	*
	*				will be used for loading selection	*
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
		// Load, line by line,selection code to 
		// our Vector (code) object		code.addElement("for (int i = 0; i < N; i++)");
		code.addElement("{");
		code.addElement("   min = i;");
		code.addElement("   for (int j = i + 1; j < N; j++)"); 		code.addElement("      if (a[j] < a[min])"); 
		code.addElement("         min = j");
		code.addElement("   Swap(a[i], a[min]);");		code.addElement("}");	
	}
	
	/****************************************************	
	* Function:		loadDebugCode()						*
	* Description:	Loads our selection code to	debug's *
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
