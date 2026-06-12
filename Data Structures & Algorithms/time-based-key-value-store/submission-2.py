class TimeMap:
    s = dict()
    def __init__(self):
        self.s = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.s:
            self.s[key] = dict()
        self.s[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.s:
            return ""
        keys = list(self.s[key].keys())
        t = len(keys)-1
        b = 0
        backup = ""

        while t>=b:
            mid = (t+b)//2
            
            if keys[mid] == timestamp:
                return self.s[key][keys[mid]]
            elif keys[mid] < timestamp:
                backup = self.s[key][keys[mid]]
                b = mid+1
            else:
                t = mid -1
            
        return backup

                