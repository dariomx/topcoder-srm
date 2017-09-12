/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    private static class Appender {
        ListNode head = null;
        ListNode tail = null;

        public void append(ListNode node) {
            if ( head == null ) {
                head = node;
                tail = node;
            } else {
                tail.next = node;
                tail = node;
            }
        }
    }

    private ListNode merge(ListNode l1, ListNode l2) {
        ListNode n1 = l1;
        ListNode n2 = l2;
        ListNode t1, t2;
        Appender appender = new Appender();
        while (n1 != null || n2 != null) {
            if (n1 != null && n2 != null && n1.val == n2.val) {
                t1 = n1.next;
                t2 = n2.next;
                appender.append(n1);
                appender.append(n2);
                n1 = t1;
                n2 = t2;
            } else if ( (n1 != null && n2 == null) ||
                      (n1 != null && n2 != null && n1.val < n2.val)) {
                t1 = n1.next;
                appender.append(n1);
                n1 = t1;
            } else {
                t2 = n2.next;
                appender.append(n2);
                n2 = t2;
            }
        }
        return appender.head;
    }

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        } else {
            ListNode head = lists[0];
            for(int i=1; i<lists.length; i++) {
                head = merge(head, lists[i]);
            }
            return head;
        }
    }
}