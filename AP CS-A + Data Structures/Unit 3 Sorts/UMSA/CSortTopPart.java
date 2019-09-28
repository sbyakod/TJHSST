
import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;
import java.net.*; 

public class CSortTopPart extends Panel
{
	private SortApplet applet;
	
	//private final Font   m_fntCompanyFont = new Font("Helvetica", Font.BOLD, 12);
	private final Font   m_fntLabelFont   = new Font("Times New Roman", Font.PLAIN, 12);
	//private final String CompanyTitle = "Java Unlimited";                    
	private final String AlgorithmString = "Algorithm: ";
		
	//public Label m_lblCompanyName = new Label(CompanyTitle);
	public Label  m_lblAlgorithm      = new Label(AlgorithmString);										                          // Label for the grade
	//public Label  m_lblAnimation      = new Label(AnimationSpeedString);										                          // Label for the grade
	public Choice m_cboAlgorithm      = new Choice();									
	public Label  m_lblNoElements     = new Label("Number of elements: ");
	public TextField  m_txtNoElements = new TextField("100", 5);
	public Label  m_lblArrayOrder     = new Label("Array order: ");
	public Choice m_cboArrayOrder     = new Choice();
		
	
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
	
	private Font smallFont = new Font("Arial", Font.PLAIN, 10); 
	public Button m_btnHelp = new Button("Help"); 

	public CSortTopPart(SortApplet parent)
	{
		applet = parent;
		
		loadAlgorithms();
		loadArrayOrder();
		
		//m_lblCompanyName.setFont(m_fntCompanyFont);
		
		//m_lblAlgorithm.setFont(m_fntLabelFont); 
		//m_lblAlgorithm.setAlignment(Label.LEFT);
		
		//m_lblAnimation.setFont(m_fntLabelFont);
		//m_lblAnimation.setAlignment(Label.LEFT);
			  
		setLayout();
	}


   //Sets up the layout for this panel.  The layout is based on the
   //GridBag which is the most flexible of the current Java Layout managers.
	public void setLayout()
	{
		//Gonna use a grid bag layout to set positions as precisely as possible
		GridBagLayout       gbl = new GridBagLayout();
		GridBagConstraints  gbc = new GridBagConstraints();
		setLayout(gbl);
		
		buildConstraints(gbc, 0, 0, 1, 1, 5, 0);
		gbc.anchor     = GridBagConstraints.WEST;
		gbc.fill       = GridBagConstraints.NONE;
		gbc.ipadx      = 0;
		gbl.setConstraints(m_lblAlgorithm, gbc);
		add(m_lblAlgorithm);

		buildConstraints(gbc, 1, 0, 1, 1, 5, 0);
		gbc.anchor     = GridBagConstraints.WEST;
		gbc.fill       = GridBagConstraints.NONE;
		gbc.ipadx      = 0;
		gbl.setConstraints(m_cboAlgorithm, gbc);
		add(m_cboAlgorithm);

		buildConstraints(gbc, 2, 0, 1, 1, 5, 0);
		gbc.anchor     = GridBagConstraints.WEST;
		gbc.fill       = GridBagConstraints.NONE;
		gbc.ipadx      = 0;		
		gbl.setConstraints(m_lblNoElements, gbc);
		add(m_lblNoElements);
				
		buildConstraints(gbc, 3, 0, 1, 1, 5, 0);
		gbc.anchor     = GridBagConstraints.WEST;
		gbc.fill       = GridBagConstraints.NONE;
		gbc.ipadx      = 0;
		gbl.setConstraints(m_txtNoElements, gbc);
		add(m_txtNoElements);
	
		buildConstraints(gbc, 4, 0, 1, 1, 1, 0);
		gbc.anchor     = GridBagConstraints.NORTH;
		gbc.fill       = GridBagConstraints.NONE;
		gbc.ipadx      = 0;
		gbc.ipady      = 5;
		Label label1 = new Label("(max. 1000000)");
		label1.setFont(smallFont);
		gbl.setConstraints(label1, gbc);
		add(label1);
		

		buildConstraints(gbc, 5, 0, 1, 1, 5, 0);
		gbc.anchor     = GridBagConstraints.NORTH;
		gbc.fill       = GridBagConstraints.NONE;
		gbc.ipadx      = 0;
		gbl.setConstraints(m_lblArrayOrder, gbc);
		add(m_lblArrayOrder);

		buildConstraints(gbc, 6, 0, 1, 1, 15, 0);
		gbc.anchor     = GridBagConstraints.WEST;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_cboArrayOrder, gbc);
		add(m_cboArrayOrder);

		buildConstraints(gbc, 7, 0, 1, 1, 59, 0);
		gbc.anchor     = GridBagConstraints.CENTER;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_btnHelp, gbc);
		add(m_btnHelp);


		m_txtNoElements.addKeyListener(new KeyPressed());
		m_cboAlgorithm.addItemListener(new AlgorithmChange());
		//m_btnHelp.addActionListener(new HelpButton()); 
	}

	private void loadAlgorithms()
	{
		m_cboAlgorithm.insert("Bubble sort", BUBBLE_SORT_ID);
		m_cboAlgorithm.insert("Bubble sort w/flag", BUBBLE_SORT_WFLAG_ID);
		m_cboAlgorithm.insert("Insertion sort", INSERTION_SORT_ID);
		m_cboAlgorithm.insert("Selection sort", SELECTION_SORT_ID);
		m_cboAlgorithm.insert("Shell sort", SHELL_SORT_ID);
		m_cboAlgorithm.insert("Heap sort", HEAP_SORT_ID);
		m_cboAlgorithm.insert("Quick sort", QUICK_SORT_ID);
		
	}
	private void loadArrayOrder()
	{
		m_cboArrayOrder.insert("Random", RANDOM_ID);
		m_cboArrayOrder.insert("Ascending", ASCENDING_ID);
		m_cboArrayOrder.insert("Descending", DESCENDING_ID);		
	}
	
	
	/**
	 * The standard component paint method.  It displays the current problem
	 * tracker with list boxes and grade in updated condion
	 * @param g the graphics context on which to display
	 */
	public void paint(Graphics g) {}
	
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
	
	public class AlgorithmChange implements ItemListener
    {		
		public void itemStateChanged(ItemEvent e)
		{
			if(applet != null)
				applet.algorithmChange(m_cboAlgorithm.getSelectedIndex());
		}
    }

	public class FocusChanged implements FocusListener
	{
		public void focusGained(FocusEvent e){}
		public void focusLost(FocusEvent e)
		{
			if (applet != null)
				applet.CheckElementsText(); 
		}
	}
	public class KeyPressed implements KeyListener
	{
		public void keyTyped(KeyEvent e){}
		public void keyPressed(KeyEvent e)
		{
			if (e.getKeyCode() == e.VK_BACK_SPACE || 
				e.getKeyCode() == e.VK_DELETE ||
				e.getKeyCode() == e.VK_LEFT ||
				e.getKeyCode() == e.VK_RIGHT)
				return;
			switch (e.getKeyChar())
			{
				case '0':
				case '1':
				case '2':
				case '3':
				case '4':
				case '5':
				case '6':
				case '7':
				case '8':
				case '9':				
					break;
				default:
					e.consume();
					break;
			}	
		
		}
		public void keyReleased(KeyEvent e){}
	}
	public class HelpButton implements ActionListener
	{
		public void actionPerformed(ActionEvent e)
		{
			URL link = applet.getDocumentBase();

			String helpDir   = "help";
			String helpFile  = "/help.htm";
			
			String host = link.getHost();
			String appDir = link.getFile();
			String rootDir;
      
			// Strip the file to get the directory
			
			int i = appDir.lastIndexOf("/");
			appDir = appDir.substring(0, i+1);
      
			/*
			i = appDir.substring(0, appDir.length() - 1).lastIndexOf("/");
			if(i == -1)
				rootDir = appDir;
			else
				rootDir = appDir.substring(0, i+1);
			*/
			String helpLoc = appDir + helpDir + helpFile;
			try
			{
				openHelp(helpLoc);
			}
			catch (IOException err)
			{}
			
		}
	}
	public void openHelp(String helpLoc) throws IOException
	{
		// Url for the help file
		URL location;
		
		boolean NETWORK = true;
		
		//String HOST = "localhost";
		
		String HOST = applet.help_location;
		//String HOST = "www.umich.edu";
		String PROTOCOL = "http";

		if (NETWORK)
		{
			location = new URL(PROTOCOL, HOST, helpLoc); // Create a URL to the CGI script
			applet.getAppletContext().showDocument(location, "_blank");	// Show help in a new window
		}
	}
}
