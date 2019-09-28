/********************************************************	
 * File:			CBubbleSort.java					*
 * Description:		Java class for running two versions	*
 *					of bubble sort: with flag and		* 
 *					without flag						*
 * Author:			Eric Torman (etorman@hotmail.com)	*
 * Date created:	July 20, 1999 (ET)					*
 * ******************************************************
 */

// Include utility header file (contains Java's Vector class)import java.util.*; 
// CBubbleSort class is derived from CSortAlgorithm class
class CBubbleSort extends CSortAlgorithm {	
	// Flag for determining whether we are running
	// normal bubble sort (w/o flag) or bubble sort
	// with flag	public boolean bBubble_w_Flag = false;
	// Two Vector objects for loading bubble sort w/flag code	// and bubble sort w/o flag code.	// NOTE: Vector object in Java is similar to 	// linked list in C++.
	private Vector code_wo_flag = new Vector();
	private Vector code_w_flag  = new Vector();
			/****************************************************	
	* Function:		CBubbleSort() -- Constructor		*
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
	public CBubbleSort(SortApplet parent)
	{
		// Set the main applet object		SetApplet(parent);		// Build debug code for bubble sort w/o flag		BuildDebugCode_wo_flag();		// Build debug code for bubble sort with flag		BuildDebugCode_w_flag();
	}		/****************************************************	
	* Function:		RunBubbleSort_w_Flag()				*
	* Description:	Runs bubble sort w/flag algorithm	*
	*													*
	* Input:		Array of numbers to sort			*
	*				(int arr[])							*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	The unsorted array will be replaced	*
	*				by sorted array						*
	* ***************************************************
	*/
	private void RunBubbleSort_w_Flag(int a[])	{		// Select line of debug window
		SelectLine(0);
		// Actual bubble sort wo/flag code
		for (int i = a.length; --i >= 0; ) 		{			// Select line of debug window			SelectLine(2);
			// Actual bubble sort wo/flag code		
			boolean	swapped = false;						// Select line of debug window			SelectLine(3);  
		
			// Actual bubble sort wo/flag code		
			for (int j = 0; j < i; j++) 			{
				// Select line of debug window				SelectLine(5);  
												
				// Compare a[j] with a[j + 1] -- part of bubble sort
				// w/flag algorithm.
				// NOTE: In addition to comparing two numbers,
				// Compare() function also animates comparision 
				// process (if necessary), updates number of 
				// comparisions and updates the text box with
				// new number of comparisions (if necessary)
				if (Compare(a, j, j + 1) == FIRST_IS_LARGER)				{   // Same as if (a[j] > a[j + 1])

					// Select line of debug window					SelectLine(7);  
						
					// Swap a[j] with a[j + 1] -- part of bubble sort
					// w/flag algorithm.
					// NOTE: In addition to swapping two numbers,
					// Swap() function also animates swapping 
					// process (if necessary), updates number of 
					// exchanges and updates the text box with
					// new number of exchanges (if necessary)
					Swap(a, j, j + 1, true);						
					// Select of debug window					SelectLine(8);  
					swapped = true;				}
			}
						// Change the color of the cell a[i] so it looks like			// it's sorted
			if (m_showAnimation)
				m_sortAnimator.ChangeColor(i, i, m_sortAnimator.SORTED_COLOR); 
			// Select line of debug window			SelectLine(11);  
		
			// Actual bubble sort wo/flag code		
			if (!swapped)			{
				// Cells a[0] to a[i] are already sorted
				// So, change the color of these cells to sorted color				if (m_showAnimation)
					m_sortAnimator.ChangeColor(0, i, m_sortAnimator.SORTED_COLOR); 				// Select line of debug window				SelectLine(12);  					return;
			}		}
	}
	/****************************************************	
	* Function:		RunBubbleSort_wo_Flag()				*
	* Description:	Runs bubble sort wo/flag algorithm	*
	*													*
	* Input:		Array of numbers to sort			*
	*				(int arr[])							*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	The unsorted array will be replaced	*
	*				by sorted array						*
	* ***************************************************
	*/
	private void RunBubbleSort_wo_Flag(int a[])	{			// Select line of debug window
		SelectLine(0);
		// Actual bubble sort wo/flag code		for (int i = a.length; --i >= 0; ) 		{
			// Select line of debug window			SelectLine(2);  			// Actual bubble sort wo/flag code		
			for (int j = 0; j < i; j++) 			{
				// Select line of debug window				SelectLine(3);  
				
				// Compare a[j] with a[j + 1] -- part of bubble sort
				// wo/flag algorithm.
				// NOTE: In addition to comparing two numbers,
				// Compare() function also animates comparision 
				// process (if necessary), updates number of 
				// comparisions and updates the text box with
				// new number of comparisions (if necessary)

				if (Compare(a, j, j + 1) == FIRST_IS_LARGER)				{	// Same as if (a[j] > a[j + 1])
		
					// Select line of debug window					SelectLine(4);  
										// Swap a[j] with a[j + 1] -- part of bubble sort
					// wo/flag algorithm.
					// NOTE: In addition to swapping two numbers,
					// Swap() function also animates swapping 
					// process (if necessary), updates number of 
					// exchanges and updates the text box with
					// new number of exchanges (if necessary)
					Swap(a, j, j + 1, true);						
				}			}			// Change the color of the cell a[i] so it looks like			// it's sorted
			if (m_showAnimation)
				m_sortAnimator.ChangeColor(i, i, m_sortAnimator.SORTED_COLOR); 		}	}	
	/****************************************************	
	* Function:		OnSort()							*
	* Description:	Function responsible for running	*
	*				actual algorithms					*
	* 													*
	* Input:		Array of numbers to sort			*
	*				(int arr[])							*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	Calls one of the private functions	*
	*				to sort the array					*
	* ***************************************************
	*/
	protected void OnSort(int a[])	{
		// If flag is set, run bubble w/flag algorithm		if (bBubble_w_Flag)			RunBubbleSort_w_Flag(a);		else
		// Otherwise, run bubble wo/flag algorithm			RunBubbleSort_wo_Flag(a);
	}	
	/****************************************************	
	* Function:		BuildDebugCode_w_flag()				*
	* Description:	Builds Java's vector object, which	*
	*				will be used for loading bubble		*
	*				w/flag code to debug window			*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	private void BuildDebugCode_w_flag()	{
		// Load, line by line, bubble w/flag code to 
		// our Vector (code_w_flag) object		code_w_flag.addElement("for (int i = N; --i >= 0)");
		code_w_flag.addElement("{");
		code_w_flag.addElement("   boolean swapped = false;");
		code_w_flag.addElement("   for (int j = 0; j < i; j++)"); 		code_w_flag.addElement("   {");		code_w_flag.addElement("      if (a[j] > a[j+1])"); 
		code_w_flag.addElement("      {");
		code_w_flag.addElement("         Swap(a[j], a[j + 1]);");		code_w_flag.addElement("         swapped = true;");		code_w_flag.addElement("      }");
		code_w_flag.addElement("   }");
		code_w_flag.addElement("   if (!swapped)");		code_w_flag.addElement("      return;");
		code_w_flag.addElement("}");
	}	
	/****************************************************	
	* Function:		BuildDebugCode_wo_flag()			*
	* Description:	Builds Java's vector object, which	*
	*				will be used for loading bubble		*
	*				wo/flag code to debug window		*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	private void BuildDebugCode_wo_flag()	{
		// Load, line by line, bubble wo/flag code to 
		// our Vector (code_wo_flag) object		code_wo_flag.addElement("for (int i = N; --i >= 0)");
		code_wo_flag.addElement("{"); 		code_wo_flag.addElement("   for (int j = 0; j < i; j++)");		code_wo_flag.addElement("      if (a[j] > a[j+1])");  		code_wo_flag.addElement("         Swap(a[j], a[j + 1]);"); 		code_wo_flag.addElement("}"); 	}
		/****************************************************	
	* Function:		load_wflag_DebugCode()				*
	* Description:	Loads our bubble w/flag code to		*
	*				debug's window list box				*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	public void load_wflag_DebugCode()	{
		// Clear debug's window list box		m_debugWindow.ClearList();		// Add a string to the debug's window list box
		for (int i = 0; i < code_w_flag.size(); i++)
			m_debugWindow.AddLine((String)(code_w_flag.elementAt(i))); 	}
	
	/****************************************************	
	* Function:		load_woflag_DebugCode()				*
	* Description:	Loads our bubble wo/flag code to	*
	*				debug's window list box				*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	public void load_woflag_DebugCode()	{		// Clear debug's window list box		m_debugWindow.ClearList();		
		// Add a string to the debug's window list box
		for (int i = 0; i < code_wo_flag.size(); i++)
			m_debugWindow.AddLine((String)(code_wo_flag.elementAt(i))); 	}
}
