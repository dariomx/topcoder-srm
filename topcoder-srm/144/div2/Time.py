class Time:
    def whatTime(self, seconds):
        secs_min = 60
        secs_hour = 60 * secs_min
        hours = int(seconds / secs_hour)
        mins = int((seconds % secs_hour) / secs_min)
        secs = int((seconds % secs_hour) % secs_min)
        return "%d:%d:%d" % (hours,mins,secs)

