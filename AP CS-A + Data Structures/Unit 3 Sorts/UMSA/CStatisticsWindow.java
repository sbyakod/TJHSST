import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;

public class CStatisticsWindow extends Panel
{
	public Label m_lblTimeElapsed = new Label("Time elapsed (ms):");
	public TextField m_txtTimeElapsed = new TextField(5);
	public Label m_lblNoExchanges = new Label("# of Exchanges:");
	public TextField m_txtNoExchanges = new TextField(5);
	public Label m_lblNoComparisons = new Label("# of Comparisons:");
	public TextField m_txtNoComparisons = new TextField(5);
	
	private Label label1 = new Label("ms");
	
	private SortApplet applet;
		
	public CStatisticsWindow(SortApplet parent)
	{		
		applet = parent;
		
		m_txtTimeElapsed.setEnabled(false);
		m_txtNoExchanges.setEnabled (false);
		m_txtNoComparisons.setEnabled (false);
		
		setLayout();		
	}


   /**
    * Sets up the layout for this panel.  The layout is based on the
    * GridBag which is the most flexible of the current Java Layout managers.
    */
   public void setLayout()
   {
      //Gonna use a grid bag layout to set positions as precisely as possible
      
	  GridBagLayout       gbl = new GridBagLayout();
      GridBagConstraints  gbc = new GridBagConstraints();
      setLayout(gbl);

      //gbc.insets     = new Insets(5, 0, 5, 0);
	  buildConstraints(gbc, 0, 0, 1, 1, 5, 10);
	  m_lblTimeElapsed.setAlignment (Label.RIGHT);
      //gbc.anchor     = GridBagConstraints.EAST;
      //gbc.fill       = GridBagConstraints.BOTH ;
      gbl.setConstraints(m_lblTimeElapsed, gbc);
      add(m_lblTimeElapsed);

	  buildConstraints(gbc, 1, 0, 1, 1, 95, 0);
      gbc.anchor     = GridBagConstraints.NORTHWEST  ;
      gbc.fill       = GridBagConstraints.NONE;
      gbl.setConstraints(m_txtTimeElapsed, gbc);
      add(m_txtTimeElapsed);

	  buildConstraints(gbc, 0, 1, 1, 1, 0, 10);
	  m_lblNoExchanges.setAlignment (Label.RIGHT);
      //gbc.anchor     = GridBagConstraints.NORTHEAST ;
      //gbc.fill       = GridBagConstraints.NONE;
      gbl.setConstraints(m_lblNoExchanges, gbc);
      add(m_lblNoExchanges);

	  buildConstraints(gbc, 1, 1, 1, 1, 0, 0);
      gbc.anchor     = GridBagConstraints.NORTHWEST;
      gbc.fill       = GridBagConstraints.NONE;
      gbl.setConstraints(m_txtNoExchanges, gbc);
      add(m_txtNoExchanges);
		
	  
	  buildConstraints(gbc, 0, 2, 1, 1, 0, 80);
	  m_lblNoComparisons.setAlignment (Label.RIGHT);
      //gbc.anchor     = GridBagConstraints.EAST;
      //gbc.fill       = GridBagConstraints.NONE;
      gbl.setConstraints(m_lblNoComparisons, gbc);
      add(m_lblNoComparisons);

	  
	  buildConstraints(gbc, 1, 2, 1, 1, 0, 0);
      gbc.anchor     = GridBagConstraints.NORTHWEST;
      gbc.fill       = GridBagConstraints.NONE ;
      gbl.setConstraints(m_txtNoComparisons, gbc);
      add(m_txtNoComparisons);
	  
	  ResetInfo();
	  
	  

   }

	
	/**
	 * The standard component paint method.  It displays the current problem
	 * tracker with list boxes and grade in updated condion
	 * @param g the graphics context on which to display
	 */
	public void paint(Graphics g) 
	{
		//g.drawRect(0, 0, size().width - 1 , size().height - 1);
		
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
	private void ResetInfo()
	{
		m_txtTimeElapsed.setText("0");
		m_txtNoExchanges.setText("0");
		m_txtNoComparisons.setText("0");
		
	}
}

