import java.util.*;

class UndergroundSystem {
    private Map<String,Stats> graph = new HashMap<>();
    private Map<Integer,CheckInInfo> passengerInfo = new HashMap<>();

    class Stats {
        int totalTime = 0;
        int count = 0;

        public void updateStats(int duration) {
            totalTime += duration;
            count++;
        }
    }

    class CheckInInfo {
        String src;
        int startTime;

        public CheckInInfo(String src_, int startTime_) {
            src = src_;
            startTime = startTime_;
        }
    }

    public UndergroundSystem() {
        
    }
    
    public void checkIn(int id, String stationName, int t) {
        passengerInfo.put(id, new CheckInInfo(stationName, t));
    }
    
    public void checkOut(int id, String stationName, int t) {
        CheckInInfo cinfo = passengerInfo.get(id);
        String route = cinfo.src+"$"+stationName;
        Stats rstats = graph.getOrDefault(route, new Stats());
        rstats.updateStats(t-cinfo.startTime);
        graph.put(route,rstats);
        passengerInfo.remove(id);
    }
    
    public double getAverageTime(String startStation, String endStation) {
        String route = startStation+"$"+endStation;
        Stats rstats = graph.get(route);
        return (double) rstats.totalTime/rstats.count;
    }
}

class Solution {

    public static void main(String[] args) {
        System.out.println();
    }
}
