"""
Python3 O(log(n)) solution using statistical ideas

I am currently studying statistics, so thought it would be a nice
practice to apply a bit of that here.

What we want here, per requirement, is that every integer point has
the same probability of being picked. Now, since points are
distributed among rectangles we could use a sampling technique where
we pick first a rectangle based on its "weight" (size), and then
we use simple random sampling within such rectangle. I actually
made the exercise of proving this implicit claim with two rectangles.

Say we have 10 points, where 6 live in first rectangle and 4 live in
the other one. We could think of a decision tree where first branching
is done by picking the rectangle and second branching is done by
picking the actual point within each rectangle (so first branch has 6
leaves and second branch has 4).

Since we know that we want to use simple random sampling (SRS) within
each rectangle, we know that:

P(x_i | R_1) = 1/6 for i in {1,2,3,4,5,6}
P(x_i | R_2) = 1/4 for i in {7, 8, 9, 10}

where x_i is the event of picking element x_i, and R_j is the event
of picking rectangle 1 or 2.

Now, using definition of conditional probability (used backwards) we know
that the probability of reaching every leaf in decision tree is given by:

P(R_j and x_i) = P(R_j) P(x_i | R_j)

and we would like the following equality to hold, if every leaf in
the decision tree is to be equally likely to be picked (as each leaf
represents one of the integer points from our total set):

P(R_1) P(x_i | R_1) = P(R_2) P(x_i | R_2)

Replacing the constants we setup for our example, equality becomes:

P(R_1) (1/6) = P(R_2) (1/4)

Since we just have two rectangles P(R_2) = 1 - P(R_1), hence

P(R_1) (1/6) = (1 - P(R_1)) (1/4)

Solving that linear equation for P(R_1) will give us 0.6, hence leaving
P(R_2) = 0.4. And that is precisely the intuitive "weight" we could
think of assigning, if wanting to make probability proportional to the size
of each rectangle. I did not do it, but suspect this proof-template
could we extended to any probabilities and number of rectangles.
So, let us buy for now that such sampling technique is valid.

Now, one way of implementing it is to to compute the
percentages out of the total that each rectangle contributes with,
and think that as the desired probability to pick such rectangle.
Then we could use an enumerative sampling algorithm like the one
mentioned at page 27 of this presentation:

http://www.eustat.eus/productosServicios/52.1_Unequal_prob_sampling.pdf

In such algorithm we compute the the cumulative sum of probabilities
for each rectangle, using the order they have already in input param.
Such cumulative probability could be thought as the high end of a
probabilities range. Then the algorithm generates a uniformly random
number in [0,1] and searches for the rectangle whose probability
range contains such random number. We can do such search efficiently
with a binary search.

Once we picked the rectangle, we proceed to generate a random number
from there by using another result from Probability: in order to
select a random point within a rectangle, we can think of two
independent random variables for each axis. Hence, generating one
tuple where first element is uniform random number for axis-X range,
and second element is uniform random number for axis-Y range; should
be equivalent to picking one point randomly from rectangle formed by
cartesian product of those two ranges. See proof/comment from this
discussion (The one starting with "That statement is incorrect,
direct product of two independent uniform measures is a uniform
measure. This can be shown as follows ...")

https://stackoverflow.com/questions/6884003/generate-a-random-point-within-a-rectangle-uniformly

And voilà, putting all that together gives following snippet. At the time
of this writing, it beats all the Python3 solutions.
"""

from bisect import bisect_left
from random import random, randint

class Solution:

    def __init__(self, rects):
        self.rects = rects
        self.cump = []
        total = 0
        for x1,y1,x2,y2 in rects:
            w, h = x2 - x1 + 1, y2 - y1 + 1
            total += w * h
            self.cump.append(total)
        for i in range(len(self.cump)):
            self.cump[i] /= total

    def pick(self):
        i = bisect_left(self.cump, random())
        x1,y1,x2,y2 = self.rects[i]
        x = randint(x1, x2)
        y = randint(y1, y2)
        return (x,y)
