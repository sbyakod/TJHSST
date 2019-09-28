 	//written by Ria - November 2014  
	
	import java.awt.*;
   import javax.swing.JFrame;
   public class AppletFrame extends JFrame {
      public static void main(String[] args) {
         SortApplet myApplet = new SortApplet(); // define applet of interest
         JFrame myFrame = new JFrame("Sorting Animations from the University of Michigan Computer and Information Science Department"); // create frame with title
      // Call applet's init method (since Java App does not call it as a browser automatically does)
			myApplet.init();	
      // add applet to the frame
         myFrame.add(myApplet, BorderLayout.CENTER);
         myFrame.pack(); // set window to appropriate size (for its elements)
         myFrame.setVisible(true); // usual step to make frame visible
         myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      } // end main
   } // end class