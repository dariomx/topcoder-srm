class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cnt = defaultdict(lambda: 0)
        for card in hand:
            cnt[card] += 1
        min_card = [card for card in cnt]
        heapify(min_card)
        pend = len(hand)
        while pend > 0:
            for card in range(min_card[0], min_card[0] + W):
                if cnt[card] == 0:
                    return False
                cnt[card] -= 1
                pend -= 1
            while min_card and cnt[min_card[0]] == 0:
                heappop(min_card)
        return True
