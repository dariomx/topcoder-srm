
inp = [[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32],[16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],[21,27],[49,50],[38,45],[4,12],[46,50],[13,21]]
maxt = max((max(a,b) for (a,b) in inp))
events = [0] * (maxt+1)

def add_event(start, end):
    for t in range(start, end):
        if events[t] > 1:
            return False
    for t in range(start, end):
        events[t] +=1
    return True

for start, end in inp:
    if add_event(start, end):
        print("added %d,%d" % (start, end))
    else:
        print("did not add %d, %d" % (start, end))
        print(events[start:(end+1)])
    print(events[6:(13 + 1)])
