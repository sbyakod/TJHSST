import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;

//We use this class to store information about graphical represantation
//of the array of numbers

class Node
{
	double x, y;
	String lbl;
	Color col;
}

public class CSortAnimator extends Panel	
{
	private final int ANIMATE_BUTTONS_CONST = 1000;
	
	public final int RESET = ANIMATE_BUTTONS_CONST + 0;
	public final int START = ANIMATE_BUTTONS_CONST + 1;
	
	public final int MAX_NUMBER_ELEMENTS = 100;

	private SortApplet applet;
	
	public Button m_btnReset = new Button("Reset");
	public Button m_btnStart = new Button("Start");
	public Label m_lblAnimationSpeed = new Label("Speed: ");
	public Choice m_cboAnimationSpeed = new Choice(); 
	public Checkbox m_chkAnimation = new Checkbox("Show animation (max. 100 elements)", true);
	public Button m_btnStatistics = new Button("Statistics");
	
	public CAnimatedPanel m_drawArea = new CAnimatedPanel(this);
	
	private final int NODE_WIDTH  = 35;
	private final int NODE_HEIGHT = 15;
	
	private int m_NodesUsed;//Contains information about the number
							//of nodes in use by the current algorithm
	
	Node m_Nodes[] = new Node[100];
	
	private int m_animationSpeed;//Contains information about which animation
							     //speed the user has chosen		
	
	public final int INSTANT_ANIMATION = 0;
	public final int FAST_ANIMATION    = 1;
	public final int MEDIUM_ANIMATION  = 2;
	public final int SLOW_ANIMATION    = 3;
	
	public static final int INSTANT_ID			 = 0;
	public static final int FAST_ID				 = 1;
	public static final int MEDIUM_ID			 = 2;
	public static final int SLOW_ID				 = 3;

	private final int LEFT_EDGE = 18;//Defines the leftmost position
									 //a node can hold
	private int right_edge;			 //Right most position
	private final int OFFSET = 20;	 //Horizontal offset to center
									 //the nodes on the screen	
	private final int V_OFFSET = 15; //Vertical offset to center
									 //the nodes on the screen
	private final int MOVE_DISTANCE = 5;//Defines the number of pixels
	//the nodes are moved during animation
	
	private final int V_DISTANCE = 15;//Since the y coordinate marks
	//the center of the node to move a node to the empty row you only
	//need to move it by NODE_HEIGHT/2
	
	private int move_speed = 1;//Used as a modifier for MOVE_DISTANCE
								//to permit faster move for longer distances
	
	//The next line creates the font to be used for the label of the node
	private Font LabelFont = new Font("Courier", Font.PLAIN, 12);
	//The next line creates the font to be used for the index of the node
	private Font IndexFont = new Font("Arial", Font.PLAIN, 8);
	
	private final static int INSTANT_DELAY = 50;  // Delay for instant animation
	private final static int FAST_DELAY    = 100; // Delay for fast animation
	private final static int MEDIUM_DELAY  = 200; // Delay for medium animation
	private final static int SLOW_DELAY    = 300; // Delay for slow animation
	
	public final Color COMPARE_COLOR = Color.red;//Color of the elements being compared
	public final Color SORTED_COLOR  = Color.lightGray;//Color of the elements that are already sorted
	
	public CSortAnimator(SortApplet parent)
	{
		
		applet = parent;
		
		loadAnimationSpeed();
		
		GridBagLayout       gbl = new GridBagLayout();
		GridBagConstraints  gbc = new GridBagConstraints();
		setLayout(gbl);

		
		buildConstraints(gbc, 0, 0, 6, 1, 0, 95);
		gbc.fill       = GridBagConstraints.BOTH;
		gbl.setConstraints(m_drawArea, gbc);
		add(m_drawArea);
		
		buildConstraints(gbc, 0, 1, 1, 1, 8, 5);
		gbc.anchor = GridBagConstraints.WEST;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_btnReset, gbc);
		add(m_btnReset);
		
		buildConstraints(gbc, 1, 1, 1, 1, 8, 0);
		gbc.anchor = GridBagConstraints.WEST;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_btnStart, gbc);
		add(m_btnStart);

		buildConstraints(gbc, 2, 1, 1, 1, 10, 0);
		gbc.anchor = GridBagConstraints.EAST;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_lblAnimationSpeed, gbc);
		add(m_lblAnimationSpeed);

		buildConstraints(gbc, 3, 1, 1, 1, 5, 0);
		gbc.anchor = GridBagConstraints.CENTER;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_cboAnimationSpeed, gbc);
		add(m_cboAnimationSpeed);       
       
		buildConstraints(gbc, 4, 1, 1, 1, 10, 0);
		gbc.anchor = GridBagConstraints.EAST;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_chkAnimation, gbc);
		add(m_chkAnimation);       
	   
		buildConstraints(gbc, 5, 1, 1, 1, 59, 0);
		gbc.anchor = GridBagConstraints.WEST;
		gbc.fill       = GridBagConstraints.NONE;
		gbl.setConstraints(m_btnStatistics, gbc);
		add(m_btnStatistics);  
		
		m_btnReset.addActionListener(new ResetClick());
		m_btnStart.addActionListener(new StartClick());
		m_btnStatistics.addActionListener(new StatisticsClick());
		
		m_cboAnimationSpeed.addItemListener(new AnimationSpeedChange());
		m_chkAnimation.addItemListener(new ShowAnimationChange());
	}
	
	private void loadAnimationSpeed()
	{
		m_cboAnimationSpeed.addItem("Instantaneous");
		m_cboAnimationSpeed.addItem("Fast");
		m_cboAnimationSpeed.addItem("Medium");
		m_cboAnimationSpeed.addItem("Slow");
			
	}

	public void paint(Graphics g) {}
	
	//This function allows the creator of the applet interface to
	//set the animation speed variable to a value selected by the user
	
	public void SetAnimationSpeed(int speed)
	{
		m_animationSpeed = speed;
	}
	
	//This function takes an array of integers as input and uses 
	//that data to create nodes to show on the screen
	//After the nodes has been created it calls CreateImage to 
	//display those nodes on the screen
	
	public void DrawTable(int arr[])
	{
		int width, height, horizontal, vertical;
		width = getSize().width;
		height = getSize().height;
		horizontal = width/12;//Calculates space taken by one node
		vertical = height/22 - 2;//Need the -2 since nodes have some space by default
		right_edge = width - (NODE_WIDTH / 2) - 7;//The right most position a node can have
		
		m_NodesUsed = arr.length; 
		
		for (int i = 0; i < m_NodesUsed; i++)
		{
			Node n = new Node();//This line creates a new node
			//Next line assigns the label to the node based on the node's position 
			n.lbl = String.valueOf(arr[i]);
			//Next line sets the background color of the node
			n.col = Color.yellow;
			//Next line sets horizontal position of the node based
			//on its position in the array.
			//The code works under the assumption that there are ten
			//nodes in each row
			n.x = OFFSET + horizontal * ((i%10) + 1);
			
			//Next line sets vertical position of the node based
			//on its position in the array.
			//The code works under the assumption that there are ten
			//nodes in each row			
			n.y = V_OFFSET + vertical * ((i / 10) * 2 + 1);
			m_Nodes[i] = n;
		}
		CreateImage();//This function will draw the image
	}
	
	//This function displays the nodes described in the m_Nodes on the
	//screen
	private void CreateImage()
	{		
		int w, h, x, y;
		w = NODE_WIDTH;
		h = NODE_HEIGHT;
		String index;//used to put the array index in the lower left corner of the cell
	
		Initialize();//Creates white rectangle with black borders
				FontMetrics labelFM = getFontMetrics(LabelFont);
		FontMetrics indexFM = getFontMetrics(IndexFont);				//This loop draws nodes on the screen
		for(int i = 0; i < m_NodesUsed; i++)
		{
			x = (int)m_Nodes[i].x;
			y = (int)m_Nodes[i].y;			//Next line is used to show the position of the node in the array
			index = String.valueOf(i);			
			//creates a shorter name for graphics object
			Graphics g = m_drawArea.m_drawGraphics;
			
			//Sets the background color of the node			g.setColor(m_Nodes[i].col);			
			//Fill the rectangular area that represents a node with color
			//which is specified in the node's col field			g.fillRect(x - w/2, y - h / 2, w, h);
			
			//Next two lines are used to draw a black rectangle around 
			//the colored area of the node			g.setColor(Color.black);
			g.drawRect(x - w/2, y - h / 2, w, h);
			g.setFont(LabelFont);//Sets the font to be used for the label of the node			
			//The next line will draw the label of the node
			//(the label is the number that the node represents)
			//the label will be place in the center of the space
			//left in the nodes after placing the index			g.drawString(m_Nodes[i].lbl, x + indexFM.stringWidth(index) / 2
						- labelFM.stringWidth(m_Nodes[i].lbl) / 2,
						y + (labelFM.getAscent() / 2));			
			g.setFont(IndexFont);//Sets the font to be used for the array index			//The next line will draw the array index in the left bottom
			//corner of the node			g.drawString(index, x - w/2 + 1, y + h/2);
					}			m_drawArea.repaint(); 
	}
	
	
	//This function takes the m_animationSpeed variable and calculates
	//the corresponding sleep delay for the animation
	private int GetDelay()
	{
		int delay;
		switch (m_animationSpeed)
		{
			case INSTANT_ANIMATION:
				delay = INSTANT_DELAY;
				break;
			
			case FAST_ANIMATION:
				delay = FAST_DELAY;
				break;
			
			case MEDIUM_ANIMATION:
				delay = MEDIUM_DELAY;
				break;
			
			case SLOW_ANIMATION:
				delay = SLOW_DELAY;
				break;

			default:
				delay = INSTANT_DELAY;
				break;
		}
		
		return delay;
	}
	
	//This function will put the thread that has called it to sleep
	//to make sure that animation isn't too fast as to be unnoticeable 
	private void SleepThread()
	{
		Thread thread = Thread.currentThread(); 

		try
		{
			thread.sleep(GetDelay());
		}
		catch (InterruptedException err) {}
	}
	
	
	//Takes two integers(array indexes) and sets the background color
	//of those elements to red
	// NOTE: i & j must be valid!
	public void AnimateCompare(int i, int j)
	{					
		Color iCol, jCol;
		iCol = m_Nodes[i].col;
		jCol = m_Nodes[j].col;
		m_Nodes[i].col = COMPARE_COLOR;
		m_Nodes[j].col = COMPARE_COLOR;
		CreateImage();
		
		SleepThread();
		SleepThread();
		
		m_Nodes[i].col = iCol;
		m_Nodes[j].col = jCol;
		CreateImage();
	}
		
	//Takes two integers(array indexes) and sets the background color
	//of elements between those two positions to Col(passed as a parameter)
	// NOTE: i & j must be valid!
	public void ChangeColor(int i, int j, Color col)
	{
		for(int k = i; k <= j; k++)
			m_Nodes[k].col = col;
		CreateImage();
	}
	
	
	//This function takes two integers(array indexes) of the nodes
	//and two other integers as desired positions for the nodes
	//respectively
	
	private void MoveHorizontally_2(int i, double ix, int j, double jx)
	{
		boolean conditionI = true, conditionJ = true;
		int di, dj, distance = MOVE_DISTANCE * move_speed;
		if(m_animationSpeed == FAST_ANIMATION)
			distance = 2 * distance;
		
		if(m_Nodes[i].x < ix)
			di = distance;
		else
			di = -distance;
		if(m_Nodes[j].x < jx)
			dj = distance;
		else
			dj = -distance;
		
		//This loop is executed untill both nodes are in the place
		//specified in the parameters passed to the function
		
		while(conditionI || conditionJ)
		{
			//If the node is within move distance of the desired position
			//it will be moved to that position and the loop variable
			//for this node will be set to false
			//Otherwise the node will be moved by move distance and 
			//the loop will be executed again
			
			if(m_Nodes[i].x > (ix - distance) && m_Nodes[i].x < (ix + distance))
			{
				m_Nodes[i].x = ix;
				conditionI = false;
			}
			else
				m_Nodes[i].x = m_Nodes[i].x + di;
			
			//If the node is within move distance of desired position
			//it will be moved to that position and the loop variable
			//for this node will be set to false
			//Otherwise the node will be moved by move distance and 
			//the loop will be executed again

			if(m_Nodes[j].x > (jx - distance) && m_Nodes[j].x < (jx + distance))
			{
				m_Nodes[j].x = jx;
				conditionJ = false;
			}
			else
				m_Nodes[j].x = m_Nodes[j].x + dj;
			
			CreateImage();
			SleepThread();
		}		
	}
	
	
	//Takes one integer(array index) and moves that node to the 
	//desired coordinates along the x axis
	
	private void MoveHorizontally_1(int i, double ix)
	{
		boolean condition = true;
		int di, distance = MOVE_DISTANCE * move_speed;
		if(m_animationSpeed == FAST_ANIMATION)
			distance = 2 * distance;
		
		if(m_Nodes[i].x < ix)
			di = distance;
		else
			di = -distance;
		while(condition)
		{
			//If the node is within move distance of desired position
			//it will be moved to that position and the loop variable
			//will be set to false
			//Otherwise the node will be moved by move distance and 
			//the loop will be executed again

			if(m_Nodes[i].x > (ix - distance) && m_Nodes[i].x < (ix + distance))
			{
				m_Nodes[i].x = ix;
				condition = false;
			}
			else
				m_Nodes[i].x = m_Nodes[i].x + di;
			CreateImage();
			SleepThread();
		}
	}
	
	//Takes on integer as input(array index) and moves that node to 
	//the desired coordinates along the y axis
	
	private void MoveVertically_1(int i, double iy)
	{
		boolean condition = true;
		int di, distance = MOVE_DISTANCE * move_speed;

		if(m_animationSpeed == FAST_ANIMATION)
			distance = 2 * distance;
		
		if(m_Nodes[i].y < iy)
			di = distance;
		else
			di = -distance;
		while(condition)
		{
			//If the node is within move distance of desired position
			//it will be moved to that position and the loop variable
			//will be set to false
			//Otherwise the node will be moved by move distance and 
			//the loop will be executed again

			if(m_Nodes[i].y > (iy - distance) && m_Nodes[i].y < (iy + distance))
			{
				m_Nodes[i].y = iy;
				condition = false;
			}
			else
				m_Nodes[i].y = m_Nodes[i].y + di;
			CreateImage();
			SleepThread();
		}
	}
	
	//This function takes two integers(array indexes) and two more
	//integers as desired y positions for the nodes represented by
	//those indexes	
	
	private void MoveVertically_2(int i, double iy, int j, double jy)
	{
		boolean conditionI = true, conditionJ = true;
		int di, dj, distance = MOVE_DISTANCE * move_speed;
		
		if(m_animationSpeed == FAST_ANIMATION)
			distance = 2 * distance;
		if(m_Nodes[i].y < iy)
			di = distance;
		else
			di = -distance;
		if(m_Nodes[j].y < jy)
			dj = distance;
		else
			dj = -distance;
		while(conditionI || conditionJ)
		{
			//If the node is within move distance of desired position
			//it will be moved to that position and the loop variable
			//for this node will be set to false
			//Otherwise the node will be moved by move distance and 
			//the loop will be executed again

			if(m_Nodes[i].y > (iy - distance) && m_Nodes[i].y < (iy + distance))
			{
				m_Nodes[i].y = iy;
				conditionI = false;
			}
			else
				m_Nodes[i].y = m_Nodes[i].y + di;
			
			//If the node is within move distance of desired position
			//it will be moved to that position and the loop variable
			//for this node will be set to false
			//Otherwise the node will be moved by move distance and 
			//the loop will be executed again

			if(m_Nodes[j].y > (jy - distance) && m_Nodes[j].y < (jy + distance))
			{
				m_Nodes[j].y = jy;
				conditionJ = false;
			}
			else
				m_Nodes[j].y = m_Nodes[j].y + dj;
			
			CreateImage();
			SleepThread();
		}		
	}

	//This function will set the image assotiated with this panel to 
	//have a black outline and a white background
	
	public void Initialize()
	{		
		m_drawArea.Initialize();		
	}
		
	
	//This function will animate the swapping of the two elements
	//of the array. Depending on animation speed it will either move 
	//the nodes or change it instantly
	// NOTE: i & j must be valid!
	public void AnimateSwap(int i, int j)
	{
		String temp;
		Color iCol, jCol;
		iCol = m_Nodes[i].col;
		jCol = m_Nodes[j].col;
		
		if(i == j)
			return;
		if (m_animationSpeed != INSTANT_ANIMATION)
		{
			double ix, iy, jx, jy, vi, vj;
			ix = m_Nodes[i].x;
			jx = m_Nodes[j].x;
			iy = m_Nodes[i].y;
			jy = m_Nodes[j].y;
			
			m_Nodes[i].col = COMPARE_COLOR;
			m_Nodes[j].col = COMPARE_COLOR;
			
			// Move the cell that is higher on the screen up and the cell
			//that is lower on the screen down
			if(iy <= jy)
			{
				vi = -V_DISTANCE;
				vj = V_DISTANCE;
			}
			else
			{
				vi = V_DISTANCE;
				vj = -V_DISTANCE;
			}
			MoveVertically_2(i, iy + vi, j, jy + vj);
			if(iy == jy)
				MoveHorizontally_2(i, jx, j, ix);
			else
			{
				move_speed = 2;//If the element has to be moved further it will move faster
				MoveHorizontally_2(i, LEFT_EDGE, j, right_edge);
				MoveVertically_2(i, jy - vi, j, iy - vj);
				MoveHorizontally_2(i, jx, j, ix);
				move_speed = 1;
			}
			MoveVertically_2(i, jy, j, iy);
			
			//Return the nodes to the previous positions and swap labels
			//Need to do this in order to keep the nodes in the same
			//order as the array
			
			m_Nodes[i].x = ix;
			m_Nodes[j].x = jx;
			m_Nodes[i].y = iy;
			m_Nodes[j].y = jy;
		}
		
		temp = m_Nodes[i].lbl;
		m_Nodes[i].lbl = m_Nodes[j].lbl;
		m_Nodes[j].lbl = temp;
			
		if (m_animationSpeed != INSTANT_ANIMATION)
		{
			CreateImage();
			SleepThread();
		}
		m_Nodes[i].col = iCol;
		m_Nodes[j].col = jCol;
	}
	
	
	//Node i will be moved to the position held by j all the nodes will
	//be moved to free space for i
	// NOTE: i & j must be valid!
	public void AnimateInsert(int i, int j)
	{
		double ix, iy, jx, jy;
		String temp;
		ix = m_Nodes[i].x;
		iy = m_Nodes[i].y;
		jx = m_Nodes[j].x;
		jy = m_Nodes[j].y;

		if(i == j)
			return;
		if(m_animationSpeed == INSTANT_ANIMATION)
			m_Nodes[i].y = m_Nodes[i].y - V_DISTANCE;
		else
			MoveVertically_1(i, iy - V_DISTANCE);
		
		temp = m_Nodes[i].lbl;
		
		//Shuffle the nodes to make space for the node to be inserted
		if(i < j)
			for(int k = i; k < j; k++)
				m_Nodes[k].lbl = m_Nodes[k+1].lbl;
		if(i > j)
			for(int k = i; k > j; k--)
				m_Nodes[k].lbl = m_Nodes[k-1].lbl;

		m_Nodes[j].x = m_Nodes[i].x;
		m_Nodes[j].y = m_Nodes[i].y;
		m_Nodes[j].lbl = temp;
		m_Nodes[i].x = ix;
		m_Nodes[i].y = iy;
		
		if(m_animationSpeed == INSTANT_ANIMATION)
		{
			m_Nodes[j].x = jx;
			m_Nodes[j].y = jy;
		}
		else
		{
			if(m_Nodes[j].y + V_DISTANCE == jy)
			{
				MoveHorizontally_1(j, jx);
				MoveVertically_1(j, jy);
			}
			else
			{
				move_speed = 2;//Move faster if needs to move farther
				MoveHorizontally_1(j, right_edge);
				MoveVertically_1(j, jy - V_DISTANCE);
				MoveHorizontally_1(j, jx);
				MoveVertically_1(j, jy);
				move_speed = 1;
			}
		}
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
	
	// Handles 'Reset' button clicking
    public class ResetClick implements ActionListener
    {
       public void actionPerformed(ActionEvent e)
       {
		  applet.animationPanelBtnClick(RESET);
       }
    }

	// Handles 'Start' button clicking
    public class StartClick implements ActionListener
    {
       public void actionPerformed(ActionEvent e)
       {
		  applet.animationPanelBtnClick(START);
       }
    }

	// Handles 'Statistics' button clicking
	public class StatisticsClick implements ActionListener
    {		
		public void actionPerformed(ActionEvent e)
		{
			m_drawArea.ShowStatistics();
		}
    }

	// Handles change in animation speed
	public class AnimationSpeedChange implements ItemListener
    {		
		public void itemStateChanged(ItemEvent e)
		{
			applet.animationChange(m_cboAnimationSpeed.getSelectedIndex());
		}
    }

	// Handles show animation state
	public class ShowAnimationChange implements ItemListener
    {		
		public void itemStateChanged(ItemEvent e)
		{
			applet.showAnimationChange(m_chkAnimation.getState());
		}
    }
}
