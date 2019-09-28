
import java.awt.*;
//import CSortAlgorithm.*;

public class RunThread extends Thread
{
	private SortApplet applet;
	private CSortAlgorithm m_currAlg;
	private int m_nElements;
	private int m_arrType;
	
	public RunThread(SortApplet parent, int n, int arrType)
	{
		applet = parent;
		m_nElements = n;
		m_arrType = arrType;
		this.setPriority(this.MIN_PRIORITY); 
	}
	
	public void run()
	{
		if (m_currAlg != null)
			m_currAlg.sort(m_nElements, m_arrType); 
		applet.FinishedAlgorithm(); 
	}
	
	public void SetCurrentAlg(CSortAlgorithm alg)
	{
		m_currAlg = alg;
	}	
}
