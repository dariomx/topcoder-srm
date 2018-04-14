import java.util.*;

class Solution {
    private Map<Character, Integer> getTaskCount(char[] tasks) {
        Map<Character,Integer> taskCnt = new HashMap<>();
        for(Character t: tasks) {
            taskCnt.merge(t, 1, Integer::sum);
        }
        return taskCnt;
    }

    private NavigableMap<Integer, Set<Character>> getTaskSched(Set<Character> tasks) {
        NavigableMap<Integer, Set<Character>> taskSched = new TreeMap<>();
        taskSched.put(Integer.MIN_VALUE, new HashSet<>(tasks));
        return taskSched;
    }

    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> taskCnt = getTaskCount(tasks);
        NavigableMap<Integer, Set<Character>> taskSched =
            getTaskSched(taskCnt.keySet());
        Comparator<Character> byCntDesc =
		    (Character t1, Character t2) ->
            taskCnt.get(t2) - taskCnt.get(t1);
        int clock = 0;
        int idle = 0;
        while(!taskSched.isEmpty()) {
            Character nextTask = null;
            int  oldSched = -1;
            int  nextSched = -1;
            int  maxCnt = Integer.MIN_VALUE;
            for(Map.Entry<Integer, Set<Character>> entry:
                taskSched.headMap(clock, true).entrySet()) {
                Character task = Collections.min(entry.getValue(), byCntDesc);
                int cnt = taskCnt.get(task);
                if (cnt > maxCnt) {
                    nextTask = task;
                    oldSched = entry.getKey();
                    nextSched = clock + n + 1;
                    maxCnt = cnt;
                }
            }
            if (nextTask == null) {
                int minSched = taskSched.firstKey();
                idle += minSched - clock;
                clock += idle;
            } else {
                if(taskSched.get(oldSched).size() == 1) {
                    taskSched.remove(oldSched);
                } else {
                    taskSched.get(oldSched).remove(nextTask);
                }
                taskCnt.put(nextTask, taskCnt.get(nextTask)-1);
                clock++;
                if (taskCnt.get(nextTask) > 0) {
                    Set<Character> taskPeers;
                    if(taskSched.containsKey(nextSched)) {
                        taskPeers = taskSched.get(nextSched);
                    } else {
                        taskPeers = new HashSet<>();
                        taskSched.put(nextSched, taskPeers);
                    }
                    taskPeers.add(nextTask);
                }
            }
        }
        return tasks.length + idle;
    }
}