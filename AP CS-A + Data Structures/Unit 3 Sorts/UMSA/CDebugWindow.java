/********************************************************	
 * File:			CDebugWindow.java					*
 * Description:		Java class for debug window feature	*
 *					of the applet						*
 * Author:			Eric Torman (etorman@hotmail.com)	*
 * Date created:	August 1, 1999 (ET)					*
 ********************************************************
 */

// Jave header files required for this class
import java.awt.*;
import java.awt.event.*;

// This class, CDebugWindow is derived from Java's Panel class
public class CDebugWindow extends Panel
{
	// Our sorting applet variable -- we need this to pause
	// events to the main applet
	private SortApplet applet;
	
	// List box, which will contains algorithm's code for
	// user to see
	private List m_codeList = new List();
	// Three buttons, which correspond to 'debug' process
	// Pause button
	public Button m_btnPause = new Button("Pause");
	// Step button
	public Button m_btnStep  = new Button("Step");
	// Continue button
	public Button m_btnContinue  = new Button("Continue");
	
	// Main ID for group of buttons of this class
	private final int DEBUG_WINDOW_BUTTONS = 2000;
	
	// ID for Pause button
	public final int PAUSE    = DEBUG_WINDOW_BUTTONS + 0;
	// ID for Step button
	public final int STEP     = DEBUG_WINDOW_BUTTONS + 1;
	// ID for Continue button
	public final int CONTINUE = DEBUG_WINDOW_BUTTONS + 2;
	
	// The following two fonts will be used in list box
	// Almost all algorithms will look nicely in 12, Times New Roman font
	public final Font fontDefault  = new Font("Times New Roman", Font.PLAIN, 12);
	// Only heap algorithm will not work in 12, so we will use 11 for
	// heap algorithm only
	public final Font fontHeapSort = new Font("Times New Roman", Font.PLAIN, 11);

	/****************************************************	
	* Function:		CDebugWindow() -- Constructor		*
	* Description:	Simple constructor function.		*
	*				Creates layout, adds events to		*
	*				buttons								*
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
	*****************************************************
	*/
	public CDebugWindow(SortApplet parent)
	{
		// Set the applet variable
		applet = parent;
		
		// We will always use grid bag layout because we
		// need to know exact locations.
		GridBagLayout       gbl = new GridBagLayout();
		GridBagConstraints  gbc = new GridBagConstraints();
		setLayout(gbl);

		// Set layout for list box
		// List box takes 3 cells in x direction, 1 in y.
		// It also takes maximum of x direction and 87% of
		// y direction
		buildConstraints(gbc, 0, 0, 3, 1, 0, 95);
		gbc.fill       = GridBagConstraints.BOTH;
		gbl.setConstraints(m_codeList, gbc);
		add(m_codeList);
		
		// Disable the list box -- this prevents users from clicking
		// on the list box while there is code in the box
		// NOTE: In IE5 with proxy server, the selected line
		// will not be shown unless you take out the following line
		// of code. This appears to be a bug with IE5
		m_codeList.setEnabled(false);
		// Use default, 12, font
		m_codeList.setFont(fontDefault);
		
		// Set layout for 'Pause' button
		// It'll take 1 cell in x & y directions and
		// 20% of the x size and 13% of the y size
		buildConstraints(gbc, 0, 1, 1, 1, 20, 5);
		gbc.anchor = GridBagConstraints.EAST;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_btnPause, gbc);
		add(m_btnPause);
		
		// Set layout for 'Step' button
		// It'll take 1 cell in x & y directions and
		// 20% of the x size and maximum of the y size
		buildConstraints(gbc, 1, 1, 1, 1, 20, 0);
		gbc.anchor = GridBagConstraints.EAST;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_btnStep, gbc);
		add(m_btnStep);

		// Set layout for 'Continue' button
		// It'll take 1 cell in x & y directions and
		// 60% of the x size and maximum of the y size
		buildConstraints(gbc, 2, 1, 1, 1, 60, 0);
		gbc.anchor = GridBagConstraints.CENTER;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_btnContinue, gbc);
		add(m_btnContinue);
		
		// Add events to pause, step, and continue buttons
		m_btnPause.addActionListener(new PauseClick());
		m_btnStep.addActionListener(new StepClick());
		m_btnContinue.addActionListener(new ContinueClick());
	}
	
	/****************************************************	
	* Function:		buildConstraints()					*
	* Description:	Function for building constraints	*
	*				variable of grid bag layout manager	*
	* 													*
	* Input:		Grid bag constraints variable		*
	*				(GridBagConstraints gbc)			*
	* 				x position of where to start		*
	*				(int gx)							*
	*				y position of where to start		*
	*				(int gy)							*
	*				x number of cells we will take		*
	*				(int gw)							*
	*				y number of cells we will take		*
	*				(int gh)							*
	*				% of x space we will take			*
	*				(int wx)							*
	*				% of y space we will take			*
	*				(int wy)							*
	*													*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	private void buildConstraints(GridBagConstraints gbc, int gx,
								  int gy, int gw, int gh, int wx, int wy)
	{
		gbc.gridx = gx;
		gbc.gridy = gy;
		gbc.gridwidth = gw;
		gbc.gridheight = gh;
		gbc.weightx = wx;
		gbc.weighty = wy;
	}

	/****************************************************	
	* Function:		ClearList()							*
	* Description:	Function for clearing the contents	*
	*				of the list box						*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public void ClearList()
	{
		// Clear the list box
		m_codeList.removeAll(); 
	}
	
	/****************************************************	
	* Function:		AddLine()							*
	* Description:	Function for adding a string to the	*
	*				list box							*
	* 													*
	* Input:		String to add to the list box		*
	*				(String s)							*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public void AddLine(String s)
	{
		// Simply add a string to the list box
		m_codeList.addItem(s); 
	}
	
	/****************************************************
	* Function:		SelectLine()						*
	* Description:	Function for selecting a line in	*
	*				the list box						*
	* 													*
	* Input:		Line to select from the list box	*
	* 				(int lineIndex)						*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	The function is thread-safe			*
	*				If lineIndex is invalid, nothing is	*
	*				performed							*
	*****************************************************
	*/
	public synchronized void SelectLine(int lineIndex)
	{
		// If invalid index, simply return from the function
		if (lineIndex > m_codeList.getItemCount() || lineIndex < 0)
			return;
		// Otherwise, select the line from the list box
		m_codeList.select(lineIndex);
	}
	
	/****************************************************
	* Function:		DeselectCurrentLine()				*
	* Description:	Deselects current selected line of	*
	*				the list box						*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public void DeselectCurrentLine()
	{
		// Get the currently selected line
		int nLine = m_codeList.getSelectedIndex();
		// Deselect it only if it's valid
		if (nLine >= 0)
			m_codeList.deselect(nLine);
	}

	/****************************************************
	* Function:		SetFont()							*
	* Description:	Sets the font of the list box		*
	* 													*
	* Input:		New font of the list box			*
	*				(Font fnt)							*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public void SetFont(Font fnt)
	{
		// Set the new font
		m_codeList.setFont(fnt); 
	}

	/****************************************************
	* Class:		PauseClick()						*
	* Description:	Handles the clicking of the pause	*
	*				button								*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public class PauseClick implements ActionListener
    {
		// This function must exist in the class
		public void actionPerformed(ActionEvent e)
		{
			// When user clicks on the 'Pause' button, call
			// 'debugWindowBtnClick' function of the applet
			// NOTE: PAUSE is button id
			applet.debugWindowBtnClick(PAUSE);
		}
    }

	/****************************************************
	* Class:		StepClick()							*
	* Description:	Handles the clicking of the step	*
	*				button								*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public class StepClick implements ActionListener
    {
		// This function must exist in the class
		public void actionPerformed(ActionEvent e)
		{
			// When user clicks on the 'Step' button, call
			// 'debugWindowBtnClick' function of the applet
			// NOTE: STEP is button id
			applet.debugWindowBtnClick(STEP);
		}
    }
	
	/****************************************************
	* Class:		ContinueClick()						*
	* Description:	Handles the clicking of the			*
	*				continue button						*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public class ContinueClick implements ActionListener
    {
		// This function must exist in the class
		public void actionPerformed(ActionEvent e)
		{	
			// When user clicks on the 'Continue' button, call
			// 'debugWindowBtnClick' function of the applet
			// NOTE: CONTINUE is button id
			applet.debugWindowBtnClick(CONTINUE);
		}
    }
}
