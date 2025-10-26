import java.util.*;
class InsertInterval {
    public static void main(String[] args) {
        int[][] intervals={{1,3},{6,9}};
        int[] newInterval={2,5};
        List<int[]> res=new ArrayList<>();
        int i=0,n=intervals.length;
        while(i<n&&intervals[i][1]<newInterval[0]) res.add(intervals[i++]);
        while(i<n&&intervals[i][0]<=newInterval[1]){
            newInterval[0]=Math.min(newInterval[0],intervals[i][0]);
            newInterval[1]=Math.max(newInterval[1],intervals[i][1]);
            i++;
        }
        res.add(newInterval);
        while(i<n) res.add(intervals[i++]);
        for(int[] arr:res) System.out.println(Arrays.toString(arr));
    }
}
