/********************************************************	
 * File:			CSortAlgorithm.java					*
 * Description:		This Java class is the parent of	*
 *					any sorting algorithm.				*
 *					It makes easier for children		*
 *					classes to perform animation,		*
 *					variable updating.					*
 *					In addition, it performs various	*
 *					tasks that are common to every		*
 *					sorting algorithm					*
 *					(for example, randomizing an array)	*
 *														*
 *					NOTE: This class is abstract!		*
 *					Sorting algorithms must be derived	*
 *					from this class.					*
 * Author:			Eric Torman (etorman@hotmail.com)	*
 * Date created:	July 21, 1999 (ET)					*
 ********************************************************
 */

// Java's header files required for this class
import java.util.*;
import java.awt.*;

// Abstract class CSortAlgorithm
abstract class CSortAlgorithm
{
	// Variables of this class
	
	// The following three variables are return values
	// of Compare() function.
	// Better implementation would have been to make them
	// enumarated type, but apparently Java doesn't support
	// enumarated types.
	public final int EQUAL            = 0;
	public final int FIRST_IS_LARGER  = 1;
	public final int FIRST_IS_SMALLER = 2;
	
	// The following three variables are used
	// in Randomize() function
	// So, we can create an array of random numbers,
	// array in ascending order and array in descending order
	public final int ARRAY_RANDOM     = 0;
	public final int ARRAY_ASCENDING  = 1;
	public final int ARRAY_DESCENDING = 2;
	
	// Maximum seed value for Java's Math.Random() function
	// Similar to C++ version of performing randomization
	private final int MAX_SEED_VALUE = 999;
	
	// CSortAnimator class variable -- responsible for animation
	protected CSortAnimator m_sortAnimator;
	// CDebugWindow class variable -- responsible for debugging code
	protected CDebugWindow m_debugWindow;
	
	// Number of exchanges made
	public int m_nExchanges;
	// Number of comparisons made
	public int m_nComparisons;
	// Elapsed time (ms) for the algorithm
	public long m_nCompletionTime;

	// Flag if in step-through mode
	private boolean m_userMode;
	// Flag if user wants to see animation
	protected boolean m_showAnimation;
	
	// Our sorting applet
	private SortApplet applet;
	// Thread that calls sort() function
	private Thread runner;
	
	/****************************************************	
	* Function:		sort()								*
	* Description:	Runs a sorting algorithm			*
	*				This is an entry point to any		*
	*				sorting classes that are derived	*
	*				from this class						*
	* 													*
	* Input:		Number of elements that in an array	*
	*				(int nElements)						*
	*				Array order -- either ARRAY_RANDOM,	*
	*				ARRAY_ASCENDING, ARRAY_DESCENDING	*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
    protected void sort(int nElements, int arrType)	{		// Set the current thread variable
		runner = Thread.currentThread();		
		// Create a new array object with just enough elements		int arr[] = new int [nElements];

		// Randomize the array
		Randomize(arr, arrType);
		// Reset all variables of any sorting algorithm
		ResetVariables();
		// If user requested animation, call CSortAnimator class		// to draw a sorting table
		if (m_showAnimation)			m_sortAnimator.DrawTable(arr);
		
		// Variables for calculating completion time of the algorithm
		long start_time, end_time;		// Get the current time
		start_time = System.currentTimeMillis();		// Sort
		OnSort(arr);
		// Get the current time again		end_time = System.currentTimeMillis();
		// Calculate completion time
		m_nCompletionTime = end_time - start_time;
	}
	
	/****************************************************	
	* Function:		OnSort()							*
	* Description:	Abstract function. Must exist in	*
	*				derived class. This is where the	*
	*				derived class performs sorting		*
	* 													*
	* Input:		Array to sort						*
	*				(int a[])							*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
    abstract void OnSort(int a[]);
	
	/****************************************************	
	* Function:		Swap()								*
	* Description:	Function to perform swapping of two	*
	*				cells. In addition to swapping, it	*
	*				updates number of exchanges made	*
	* 													*
	* Input:		Array object						*
	*				(int arr[])							*
	*				First cell index of the array		*
	*				(int A)								*
	*				Second cell index of the array		*
	*				(int B)								*
	*				Flag if need to swap the actual		*
	*				contents of the array				*
	*				(boolean swapFlag)					*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	Cells A and B must be valid.		*
	*				Otherwise, Java will throw an		*
	*				exception. We don't catch any		*
	*				exceptions though.					*
	*				Most of the times, swapFlag will be	*
	*				set to true, so that we will also	*
	*				change the contents of the array.	*
	*				Only in for shell sort, the flag	*
	*				will be set to false so that we can	*
	*				animate the process but not perform	*
	*				actual swapping.					*
	*				If animation flag was set, the		*
	*				function also animates the process	*
	* ***************************************************
	*/
	protected void Swap(int arr[], int A, int B, boolean swapFlag)
	{	
		// Update number of exchanges
		m_nExchanges++;
		// If animation flag is set, show animation process
		// of two cells, and update number of exchanges box
		// of the applet
		if (m_showAnimation)
		{
			m_sortAnimator.AnimateSwap(A, B);
			applet.UpdateNoExchanges(m_nExchanges); 
		}		// If swapping flag is set, swap cells of the array
		// as well.		if (swapFlag)		{
			int temp;					temp = arr[A];			arr[A] = arr[B];
			arr[B] = temp;				}
	}
	
	/****************************************************	
	* Function:		Insert()							*
	* Description:	Function to animate insertion of	*
	*				a cell into another cell			*
	*				Useful for insertion sort only		*
	* 													*
	* Input:		Array object						*
	*				(int arr[])							*
	*				From cell index of the array		*
	*				(int A)								*
	*				To  cell index of the array			*
	*				(int B)								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	Cells A and B must be valid.		*
	*				Otherwise, Java will throw an		*
	*				exception. We don't catch any		*
	*				exceptions though.					*
	*				If animation flag was set, the		*
	*				function animates the insertion		*
	*				process								*
	* ***************************************************
	*/
	protected void Insert(int arr[], int A, int B)
	{	
		// Update number of exchanges
		m_nExchanges++;
		// If animation flag is set, show animation of 
		// inserting cells and update number of exchanges
		// in the applet
		if (m_showAnimation)
		{
			m_sortAnimator.AnimateInsert(A, B);
			applet.UpdateNoExchanges(m_nExchanges); 
		}	}
	
	/****************************************************	
	* Function:		SetApplet()							*
	* Description:	Sets various objects of this class	*
	* 													*
	* Input:		SortApplet object					*
	*				(SortApplet parent)					*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	Sets the applet object. Also sets	*
	*				the CSortAnimator and CDebugWin		*
	*				objects								*
	* ***************************************************
	*/
	protected void SetApplet(SortApplet parent)
	{
		// Set applet object
		applet = parent;
		// Set the CSortAnimator object
		m_sortAnimator = applet.an;		// Set the CDebugWin object
		m_debugWindow = applet.m_debugWin;	}
	
	/****************************************************	
	* Function:		Randomize()							*
	* Description:	Function to perform randomization	*
	*				of the array						*
	* 													*
	* Input:		Array object						*
	*				(int arr[])							*
	*				How to randomize the array			*
	*				(int arrType; either ARRAY_RANDOM,	*
	*				ARRAY_ASCENDING, or					*
	*				ARRAY_DESCENDING)					*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	private void Randomize(int a[], int arrType)
	{
		// Determine how to fill the array
		switch (arrType)
		{
			// Random numbers
			case ARRAY_RANDOM:
				// Initialize random object
				Random rnd = new Random();
				for (int i = 0; i < a.length; i++)
				{
					// For animation, set the seed value to 
					// MAX_SEED_VALUE, which is currently 999
					if (m_showAnimation)
						a[i] = Math.abs(rnd.nextInt()) % MAX_SEED_VALUE; 
					else
					// Otherwise, the seed value is the length of
					// of the array
						a[i] = Math.abs(rnd.nextInt()) % a.length; 
				}
			break;
			// Ascending order
			case ARRAY_ASCENDING:
				// For ascending order, simply fill the array
				// from 0 to the length of the array
				for (int i = 0; i < a.length; i++)
					a[i] = i;
			break;
			// Descending order
			case ARRAY_DESCENDING:
				// For descending order, simply fill the array
				// from length of the array to 0
				for (int i = 1; i <= a.length; i++)
					a[i-1] = a.length - i;
			break;
		}		
	}
	
	/****************************************************	
	* Function:		SetAnimation()						*
	* Description:	Sets animation flag					*
	* 													*
	* Input:		Flag to show animation or not		*
	* 				(boolean show)						*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	protected void SetAnimation(boolean show)
	{
		// Set our internal animation flag
		m_showAnimation = show;
	}
	
	/****************************************************	
	* Function:		ResetVariables()					*
	* Description:	Resets time elapsed, number of		*
	*				exchanges made and number of		*
	*				comparisons made					*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	* ***************************************************
	*/
	private void ResetVariables()
	{
		// Set completion time, number of exchanges and 
		// number of comparions variables to 0
		m_nCompletionTime = 0;
		m_nExchanges      = 0;		m_nComparisons    = 0;
	}
	
	/****************************************************	
	* Function:		SetUserMode()						*
	* Description:	Function to set whether the flag	*
	*				which we will be using to test if	*
	*				need to suspend the execution of	*
	*				the thread if user is in			*
	*				step-through mode.					*
	* 													*
	* Input:		User mode							*
	*				(boolean mode)						*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	Thread-safe function				*
	* ***************************************************
	*/
	protected synchronized void SetUserMode(boolean mode)
	{
		// Set the internal user mode flag
		m_userMode = mode;
	}
	
	/****************************************************	
	* Function:		GetUserMode()						*
	* Description:	Function to get the debug mode flag	*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	Current debug mode flag				*
	* Side effects:	Thread-safe function				*
	* ***************************************************
	*/
	protected synchronized boolean GetUserMode() 
	{
		// Return the current user mode flag
		return m_userMode;
	}
	
	/****************************************************	
	* Function:		Compare()							*
	* Description:	Function to perform comparison of	*
	*				two cells of the array.	In addition,*
	*				to comparison, it also tests		*
	*				whether the first cell is equal,	*
	*				larger or smaller than the second	*
	*				cell.								*
	* 													*
	* Input:		Array object						*
	*				(int arr[])							*
	*				First cell of the array				*
	*				(int A)								*
	*				Second cell of the array			*
	*				(int B)								*
	* Output:		NONE								*
	* Return value:	EQUAL if arr[A] = arr[B]			*
	*				FIRST_IS_SMALLER if arr[A] < arr[B]	*
	*				FIRST_IS_LARGER if arr[A] > arr[B]	*
	* Side effects:	A and B must be valid or a Java		*
	*				exception will occur. This function	*
	*				also updates number of comparions,	*
	*				and performs comparison animation	*
	* ***************************************************
	*/
	protected int Compare(int arr[], int A, int B)
	{
		// Update number of comparisons		m_nComparisons++;

		// If animation flag is set, show comparison animation
		// process and update number of comparisons made
		if (m_showAnimation)
		{			m_sortAnimator.AnimateCompare(A, B); 
			applet.UpdateNoComparisons(m_nComparisons);
		}		
		// Test whether arr[A] is equal arr[B], larger than arr[B],
		// smaller than arr[B].
		if (arr[A] > arr[B])
			return FIRST_IS_LARGER;
		else if (arr[A] < arr[B])
			return FIRST_IS_SMALLER;
		else
			return EQUAL;
	}
	
	/****************************************************	
	* Function:		SelectLine()						*
	* Description:	Selects a particular line from the	*
	*				debug window						*
	* 													*
	* Input:		Line to select						*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	This function will not do anything	*
	*				if animation flag is not set.		*
	*				If animation flag is set and the	*
	*				call to this function is made, then	*
	*				the line pointed by nLine will be	*
	*				selected from the list box. Also,	*
	*				if the user mode variable was true,	*
	*				it suspends the execution of the	*
	*				running thread.						*
	*				This is basically how step-through	*
	*				window works!						*
	* ***************************************************
	*/	
	protected void SelectLine(int nLine)
	{		
		// Don't do anything if animation is not set
		if (m_showAnimation)
		{
			// Select a line from the list box
			m_debugWindow.SelectLine(nLine);
			// If in user mode, suspend the thread
			if (GetUserMode()) 				runner.suspend(); 
		}
	}
}
