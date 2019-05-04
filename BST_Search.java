 //Definition for a binary tree node.
 public class TreeNode {
       int val;
       TreeNode left;
       TreeNode right;
       TreeNode(int x) { val = x; }
  }
 
 //Recursive solution to searching a BST 
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        while(root != null){
            if (val == root.val){
                return root; 
            }
            if(val < root.val){
                return searchBST(root.left, val);
            }
            else{
                return searchBST(root.right, val);
            }
        }
        return null;
                        
    }
}