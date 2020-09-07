# looked for it in stackoverflow, im used to oracle capabilities
# and did not know that mysql does not allow correlated delete subquery

delete p1
from person p1 join person p2
on p1.email=p2.email and p1.id > p2.id;

