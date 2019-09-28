/********************************************************	
 * File:			CAnimatedPanel.java					*
 * Description:		A sub-panel class of CSortAnimator	*
 *					class that contains just the		*
 *					animation area.						*
 * Author:			Eric Torman (etorman@hotmail.com)	*
 * Date created:	August 15, 1999 (ET)				*
 * ******************************************************
 */

// Java's header files required for this class
import java.awt.*;
import java.awt.event.*;
import java.util.*;

// Statistics structure that we will display in this
// panel once the user click statistics button
class Statistics
{
	String algName;		// Name of the algorithm
	int noElements;		// Number of elements
	int timeElapsed;	// Time elapsed (ms)
	int noExchanges;	// Number of exchanges
	int noComparisons;	// Number of comparisons
	String arrType;		// Type of the array (random, ascending, 
						// descending)
}

// CAnimatedPanel class is derived from Panel class
public class CAnimatedPanel extends Panel 
{
	// Maximum of 5 graphs will be displayed at a time
	private int MAX_NUMBER_OF_GRAPHS = 5;
	// List box will have maximum of 100 items
	private int MAX_NUMBER_OF_ITEMS  = 100;
	
	// Vector object where we store statistics information
	// after the algorithm is complete
	public Vector statVector  = new Vector(MAX_NUMBER_OF_ITEMS);
	// List box where we will display the statistics information
	public java.awt.List   statList    = new java.awt.List();
	// Graph button
	public Button m_btnGraph  = new Button("Graph"); 		
	// Combo box for selecting variuous graphs
	public Choice m_cboGraph  = new Choice();
	// Clear list button
	public Button m_btnClear  = new Button("Clear list");
	// Information label about the statistics panel
	public Label  m_lblSelect = new Label("Max: 5 graphs, 100 items");
	
	// Label that explains what various columns of the list box 
	// mean
	public Label bigLabel = new Label();
	
	// Regular font -- DON'T CHANGE this or the program may not work!
	private Font fnt = new Font("Arial", Font.PLAIN, 12);
	// Font for information label only -- DON'T CHANGE this
	// or the program may not work
	private Font fntWarn = new Font("Arial", Font.BOLD, 12); 
	
	// ID's for graph selection combo box
	public final int ELEMENTS_VS_TIME_ID     = 0;
	public final int ELEMENTS_VS_EXCHANGES   = 1;
	public final int ELEMENTS_VS_COMPARISONS = 2;
	
	// Parent of this panel
	private CSortAnimator parent;
	
	// Image object of this panel
	protected Image m_drawImage;
	// Graphics object of this panel
	protected Graphics m_drawGraphics;
	
	// Background color
	private final Color bgColor = new Color(220,210,180);

	/****************************************************	
	* Function:		CAnimatedPanel() -- Constructor		*
	* Description:	Simple constructor function.		*
	*				Creates layout, adds events to		*
	*				buttons								*
	*													*
	* Input:		Parent of this panel				*
	* 				(CSortAnimator parentPanel)			*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	Note that in Java there is no		*
	*				destructor. You can override		*
	*				protected void finalize() function,	*
	*				and it'll get called by Java's		*
	*				garbage	collector					*	
	*****************************************************
	*/
	public CAnimatedPanel(CSortAnimator parentPanel)
	{
		// Set the parent of this panel
		parent = parentPanel;
		// Fill combo box with strings
		loadGraphCombo();
		
		// Create new grid bag layout
		GridBagLayout       gbl = new GridBagLayout();
		GridBagConstraints  gbc = new GridBagConstraints();
		setLayout(gbl);
			
		// Text for the big label object
		String s;

		// Create a text that will explain what every column in list
		// box means
		// DON'T CHANGE this or the program may not work!
		s =  "Name                         ";
		s += "Array size  ";
		s += "Time (ms.)  ";
		s += "Exchanges   ";
		s += "Comparisons    ";
		s += "Order";
			
		// Set the text of the label
		bigLabel.setText(s);
			
		// Add header-type label
		buildConstraints(gbc, 0, 0, 4, 1, 0, 5);
		gbc.fill       = GridBagConstraints.NONE;
		gbc.anchor       = GridBagConstraints.WEST;
		bigLabel.setFont(fnt);
		bigLabel.setAlignment(Label.LEFT);  
		gbl.setConstraints(bigLabel, gbc);
		add(bigLabel);

		// Add list box
		buildConstraints(gbc, 0, 1, 4, 1, 0, 85);
		gbc.fill       = GridBagConstraints.BOTH;
		gbl.setConstraints(statList, gbc);
		add(statList);
			
		// Add 'Graph' button
		buildConstraints(gbc, 0, 2, 1, 1, 10, 10);
		gbc.fill       = GridBagConstraints.NONE;
		gbc.anchor = GridBagConstraints.CENTER ;
		gbl.setConstraints(m_btnGraph, gbc);
		add(m_btnGraph);
			
		// Add combo box
		buildConstraints(gbc, 1, 2, 1, 1, 8, 0);
		gbc.fill       = GridBagConstraints.NONE ;
		gbc.anchor = GridBagConstraints.CENTER ;
		gbl.setConstraints(m_cboGraph, gbc);
		add(m_cboGraph);
		
		// Add 'Clear' button
		buildConstraints(gbc, 2, 2, 1, 1, 10, 0);
		gbc.fill       = GridBagConstraints.NONE ;
		gbc.anchor = GridBagConstraints.CENTER;
		gbl.setConstraints(m_btnClear, gbc);
		add(m_btnClear);
		
		// Add information label
		buildConstraints(gbc, 3, 2, 1, 1, 72, 0);
		gbc.fill       = GridBagConstraints.NONE ;
		gbc.anchor = GridBagConstraints.CENTER;
		m_lblSelect.setFont(fntWarn);
		m_lblSelect.setAlignment(Label.LEFT);  
		gbl.setConstraints(m_lblSelect, gbc);
		add(m_lblSelect);
			
		// Disable 'Graph' button
		m_btnGraph.setEnabled(false); 
		// Handle an event when user clicks on graph button
		m_btnGraph.addActionListener(new GraphClick());
		// Handle an event when user clicks on clear list button
		m_btnClear.addActionListener(new ClearListClick()); 
		// Set the font of the list box
		statList.setFont(fnt);
		// Allow multiple selections in the list box
		statList.setMultipleMode(true); 
	}
		
	/****************************************************	
	* Function:		paint()								*
	* Description:	Draws a memory-buffer image on the	*
	*				screen								*
	* 													*
	* Input:		Graphics object	of the panel		*
	*				(Graphics g)						*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public void paint(Graphics g) 
	{
		// Draw an image
		g.drawImage(m_drawImage, 0, 0, null);		
	}
		
	/****************************************************	
	* Function:		update()							*
	* Description:	Calls paint to draw an image		*
	*				Will get called automatically if	*
	*				repaint() has been issued			*
	* 													*
	* Input:		Graphics object	of the panel		*
	*				(Graphics g)						*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public synchronized void update(Graphics g)
	{
		// Call paint to draw an image
		paint(g);
	}

	/****************************************************	
	* Function:		AddToList()							*
	* Description:	Builds one huge string and adds to	*
	*				the list box. The string will		*
	*				contain statistical information		*
	* 													*
	* Input:		Name of the algorithm				*
	*				(String algName)					*
	*				Number of elements					*
	*				(String noElements)					*
	*				Time elapsed						*
	*				(String timeElapsed)				*
	*				Number of exchanges					*
	*				(String noExchanges)				*
	*				Number of comparisons				*
	*				(String noComparisons)				*
	*				Array type							*
	*				(String arrType)					*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	private void AddToList(String algName, String noElements,
							  String timeElapsed, String noExchanges,
							  String noComparisons, String arrType)
	{
		// String that we will add to the list box
		String s;
		// Font metric of the font used in the list box	
		FontMetrics f = getFontMetrics(fnt);
		
		// Calculare number of spaces we need to add to the name of
		// the algorithm.
		int spaceNum = (110 - f.stringWidth(algName)) / f.stringWidth(" "); 
						
		// Pad spaces to it
		algName = PadString(spaceNum, algName);
		// Assign to our big string
		s = algName; 
			
		// Calculare number of spaces we need to add to the number of
		// elements.
		spaceNum = (64 - f.stringWidth(noElements)) / f.stringWidth(" "); 
			
		// Pad spaces to it
		noElements = PadString(spaceNum, noElements);
		// Add it to our string
		s += noElements;
		
		// Calculare number of spaces we need to add to time elapsed
		spaceNum = (65 - f.stringWidth(timeElapsed)) / f.stringWidth(" "); 
			
		// Pad spaces
		timeElapsed = PadString(spaceNum, timeElapsed);
		// Add it to our big string
		s += timeElapsed;
			
		// Calculare number of spaces we need to add to the number of
		// exchanges.
		spaceNum = (70 - f.stringWidth(noExchanges)) / f.stringWidth(" "); 

		// Pad spaces
		noExchanges = PadString(spaceNum, noExchanges);
		// Add it to our big string
		s += noExchanges;
			
		// Calculare number of spaces we need to add to the number of
		// comparisons.
		spaceNum = (85 - f.stringWidth(noComparisons)) / f.stringWidth(" "); 
		// Pad spaces
		noComparisons = PadString(spaceNum, noComparisons);
		// Add it to our big string
		s += noComparisons;

		// Finally, add array type to our big string
		s += arrType;
		// Add our big string to the list box
		statList.add(s); 
	}
	
	/****************************************************	
	* Function:		PadString()							*
	* Description:	Adds spaces to the string			*
	* 													*
	* Input:		Number of spaces to add				*
	*				(int width)							*
	* Output:		NONE								*
	* Return value:	Padded string						*
	* Side effects:	NONE								*
	*****************************************************
	*/
	private String PadString(int width, String s)
	{
		// Add spaces
		for (int i = 0; i < width; i++)
			s += " ";
		return s;
	}
		
	/****************************************************	
	* Function:		loadGraphCombo()					*
	* Description:	Loads string to the combo box		*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	private void loadGraphCombo()
	{
		// Add strings to the combo box
		m_cboGraph.addItem("# of elements vs. time");
		m_cboGraph.addItem("# of elements vs. # of exchanges");
		m_cboGraph.addItem("# of elements vs. # of comparisons");
	}
		
	/****************************************************	
	* Function:		handleEvent()						*
	* Description:	Handles any event of this panel		*
	*				Here, we are only interested when	*
	*				user selectes and deselectes		*
	*				something from the list box			*
	* 													*
	* Input:		Event object						*
	* 				(Event e)							*
	* Output:		NONE								*
	* Return value:	Value if the event was consumed		*
	* Side effects:	NONE								*
	*****************************************************
	*/	
	public boolean handleEvent(Event e)
	{
		// Intercept event generated by the list box
		if (e.target instanceof java.awt.List)
		{
			// Check if the user just selected something
			// from the list box
			if (e.id == e.LIST_SELECT) 
			{
				// Get number of selected items
				int nCount[] = statList.getSelectedIndexes();
				// If user exceeded maximum number of allowed graphs,
				// disable the 'Graph' button
				if (nCount.length > MAX_NUMBER_OF_GRAPHS)	
					m_btnGraph.setEnabled(false);
				else
				// Otherwise, enable the 'Graph' button
					m_btnGraph.setEnabled(true);					
			}
			// Check if the user just deselected something
			// from the list box
			if (e.id == e.LIST_DESELECT) 
			{
				// Get number of selected items
				int nCount[] = statList.getSelectedIndexes();
				// Make sure we have valid number of selected items
				// before enabling 'Graph' button again
				if (nCount.length > 0 && nCount.length <= MAX_NUMBER_OF_GRAPHS)
					m_btnGraph.setEnabled(true);										
				else
					m_btnGraph.setEnabled(false);
			}
		}
		return false;
	}
		
	public void SetBackground()
	{
		int width, height;
		width = getSize().width;
		height = getSize().height;

		if (m_drawImage == null)
			m_drawImage = createImage(width, height);
		
		m_drawGraphics = m_drawImage.getGraphics(); 
		
		m_drawGraphics.setColor(bgColor);
		m_drawGraphics.fillRect(0, 0, width, height);
	}

	public int GraphSelection()
	{
		return m_cboGraph.getSelectedIndex(); 
	}
		
	public class ClearListClick implements ActionListener
	{		
		public void actionPerformed(ActionEvent e)
		{
			statList.removeAll();
			statVector.removeAllElements(); 
			m_btnGraph.setEnabled(false); 
		}
	}
	public class GraphClick implements ActionListener
	{		
		public void actionPerformed(ActionEvent e)
		{
			int selCount[] = statList.getSelectedIndexes();  
				
			if (selCount.length > 0 && selCount.length <= MAX_NUMBER_OF_GRAPHS)
			{
				int x[] = new int[selCount.length]; 
				double y[] = new double[selCount.length];
				Vector algName = new Vector();
				Statistics stat;
				String x_label = "", y_label = "";
				
				for (int i = 0; i < selCount.length; i++)
				{
					stat = (Statistics) statVector.elementAt(selCount[i]);
					x[i] = (int)stat.noElements;
					algName.addElement(stat.algName + "(" + stat.arrType + ")");  
							
					int selIndex = GraphSelection(); 
							
					if (selIndex == ELEMENTS_VS_TIME_ID)
					{
						y[i] = (int)stat.timeElapsed;
						x_label = "Number of elements";
						y_label = "Time ms.";
					}
					else if (selIndex == ELEMENTS_VS_EXCHANGES)
					{
						y[i] = (int)stat.noExchanges;
						x_label = "Number of elements";
						y_label = "Number of exchanges";
					}
					else 
					{
						y[i] = (int)stat.noComparisons;
						x_label = "Number of elements";
						y_label = "Number of comparisons";
					}
				}
				CGraph gr = new CGraph(parent.m_drawArea);
				
				HideStatistics();
				gr.DrawGraph(x, y, true, algName, x_label, y_label);
			}
		}
	}

	public void AddStatistics(String algName, int noElements,
							  int time, int noExchanges, 
							  int noComparisons, String arrType)
	{
		Statistics newNode = new Statistics();
		newNode.algName = algName;
		newNode.noElements = noElements;
		newNode.timeElapsed = time;
		newNode.noExchanges = noExchanges;
		newNode.noComparisons = noComparisons;
		newNode.arrType = arrType;
		
		int nItems = statList.getItemCount();
		
		if (nItems >= 100)
		{
			statVector.removeElementAt(0);
			statList.delItem(0);
		}

		statVector.addElement(newNode);
		AddToList(algName, String.valueOf(noElements),
		 		  String.valueOf(time), 
				  String.valueOf(noExchanges),
				  String.valueOf(noComparisons),
				 arrType);		
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
	
	/****************************************************	
	* Function:		Initialize()						*
	* Description:	Creates an image object, creates	*
	*				a rectangle filled with white color	*
	*				and lines surrounding the rectangle	*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public void Initialize()
	{				
		// Width and height of this panel
		int width, height;
		// Get the width and height of this panel
		width = getSize().width;
		height = getSize().height;

		// If we don't have an image object, create it
		if (m_drawImage == null)
			m_drawImage = createImage(width, height);
		
		// Get the graphics object of an image object
		m_drawGraphics = m_drawImage.getGraphics(); 
		
		// Create fill and draw rectangels
		m_drawGraphics.setColor(Color.white);
		m_drawGraphics.fillRect(0, 0, width, height);
		m_drawGraphics.setColor(Color.black);
		m_drawGraphics.drawRect(0, 0, width - 1, height - 1);
	}
	
	/****************************************************	
	* Function:		Hidetatistics()						*
	* Description:	Sets controls of this panel to be	*
	*				not visisble						*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public void HideStatistics()
	{
		// Hide controls
		bigLabel.setVisible(false);  
		m_cboGraph.setVisible(false);  
		statList.setVisible(false);
		m_btnGraph.setVisible(false);  
		m_btnClear.setVisible(false);
		m_lblSelect.setVisible(false);
	}

	/****************************************************	
	* Function:		ShowStatistics()					*
	* Description:	Clears the image and sets the		*
	*				controls of this panel to visisble	*
	* 													*
	* Input:		NONE								*
	* Output:		NONE								*
	* Return value:	NONE								*
	* Side effects:	NONE								*
	*****************************************************
	*/
	public void ShowStatistics()
	{
		// Clear an image
		repaint(); 
		
		// Set every control to visible
		bigLabel.setVisible(true);  
		m_cboGraph.setVisible(true);  
		statList.setVisible(true);		
		m_btnGraph.setVisible(true);		
		m_btnClear.setVisible(true);
		m_lblSelect.setVisible(true);
				
		// Change the background color of this panel
		// to applet's background color
		SetBackground();	
	}
}
