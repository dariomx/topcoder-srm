# originally made a O(n) but found in phorum that it could be done O(log n)
# i knew that bin-search could be leveraged but was not really sure of
# the details, anyway, after seeing that phorum entry (did not see the code),
# tried my own O(log n) solution .. im sure is overkill and not very
# elegant; but it is mine :-)
#
# i can see others in phorum used a search space over a diff space, though
# there solutions look quite similar. the biggest puzzle for me is their
# usage of the start index, and not the start value.

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        else:
            k -= arr[0] - 1
        if arr[-1] < 1000:
            expanded = True
            arr.append(1000)
        else:
            expanded = False
        start, end = 0, len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            left_range = arr[mid] - arr[start] + 1
            left_size = mid - start + 1
            left_gaps = left_range - left_size
            if left_gaps > 0 and k <= left_gaps:
                if left_size == 2:
                    break
                else:
                    end = mid
                    continue
            k -= left_gaps
            right_range = arr[end] - arr[mid] + 1
            right_size = end - mid + 1
            right_gaps = right_range - right_size
            if right_gaps > 0 and k <= right_gaps:
                if right_size == 2:
                    start = mid
                    break
                else:
                    start = mid
            elif end == len(arr) - 1 and k > right_gaps:
                k -= right_gaps + int(expanded)
                start = end
                break
        return arr[start] + k

