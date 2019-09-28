import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;

//this class creates bar chart
public class CGraph
{
	private CAnimatedPanel panel; // Animated panel object
	private Image m_drawImage;    // Image object
	private Graphics g;           // Graphics
	
	//initialize fonts
	private Font f1 = new Font("Helvetica", Font.BOLD, 14);//font for the title
	private Font f2 = new Font("Helvetica", Font.PLAIN, 12);//regular font
	private Font f3 = new Font("Helvetica", Font.PLAIN, 10);//small font
	
	//initialize array of colors for maximum of 5 bars
	private final Color colors[] = {Color.red, Color.blue, Color.green, Color.magenta, Color.orange};
	
	//initialize applet
	//Input: CAnimatedPanel
	public CGraph(CAnimatedPanel parent)
	{
		panel = parent;
	}
	
	//for y values convert double to int if needed
	//multiply by 1000 to keep 3 numbers after decimal point
	//Input: double y[], boolean y_int_flag
	private int[] Convert_To_Int(double y[], boolean y_int_flag)
	{	
		int y_data_set[] = new int[y.length];//create array
		if(y_int_flag == false)
			for(int i = 0; i < y.length; i++)
				y_data_set[i] = (int)(y[i] * 1000);
		else
			for(int i = 0; i < y.length; i++)
				y_data_set[i] = (int)y[i];					
		return y_data_set;
	}//end of function Convert_To_Int
	
	//this function finds index of the maximum value in the array
	//Input: double y[]
	//Output: max_index
	private int Find_Max_Index(double y[])
	{
		int max_index = 0; 
		for(int i = 0; i < y.length; i++)
		{
			if(y[i] > y[max_index])
				max_index = i;
		}
        //end of the loop for findindg the y max index  
		return max_index;
	}//End of function Find_Max_Index
	
	//this function sorts array x, y_data_set array, and vector algName accordingly 
	//using bubble sort
	//Input: Vector algName, int x[], int y_data_set[]
	private void Sort_Arrays(Vector algName, int x[], int y_data_set[])
	{
	  int i = x.length;//set i to the size of the arrays
	  while(--i >= 0)
	  {
		  for(int j = 0; j < i; j++)
		  {
			  if(x[j] > x[j+1])
				{
					//swap x array values values
					int temp_int = x[j];
					x[j] = x[j+1];
					x[j+1] = temp_int;
					
					//swap y_data_set array values values
					temp_int = y_data_set[j];
					y_data_set[j] = y_data_set[j+1];
					y_data_set[j+1] = temp_int;
	                
					//swap elements of the vector
					String temp_string = (algName.elementAt(j)).toString();
					algName.setElementAt(algName.elementAt(j+1), j);
					algName.setElementAt(temp_string, j+1);
				}
		  }
	  }//end of while loop for sorting arrays and vectors
	}//end of function Sort_Arrays
	
	
	//this function calculates sizes and start indeces of all bar groups
	//Input: int group_size[], int group_start[], int x[]
	private void Find_Size_Start(int group_size[], int group_start[], int x[])
	{
		for(int i = 0; i < x.length; i++)
			for(int j = 0; j < x.length; j++)
				if(x[i] == x[j])
					group_size[i]++;
		//calculate the positions of bars in the groups			
		for(int i = 0; i < x.length; i++)
			for(int j = 0; j < x.length; j++)
				if(x[i] == x[j])
				{
					group_start[i] = j;
		            break;
				}
	}//End of Find_SIze_Start function
	
	
	//This function draws all the componets of the graph on the applet.
	//It also controls all other functions in the class
	//Input: int x[], double y[], boolean y_int_flag, Vector algName, String x_label, String y_label
	//Output: Bar Chart on the applet
	public void DrawGraph(int x[], double y[], boolean y_int_flag, Vector algName, String x_label, String y_label)
	{
		// Blank screen!
		panel.Initialize(); 
		
		// Image object
		m_drawImage = panel.m_drawImage;
		// Graphics object
	 	g = m_drawImage.getGraphics(); 
		
		int width = panel.getSize().width - panel.getSize().width%20;//find the available width 
        int height = panel.getSize().height - panel.getSize().height%20;//find the available height
 		int Graph_y_offset = height/4; //graph y offset from origin
		int Graph_Height = height/2;//find the Graph Height
		int Y_Axis_Divisions = 4;//define the number of y axis divisions
		int Y_Tick_Height = Graph_Height/Y_Axis_Divisions;//find the y tick height
		int Graph_x_offset = 80;//width/2 - 20; //graph x offset from origin
		int Graph_Width = width/2;//find the Graph Width
		int X_Tick_Width = Graph_Width/20;//find the x tick width
		String tick_value;//temp tick value		
		int char_num = 0;//number of chars to be printed
		char chars[] = y_label.toCharArray();//char array for y axis units
		
		int y_data_set[] = Convert_To_Int(y, y_int_flag);//convert double to int for drawing
		
		int y_data_set_max = y_data_set[Find_Max_Index(y)];//find maximum for y axis values
		double y_max = y[Find_Max_Index(y)];//find maximum for y axis drawing values
				
		//scaling process for y_data_set
		for(int i = 0; i < y_data_set.length; i++)
		{
			if (y_data_set_max != 0)
				y_data_set[i] = 100 * y_data_set[i] / y_data_set_max;
			else
				y_data_set[i] = 100 * y_data_set[i];
		}//end of the loop for reloading the y_data_set
		
		//draw title
		g.setColor(Color.black);
		g.setFont(f1);//set bigger font
		FontMetrics fm = g.getFontMetrics();//set the font metrics
		g.drawString(x_label + " vs. " + y_label, width/2 - fm.stringWidth(y_label + " vs. " + x_label)/2, 30);
		g.setFont(f2);//back to normal font
		
		//draw y axis
		g.drawLine(Graph_x_offset, Graph_y_offset - 10, Graph_x_offset, Graph_y_offset + Graph_Height + 5);
		
		//draw y axis units by drawing chars one by one
		fm = g.getFontMetrics();//set font metrics		
		for(int i=0; i<y_label.length(); i++)
			g.drawChars(chars,i,1,Graph_x_offset - 70 - fm.charsWidth(chars,i,1)/2,Graph_y_offset + Graph_Height/2 - 12*(y_label.length()/2-i));
				
		//check what the type of y label is (int or double) then draw y-tick labels	
		if (y_data_set_max != 0)
		{
			for(int i=0; i<=Y_Axis_Divisions; i++)
				if(y_int_flag == true)//if integers draw strings
					g.drawString(String.valueOf(i * y_data_set_max/Y_Axis_Divisions), 
							 Graph_x_offset - 5 - String.valueOf(i * y_data_set_max/Y_Axis_Divisions).length()*7,
							 Graph_y_offset + Graph_Height -(i*Y_Tick_Height) + 4);
				else//if doubles cut off insignificant digits to fit the chart then draw strings
				{
					tick_value = String.valueOf(i * y_max/Y_Axis_Divisions);
					switch(String.valueOf(i * y_max/Y_Axis_Divisions).length() - String.valueOf(Math.round(i * y_max/Y_Axis_Divisions)).length())
					{
					case 0: char_num = String.valueOf(Math.round(i * y_max/Y_Axis_Divisions)).length();
							break;
					case 1: char_num = String.valueOf(Math.round(i * y_max/Y_Axis_Divisions)).length() + 1;
							break;
					case 2:	char_num = String.valueOf(Math.round(i * y_max/Y_Axis_Divisions)).length() + 2;
							break;
					case 3:	char_num = String.valueOf(Math.round(i * y_max/Y_Axis_Divisions)).length() + 3;
							break;
					default: char_num = String.valueOf(Math.round(i * y_max/Y_Axis_Divisions)).length() + 4;
							break;
					}
					tick_value = tick_value.substring(0, char_num);
					g.drawString(tick_value, Graph_x_offset - 5 - tick_value.length()*7, Graph_y_offset + Graph_Height -(i*Y_Tick_Height) + 4);
				}//end of the loop for drawing the y axis tick values
		}
		else
			g.drawString(String.valueOf(0), Graph_x_offset - 12, Graph_y_offset + Graph_Height + 4);
		
		//draw horizontal grid lines and y ticks
		for(int i=0; i<=Y_Axis_Divisions; i++)
			g.drawLine(Graph_x_offset - 5, Graph_y_offset + Graph_Height -(i*Y_Tick_Height),
					   Graph_x_offset + Graph_Width, Graph_y_offset + Graph_Height -(i*Y_Tick_Height));
		
		//draw x axis
		g.drawLine(Graph_x_offset, Graph_y_offset + Graph_Height, Graph_x_offset + Graph_Width, Graph_y_offset + Graph_Height);
		
		//sort arrays x, y, and vector algName based on array x
		Sort_Arrays(algName, x, y_data_set);
				
		//find the number of X Axis Divisions
		int X_Axis_Divisions = x.length;//define the number of x axis divisions
		for(int i = 0; i < x.length - 1; i++)
			if(x[i] == x[i+1])
				X_Axis_Divisions--;
		
		//draw x-tick lables and lines
		for(int i=0, temp = -1, removed = 0; i < x.length; temp = x[i], i++)
			if(x[i] != temp)
			{
				//draw x-tick labels
				g.drawString(String.valueOf(x[i]),	 
				            (Graph_x_offset + (i-removed+1) * Graph_Width / (X_Axis_Divisions+1) - fm.stringWidth(String.valueOf(x[i]))/2),
						     Graph_y_offset + Graph_Height + 16);
			    
				//draw x-tick lines
				g.drawLine(Graph_x_offset + (i-removed+1) * Graph_Width / (X_Axis_Divisions+1), Graph_y_offset + Graph_Height, 
						   Graph_x_offset + (i-removed+1) * Graph_Width / (X_Axis_Divisions+1),	Graph_y_offset + Graph_Height + 5);
			}
			else
				removed++;//increment counter of the ticks that are not printed
					
		//draw x axis unit label
		g.drawString(x_label, Graph_x_offset + Graph_Width/2 - fm.stringWidth(x_label)/2, Graph_y_offset + Graph_Height + 35);
		
		//calculate the sizes and start indeces of the bar groups 
		int group_size[] = {0,0,0,0,0};		//initialize how many in the group 
		int group_start[] = {0,0,0,0,0};	//where the group starts
		Find_Size_Start(group_size, group_start, x);
			
		//draw data bars
		for(int i=0, removed = 0; i < x.length; i++)
		{
			g.setColor(colors[i]);	
			if(group_size[i] == 1)
				g.fillRect(Graph_x_offset + (i-removed+1) * Graph_Width / (X_Axis_Divisions+1) - X_Tick_Width/2,
					   Graph_y_offset + Graph_Height - (y_data_set[i]+1) * Graph_Height / 100,
					   X_Tick_Width, (y_data_set[i]+1) * Graph_Height / 100);
			else 
			{
				
				g.fillRect(Graph_x_offset + (i-removed+1) * Graph_Width / (X_Axis_Divisions+1) - 
						   (X_Tick_Width*group_size[i])/2 + (i-group_start[i]) * X_Tick_Width,
							Graph_y_offset + Graph_Height - (y_data_set[i]+1) * Graph_Height / 100,
							X_Tick_Width, (y_data_set[i]+1) * Graph_Height / 100);
				if(group_start[i] + group_size[i] != i+1)
					removed++;//increment number of bars that are not drawn one at a tick
			}			
		}// end of the loop for drawing the bars
		
		//draw legend
		g.setColor(Color.black);
		g.drawString("Legend:", Graph_x_offset + Graph_Width + 20, Graph_y_offset);
		g.setFont(f3);
		for(int i=0; i < algName.size(); i++)
		{
			g.setColor(colors[i]);
			g.fillRect(Graph_x_offset + Graph_Width + 20, Graph_y_offset + (i+1)*16, 12, 12);
			g.setColor(Color.black);
			g.drawString(algName.elementAt(i).toString(), Graph_x_offset + Graph_Width + 35, Graph_y_offset + (i+1)*16 + 12);
		}//end of the loop for drawing the legend
		
	    panel.repaint(); 
	}//end of public void DrawGraph
}//end of public class CGraph