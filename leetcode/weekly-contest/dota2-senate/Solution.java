import java.util.*;

public class Solution {
    private static final char DARE = 'D';
    private static final char RADIANT = 'R';

    private Map<Character, String> partyName =
        new HashMap<Character, String>() {{
            put(DARE, "Dire");
            put(RADIANT, "Radiant");
    }};

    private Map<Character, Character> enemy =
        new HashMap<Character, Character>() {{
            put(DARE, RADIANT);
            put(RADIANT, DARE);
    }};

   private Map<Character, NavigableMap<Integer, ListNode>> partySenate =
       new HashMap<Character, NavigableMap<Integer, ListNode>>() {{
            put(DARE, new TreeMap<>());
            put(RADIANT, new TreeMap<>());
    }};

    private ListNode appendNode(ListNode last, ListNode node) {
        last.next = node;
        node.prev = last;
        return node;
    }

    public void deleteNode(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private ListNode createList(String senate) {
        partySenate.get(DARE).clear();
        partySenate.get(RADIANT).clear();
        ListNode head = new ListNode(senate.charAt(0), 0);
        partySenate.get(senate.charAt(0)).put(0, head);
        ListNode last = head;
        for(int i=1; i<senate.length(); i++) {
            char party = senate.charAt(i);
            last = appendNode(last, new ListNode(party, i));
            partySenate.get(party).put(i, last);
        }
        last.next = head;
        head.prev = last;
        return head;
    }

    private ListNode nextVictim(int index,
                                NavigableMap<Integer, ListNode> enemyParty) {
        ListNode victim = null;
        if (!enemyParty.isEmpty()) {
            Map.Entry<Integer, ListNode> entry = enemyParty.higherEntry(index);
            if ( entry == null ) {
                entry = enemyParty.firstEntry();
            }
            victim = entry.getValue();
        }
        return victim;
    }

    public String predictPartyVictory(String senate) {
        ListNode node = createList(senate);
        while(true) {
            NavigableMap<Integer, ListNode> enemyParty =
                partySenate.get(enemy.get(node.party));
            ListNode victim = nextVictim(node.index, enemyParty);
            if ( victim == null ) {
                return partyName.get(node.party);
            } else {
                enemyParty.remove(victim.index);
                deleteNode(victim);
                node = node.next;
            }
        }
    }

    private static class ListNode {
        public char party;
        public int  index;
        public ListNode next;
        public ListNode prev;

        public ListNode(char party, int index) {
            this.party = party;
            this.index = index;
            this.next = null;
            this.prev = null;
        }
    }

}