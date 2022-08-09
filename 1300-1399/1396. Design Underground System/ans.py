class UndergroundSystem:

    def __init__(self):
        self.graph = {}
        self.record = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.record[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        src,startTime = self.record[id]
        self.record.pop(id)
        if src not in self.graph:
            self.graph[src] = {}
        if stationName not in self.graph[src]:
            self.graph[src][stationName] = [0,0]
        totalTime,count = self.graph[src][stationName]
        self.graph[src][stationName][0] = totalTime+t-startTime
        self.graph[src][stationName][1] = count+1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.graph[startStation][endStation][0]/self.graph[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)