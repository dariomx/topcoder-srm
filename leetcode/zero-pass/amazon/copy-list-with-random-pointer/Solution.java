/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *   int label;
 *   RandomListNode next, random;
 *   RandomListNode(int x) { this.label = x; }
 * };
 */
import java.util.HashMap;
import java.util.Map;
public class Solution {
  public RandomListNode copyRandomList(RandomListNode head) {
    if(head == null){
      return null;
    }
    RandomListNode origHead = head;
    Map<Integer, RandomListNode> nodeRef = new HashMap<>();
    RandomListNode res = new RandomListNode(head.label);
    RandomListNode current = res;
    nodeRef.put(current.label, current);

    while(head.next != null){
      current.next = new RandomListNode(head.next.label);
      nodeRef.put(current.next.label, current.next);
      current = current.next;
      head = head.next;
    }

    head = origHead;
    current = res;

    while(head.next != null){
      RandomListNode tmp = nodeRef.get(head.random.label);
      if(tmp != null){
        current.random = tmp;
      }
      current = current.next;
      head = head.next;
    }

    return res;
  }
}