
//import CSortTopPart.*;
// import CSortAnimator.*;
// import CDebugWindow.*;
// import CStatisticsWindow.*;
//import CSortAlgorithm.*;
//import RunThread.*;
import java.awt.*;
import java.io.*;
import java.net.*;


public class SortApplet extends java.applet.Applet 
{
	//Ria added these constants here
	public static final int BUBBLE_SORT_ID       = 0;
	public static final int BUBBLE_SORT_WFLAG_ID = 1;
	public static final int INSERTION_SORT_ID    = 2;
	public static final int SELECTION_SORT_ID    = 3;
	public static final int SHELL_SORT_ID		 = 4;
	public static final int HEAP_SORT_ID		 = 5;
	public static final int QUICK_SORT_ID		 = 6;
	
	
	public static final int RANDOM_ID			 = 0;
	public static final int ASCENDING_ID		 = 1;
	public static final int DESCENDING_ID		 = 2;
	public String help_location;
	public CSortTopPart top;
	public CSortAnimator an;
	public CStatisticsWindow m_statsWin;
	public CDebugWindow m_debugWin;
	
	private CSortAlgorithm m_currAlg;
	private RunThread m_runThread;

	private CBubbleSort m_bubbleSort;
	private CInsertionSort m_insertionSort;
	private CSelectionSort m_selectionSort;
	private CHeapSort m_heapSort;
	private CShellSort m_shellSort;
	private CQuickSort m_quickSort;
			
	public void init()
	{		
		Color bgColor = new Color(220,210,180);
		setBackground(bgColor);
		
		//help_location = getParameter("link");
		
		top = new CSortTopPart(this);
		an = new CSortAnimator(this); 
		m_statsWin = new CStatisticsWindow(this);
		m_debugWin = new CDebugWindow(this);
							   
		m_bubbleSort    = new CBubbleSort(this);
		m_insertionSort = new CInsertionSort(this);
		m_selectionSort = new CSelectionSort(this);
		m_heapSort      = new CHeapSort(this);	
		m_shellSort     = new CShellSort(this); 
		m_quickSort     = new CQuickSort(this); 
		
		GridBagLayout gbLayout = new GridBagLayout();
		GridBagConstraints gbConst = new GridBagConstraints();
		setLayout(gbLayout);

		buildConstraints(gbConst, 0, 0, 2, 1, 0, 7);
	    gbConst.fill = GridBagConstraints.HORIZONTAL;
		gbLayout.setConstraints(top, gbConst);
		add(top);

		buildConstraints(gbConst, 0, 1, 1, 2, 60, 0);
	    gbConst.fill = GridBagConstraints.BOTH;
		gbLayout.setConstraints(an, gbConst);
		add(an);
		
		buildConstraints(gbConst, 1, 1, 1, 1, 40, 3);
	    gbConst.fill = GridBagConstraints.BOTH;
		gbLayout.setConstraints(m_statsWin, gbConst);
		add(m_statsWin);
		
		gbConst.insets = new Insets(0, 3, 3, 3);
		buildConstraints(gbConst, 1, 2, 1, 1, 0, 90);
	    gbConst.fill = GridBagConstraints.BOTH;
		gbLayout.setConstraints(m_debugWin, gbConst);
		add(m_debugWin);
		
		SetControls_Finish();
					
		algorithmChange(top.m_cboAlgorithm.getSelectedIndex());
	}
	
	public void start()
	{
		an.m_drawArea.HideStatistics();
		an.Initialize();
		an.m_drawArea.repaint();
	}
	
	public void stop()
	{
		animationPanelBtnClick(an.RESET);
	}
	
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

	public void animationPanelBtnClick(int btnId)
	{
		int noElements;

		if (btnId == an.RESET)
		{
			if (m_runThread != null)
			{
				m_runThread.stop();
				m_runThread = null;
			}
			SetControls_Finish();
			ResetStatistics();
		}
		else if (btnId == an.START)
		{
			SetControls_Start(false);
			StartAlgorithm(false);
		}
	}
	
	public void debugWindowBtnClick(int btnId)
	{
		if (btnId == m_debugWin.PAUSE)
		{
			m_currAlg.SetUserMode(true); 
			SetControls_Pause();
		}
		else if (btnId == m_debugWin.STEP)
		{
			if (m_runThread == null)
			{
				SetControls_Start(true);
				StartAlgorithm(true);								
			}
			else
				m_runThread.resume(); 	
		}
		else if (btnId == m_debugWin.CONTINUE)
		{
			SetControls_Continue();
			m_currAlg.SetUserMode(false);
			m_runThread.resume(); 
		}
	}
	
	public void algorithmChange(int sortId)
	{
		switch (sortId)
		{
			//Ria changed from top.BUBBLE_SORT_ID (also in another switch statement in this class
			case BUBBLE_SORT_ID:
				m_debugWin.SetFont(m_debugWin.fontDefault); 
				m_bubbleSort.load_woflag_DebugCode(); 
				m_currAlg = m_bubbleSort;
			break;
			
			case BUBBLE_SORT_WFLAG_ID:
				m_debugWin.SetFont(m_debugWin.fontDefault); 
				m_bubbleSort.load_wflag_DebugCode(); 
				m_currAlg = m_bubbleSort;
			break;
			case SELECTION_SORT_ID:
				m_debugWin.SetFont(m_debugWin.fontDefault); 
				m_selectionSort.loadDebugCode();
				m_currAlg = m_selectionSort;
			break;	

			case INSERTION_SORT_ID:
				m_debugWin.SetFont(m_debugWin.fontDefault); 
				m_insertionSort.loadDebugCode();
				m_currAlg = m_insertionSort;
			break;	

			case HEAP_SORT_ID:
				m_debugWin.SetFont(m_debugWin.fontHeapSort); 
				m_heapSort.loadDebugCode();
				m_currAlg = m_heapSort;
			break;	

			case SHELL_SORT_ID:
				m_debugWin.SetFont(m_debugWin.fontDefault); 
				m_shellSort.loadDebugCode();
				m_currAlg = m_heapSort;
			break;	

			case QUICK_SORT_ID:
				m_debugWin.SetFont(m_debugWin.fontHeapSort ); 
				m_quickSort.loadDebugCode();
				m_currAlg = m_quickSort;
			break;	
		}		
	}
	
	private void SetControls_Pause()
	{
		m_debugWin.m_btnPause.setEnabled(false);
		m_debugWin.m_btnContinue.setEnabled(true);
		m_debugWin.m_btnStep.setEnabled(true);  
	}
	private void SetControls_Continue()
	{
		m_debugWin.m_btnPause.setEnabled(true);
		m_debugWin.m_btnContinue.setEnabled(false);
		m_debugWin.m_btnStep.setEnabled(false);  
	}
	private void SetControls_Start(boolean stepThrough)
	{
		top.m_txtNoElements.setEnabled(false);  
		top.m_cboAlgorithm.setEnabled(false);
		top.m_cboArrayOrder.setEnabled(false);
		
		an.m_btnStart.setEnabled(false);
		an.m_btnStatistics.setEnabled(false);
		an.m_chkAnimation.setEnabled(false);
				
		if (ShowAnimation())
		{
			if (stepThrough)
			{
				m_debugWin.m_btnPause.setEnabled(false);  
				m_debugWin.m_btnStep.setEnabled(true);
				m_debugWin.m_btnContinue.setEnabled(true);
			}
			else
			{
				m_debugWin.m_btnPause.setEnabled(true);
				m_debugWin.m_btnStep.setEnabled(false);
				m_debugWin.m_btnContinue.setEnabled(false);
			}
		}
		else
		{
			m_debugWin.m_btnPause.setEnabled(false);
			m_debugWin.m_btnContinue.setEnabled(false);
			m_debugWin.m_btnContinue.setEnabled(false);		
		}
	}

	private void SetControls_Finish()
	{
		top.m_cboAlgorithm.setEnabled(true); 
		top.m_txtNoElements.setEnabled(true); 
		top.m_cboArrayOrder.setEnabled(true);
		
		an.m_btnStart.setEnabled(true);
		an.m_chkAnimation.setEnabled(true);
		an.m_btnStatistics.setEnabled(true);
				
		m_debugWin.m_btnPause.setEnabled(false);
		m_debugWin.m_btnContinue.setEnabled(false);  
		
		if (ShowAnimation())
			m_debugWin.m_btnStep.setEnabled(true);
		else
			m_debugWin.m_btnStep.setEnabled(false);
	}
	
	public synchronized void FinishedAlgorithm()
	{
		m_debugWin.DeselectCurrentLine();
		m_statsWin.m_txtTimeElapsed.setText(String.valueOf(m_currAlg.m_nCompletionTime));
		if (!ShowAnimation())
		{
			UpdateNoExchanges(m_currAlg.m_nExchanges);
			UpdateNoComparisons(m_currAlg.m_nComparisons); 
		}
		if (m_runThread != null)
			m_runThread = null;
		SetControls_Finish();
		an.m_drawArea.AddStatistics(top.m_cboAlgorithm.getSelectedItem(),
						 Integer.parseInt(top.m_txtNoElements.getText()),
						 (int)m_currAlg.m_nCompletionTime,
						 m_currAlg.m_nExchanges,
						 m_currAlg.m_nComparisons,
						 top.m_cboArrayOrder.getSelectedItem()); 
								
	}
	
	
	public void StartAlgorithm(boolean userMode)
	{		
		an.m_drawArea.HideStatistics();
		
		switch (top.m_cboAlgorithm.getSelectedIndex())
		{
			case BUBBLE_SORT_ID:
				m_bubbleSort.bBubble_w_Flag = false;
				m_currAlg = m_bubbleSort;
			break;
			
			case BUBBLE_SORT_WFLAG_ID:
				m_bubbleSort.bBubble_w_Flag = true;
				m_currAlg = m_bubbleSort;
			break;
				
			case SELECTION_SORT_ID:
				m_currAlg = m_selectionSort;
			break;
			case INSERTION_SORT_ID:
				m_currAlg = m_insertionSort;
			break;

			case HEAP_SORT_ID:
				m_currAlg = m_heapSort;
			break;

			case SHELL_SORT_ID:
				m_currAlg = m_shellSort;
			break;

			case QUICK_SORT_ID:
				m_currAlg = m_quickSort;
			break;
		}

		ResetStatistics();

		CheckElementsText();
		
		int noElements = Integer.parseInt(top.m_txtNoElements.getText());
		boolean showAnimation = ShowAnimation();
						
		m_currAlg.SetAnimation(showAnimation);  
		m_currAlg.SetUserMode(userMode);

		if (showAnimation)
		{
			m_runThread = new RunThread(this, noElements, top.m_cboArrayOrder.getSelectedIndex());
			m_runThread.SetCurrentAlg(m_currAlg); 
			m_runThread.start(); 
		}
		else
		{
			int width, height;
			width  = an.m_drawArea.getSize().width;
			height = an.m_drawArea.getSize().height;
			
			an.m_drawArea.Initialize(); 
			Image im = an.m_drawArea.m_drawImage; 
			Graphics g = im.getGraphics();
			
			an.m_drawArea.paint(an.m_drawArea.getGraphics());
			
			g.setFont(new Font("Times New Roman", Font.BOLD, 20 ));  
			g.drawString("Running algorithm...", (width / 2) - 70, (height / 2) - 20);
			an.m_drawArea.paint(an.m_drawArea.getGraphics());
			m_currAlg.sort(noElements, top.m_cboArrayOrder.getSelectedIndex());   
			FinishedAlgorithm();

			g.drawString("Complete!", (width / 2) - 70, (height / 2) + 20);
			an.m_drawArea.paint(an.m_drawArea.getGraphics());
		}		
	}
	
	public synchronized void UpdateNoExchanges(int noExchanges)
	{
		String s = String.valueOf(noExchanges);
		m_statsWin.m_txtNoExchanges.setText(s); 
	}
	
	public synchronized void UpdateNoComparisons(int noComparisons)
	{
		String s = String.valueOf(noComparisons);
		m_statsWin.m_txtNoComparisons.setText(s); 
	}
	
	private void ResetStatistics()
	{
		m_statsWin.m_txtTimeElapsed.setText("0");  
		m_statsWin.m_txtNoExchanges.setText("0");
		m_statsWin.m_txtNoComparisons.setText("0");	
	}
	
	public void animationChange(int sortId)
	{
		if (sortId == an.INSTANT_ID)
			an.SetAnimationSpeed(an.INSTANT_ANIMATION);
		else if (sortId == an.FAST_ID)
			an.SetAnimationSpeed(an.FAST_ANIMATION);
		else if (sortId == an.MEDIUM_ID)
			an.SetAnimationSpeed(an.MEDIUM_ANIMATION);
		else if (sortId == an.SLOW_ID)
			an.SetAnimationSpeed(an.SLOW_ANIMATION);
	}
	/********************************************
	 * Function:    CheckElementsText()         *
	 * Description: Whenever text field of      *
	 *              number of elements loses    *
	 *              focus, this function will   *
	 *              get called.                 *
	 *              It basically checks to make *
	 *              sure user entered valid     *
	 *              input for number of         *
	 *              elements to sort            *
	 * Author:      Eric Torman                 *
	 * Input:       NONE                        *
	 * Output:      NONE						*
	 * Return value:NONE						*
	 * Side effects:NONE						*
	 * ******************************************
	 */
	public void CheckElementsText()
	{
		// Integer representing number of elements to sort
		int noElements;
		
		// Get the text string from the number of elements text box
		String s = top.m_txtNoElements.getText();
		
		// If there was nothing in the text box, default the text box
		// back to 100 elements to sort
		if (s == null)
		{
			top.m_txtNoElements.setText(String.valueOf(an.MAX_NUMBER_ELEMENTS));  
			return;
		}
		
		// Try to convert a text string to integer.
		// This will check if user input is integer type
		try
		{
			noElements = Integer.parseInt(s);
		}
		catch (NumberFormatException a)
		{	// User input is not integer type
			// Default the text box back to 100 elements to sort
			top.m_txtNoElements.setText(String.valueOf(an.MAX_NUMBER_ELEMENTS));  				
			return;
		}
		
		// If animation flag is checked, make sure that number of
		// elements to sort falls between 1 < n <= 100.
		if (an.m_chkAnimation.getState())
		{	
			if (!(noElements > 1 && noElements <= 100))
				top.m_txtNoElements.setText(String.valueOf(an.MAX_NUMBER_ELEMENTS));
		}
		else
		{
			// More than 1000000 is possible BUT WHY?????
			if (!(noElements > 1 && noElements <= 1000000))
				top.m_txtNoElements.setText("1000000");
		}			
	}
	
	/********************************************
	 * Function:	showAnimationChange()		*
	 * Description:	Whenever user click of		*
	 *				'Show animation' checkbox,	*
	 *				this function will get		*
	 *				called.						*
	 *				It basically sets the show	*
	 *				animation flag of the		*
	 *				current algorithm and		*
	 *				enables/disables animation	*
	 *				speed combo box				*
	 * Author:		Eric Torman					*
	 * Input:		Show animation flag			*
	 *				(boolean showAnimation		*
	 * Output:		NONE						*
	 * Return value:NONE						*
	 * Side effects:NONE						*
	 * ******************************************
	 */
	public void showAnimationChange(boolean showAnimation)
	{
		//m_currAlg.SetAnimation(showAnimation);
		an.m_cboAnimationSpeed.setEnabled(showAnimation);
		m_debugWin.m_btnStep.setEnabled(showAnimation);  
	}
	
	private boolean ShowAnimation()
	{
		return an.m_chkAnimation.getState();  
	}
}
