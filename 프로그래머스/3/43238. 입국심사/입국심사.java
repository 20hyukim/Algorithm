import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        long l = 0;
        long r = (long)Arrays.stream(times).max().getAsInt()*n;
        long m = 0;
        while (l <= r){
            m = (l+r)/2;
            long process = 0;
            for(int time : times){
                process += m/time;    
            }
            
            if (process >= n){
                r = m -1;
                answer = m;
            }
            else{
                l = m + 1;
            }
        }
        
        return answer;
    }
}