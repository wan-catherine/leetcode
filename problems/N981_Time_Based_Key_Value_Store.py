import bisect
import collections


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = ([timestamp],[value])
        else:
            self.mapping[key][0].append(timestamp)
            self.mapping[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        index = bisect.bisect(self.mapping[key][0], timestamp)
        if index <= 0:
            return ""
        if index >= len(self.mapping[key][0]):
            return self.mapping[key][1][-1]
        return self.mapping[key][1][index - 1]

    # Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

class TimeMap_1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tm = collections.defaultdict(dict)
        self.times = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.tm:
            bisect.insort_left(self.times, timestamp)
        self.tm[timestamp][key] = value


    def get(self, key: str, timestamp: int) -> str:
        times = self.times
        index = bisect.bisect(times, timestamp)
        if index == 0 :
            return ""
        for i in range(index-1, -1, -1):
            if key in self.tm[times[i]]:
                return self.tm[times[i]][key]
        return ""