"""
I still do not master DP good enough, so kinda cheated for this exercise.
But well, at least let me do the exercise of verbalizing what I learned from
here.

I knew that the DP recursion "table" rec(i,j) will require using the
positions i and j from the words, because otherwise we can not "extend" into
a better solution for the recursive case. That is, the best solution for next
size n, must be formed by extending best solution for size n-1 (optimal
subproblem structure this property is called, if I recall properly). So we
needed that positions i and j were used, and then recursive equation would
extend either to the left or to the right, in order to form a better solution.

I was thinking it extending to the right, kinda distrust the extension to a
better solution. Extending both strings simultaneously sounded like cheating,
I felt like the non linear recursion (one branch per word), needed to be
antisymmetric. So I abandoned my attempt and cheated; but later on realized
that my intuition was not 100% garbage: there was a need to do asymmetric
recursion after all.

At the beginning I thought that this could be solved with max common
substring, in the sense that I could simply remove chars before and after
this common substring, from both words; counting those removals would be the
distance. I suspected that computing maximum common substring required DP,
but did not recall the recursion formula. Hence just went to Wikipedia and
looked at it . The recursion is actually against longest common prefix,
which means that we shall use positions i and j (otherwise, we can not extend to
a better solution in recursive case):

rec(i, j) = rec(i-1, j-1) + 1  ,if word1[i] == word[j]
          = 0                  ,otherwise

Once we know all the rec(i, j) values, we just take the maximum across all
possible prefixes combos; that is, we traverse all rec(i, j) where (i,
j) is in [0,n-1] x [0, m-1], and just take the maximum. If I needed to
translate into my own words, why this works, it would be something like:

<the max common string can be found by exploring all possible endings (i,j),
where i and j are endings of wanted substring in word1 and word2 respectively.
if for each one of those possible endings (i,j), we had a way of knowing what
is the maximum # of steps that we can move backwards such that words keep on
matching; then we would be done>

Thus, the meaning of the recursion "table" rec(i,j) is precisely that wish we
stated on paragraph above: assuming we are forced to use positions i and j in
word1 and word2 respectively, what is the maximum number of steps that I can
move backwards until the words differ. In other words, aligning the words at
those positions (i, j); what is the size of the left common prefix.

So far I was happy with this approach, but submitted and realized that for a
sample like: [die, de], that common substring "d" was not good enough;
simply removing the i (1 operation) could make the strings match. The
immersed subproblem here then, is rather the max common "subsequence".

I then saw the recursive formula for this related problem at Wikipedia,
and realized that is quite similar to max common substring. But instead of
simply throwing the towel when positions i and j do not match; we just
consider the options where we shift just one of the indexes, and take the
best of both recursion branches:

rec(i, j) = rec(i-1, j-1) + 1              ,if word1[i] == word[j]
          = max(rec(i-1, j), rec(i, j-1))  ,otherwise

The solution of course could be optimized further by using memoization,
or even more by using the iterative version. I just added the former and the
submission passes; so I let the solution like that. I did so, cause it shows me
the close relation between the recursive equations of both sub-problems
considered here: max common substring and max common subsequence.

"""


class Solution(object):
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        cache = dict()

        def rec(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if not (0 <= i < n) or not (0 <= j < m):
                ret = 0
            elif word1[i] == word2[j]:
                ret = rec(i - 1, j - 1) + 1
            else:
                ret = max(rec(i, j - 1), rec(i - 1, j))
            cache[(i, j)] = ret
            return ret

        max_len = 0
        for i in xrange(n):
            for j in xrange(m):
                max_len = max(max_len, rec(i, j))
        return (n - max_len) + (m - max_len)
