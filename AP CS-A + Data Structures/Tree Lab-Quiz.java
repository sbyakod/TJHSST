// TreesEqual
// TreeToString
// DropLeaves
// CutBranches
// FillTheTree
// CountBranchesWithEvens
// DoublePositivesInts
//
// Extra: trim

/* Write a method equals that could be added to the IntTree class. The method 
 * accepts another binary tree of integers as a parameter and compares the two 
 * trees to see if they are equal to each other. Two trees are considered 
 * equal if they have exactly the same structure and store the same values. 
 * Each node in one tree must have a corresponding node in the other tree in 
 * the same location relative to the root and storing the same value. Two 
 * empty trees are considered equal to each other.
 */
import java.util.*;

public class Tree Lab-Quiz
{
   public static void main(String[] args)
   {
   
   
   
public boolean equals2(IntTree t2) {
    return equals2(overallRoot, t2.overallRoot);
}

private boolean equals2(IntTreeNode n1, IntTreeNode n2) {
    if(n1 == null && n2 == null)
        return true;
        
    if(n1 == null && n2 != null)
        return false;
        
    if(n1 != null && n2 == null)
        return false;
        
    return n1.data == n2.data && equals2(n1.left, n2.left) &&
        equals2(n1.right, n2.right);
}

/* Write a method toString2 for a binary tree of integers. The method should 
 * return "empty" for an empty tree. For a leaf node, it should return the 
 * data in the node as a String. For a branch node, it should return a 
 * parenthesized String that has three elements separated by commas:
 *
 * The data at the root.
 * A String representation of the left subtree.
 * A String representation of the right subtree.
 */
public String toString2() {
    return toString2(overallRoot);
}

private String toString2(IntTreeNode node) {
    if(node == null)
        return "empty";
        
    if(node.left == null && node.right == null)
        return String.valueOf(node.data);
        
    return "(" + node.data + ", " + toString2(node.left) + ", " +
        toString2(node.right) + ")";
}

/* Write a method removeLeaves that removes the leaves from a tree.  If your 
 * method is called on an empty tree, the method does not change the tree 
 * because there are no nodes of any kind (leaf or not).
 */
public void removeLeaves() {
    overallRoot = removeLeaves(overallRoot);
}

private IntTreeNode removeLeaves(IntTreeNode node) {
    if(node == null)
        return null;
        
    if(node.left == null && node.right == null)
        return null;
        
    node.left = removeLeaves(node.left);
    node.right = removeLeaves(node.right);
    return node;
}

/* Write a method tighten that eliminates branch nodes that have only one
 * child.
 */
public void tighten() {
    overallRoot = tighten(overallRoot);
}

private IntTreeNode tighten(IntTreeNode node) {
    if(node == null)
        return null;
        
    if(node.left == null && node.right != null)
        return tighten(node.right);
        
    if(node.left != null && node.right == null)
        return tighten(node.left);
        
    node.left = tighten(node.left);
    node.right = tighten(node.right);
    return node;
}

/* Write a method that adds nodes until the binary tree is a "perfect" tree. A 
 * perfect binary tree is one where all leaves are at the same level. Another 
 * way of thinking of it is that you are adding dummy nodes to the tree until 
 * every path from the root to a leaf is the same length. A perfect tree's 
 * shape is exactly triangular and every branch node has exactly two children. 
 * Each node you add to the tree should store the value 0.
 */
public void makePerfect() {
    int h = height();
    overallRoot = makePerfect(overallRoot, h);
}

private IntTreeNode makePerfect(IntTreeNode node, int h) {
    if(h <= 0)
        return null;
        
    if(node == null)
        node = new IntTreeNode(0);
        
    node.left = makePerfect(node.left, h - 1);
    node.right = makePerfect(node.right, h - 1);
    return node;
}

public int height() {
    return height(overallRoot);
}

private int height(IntTreeNode root) {
    if(root == null) {
        return 0;
    } else {
        return 1 + Math.max(height(root.left), height(root.right));
    }
}

/* Write a method countEvenBranches that returns the number of branch nodes in 
 * a binary tree that contain even numbers. A branch node is one that has one 
 * or two children (i.e., not a leaf node). An empty tree has 0 even branches.
 */
public int countEvenBranches() {
    return countEvenBranches(overallRoot);
}

private int countEvenBranches(IntTreeNode node) {
    if(node == null)
        return 0;
        
    int count = 0;
    
    if(node.data % 2 == 0 && (node.left != null || node.right != null))
        count++;
        
    return count + countEvenBranches(node.left) +
        countEvenBranches(node.right);
}

/* Write a method doublePositives that doubles all data values greater than 0 
 * in a binary tree of integers.
 */
public void doublePositives() {
    doublePositives(overallRoot);
}

private void doublePositives(IntTreeNode node) {
    if(node == null)
        return;
        
    if(node.data > 0)
        node.data *= 2;
        
    doublePositives(node.left);
    doublePositives(node.right);
}

/* Write a method trim that could be added to the IntTree class. The method 
 * accepts minimum and maximum integers as parameters and removes from the 
 * tree any elements that are not within that range, inclusive. For this 
 * method you should assume that your tree is a binary search tree (BST) and 
 * that its elements are in valid BST order. Your method should maintain the 
 * BST ordering property of the tree.
 */
public void trim(int min, int max) {
    overallRoot = trim(overallRoot, min, max);
}

private IntTreeNode trim(IntTreeNode node, int min, int max) {
    if(node == null)
        return null;
        
    if(node.data < min)
        return trim(node.right, min, max);
        
    if(node.data > max)
        return trim(node.left, min, max);
        
    node.left = trim(node.left, min, max);
    node.right = trim(node.right, min, max);
    return node;
}