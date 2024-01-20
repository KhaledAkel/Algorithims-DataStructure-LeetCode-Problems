class TimeMap:

    def __init__(self):
        self.Map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.Map:
            self.Map[key] = []
        self.Map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.Map:
            a, b = 0, len(self.Map[key]) - 1
            res = ""

            while a <= b:
                mid = (a + b) // 2

                if self.Map[key][mid][0] == timestamp:
                    return self.Map[key][mid][1]
                
                elif self.Map[key][mid][0] < timestamp:
                    res = self.Map[key][mid][1]
                    a = mid + 1
                
                else:
                    b = mid - 1
            return res
        else:
            return ""
