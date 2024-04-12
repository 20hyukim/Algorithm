import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        int[] curr = new int[n + 1];
        for(int i = 1; i <= n; i++){
            curr[i] = 1;
        }
        
        
        for (int l : lost){
            curr[l]--;
        }
        
        for(int r : reserve) {
            curr[r] += 1;
        }
        
        for (int i = 1; i <= n; i++){
            if (curr[i] == 0){
                if (i>1 && curr[i-1] > 1){
                    curr[i] += 1;
                    curr[i-1] -= 1;
                } else if (i<n && curr[i+1] > 1){
                    curr[i] += 1;
                    curr[i+1] -=1;
                }
            }
        }
        
        for (int i = 1; i<= n; i++) {
            if(curr[i] >= 1){
                answer ++;
            }
        }
        
        return answer;
    }
}