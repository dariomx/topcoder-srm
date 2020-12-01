use std::*;
use std::collections::HashMap;

struct Solution {

}

impl Solution {
fn removeLeafNodes(&self, root: TreeNode, target: i32) -> TreeNode {
fn canRemove<T0, RT>(n: T0) -> RT {
return n&&n.left == None&&n.right == None&&n.val == target;
}
if root {
self.removeLeafNodes(root.left, target);
if canRemove(root.left) {
root.left = None;
}
self.removeLeafNodes(root.right, target);
if canRemove(root.right) {
root.right = None;
}
if canRemove(root) {
root = None;
}
}
return root;
} 
}