import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int n: nums){
            map.put(n,1);
        }
    
         int answer = map.size();
        
        if (nums.length/2 < answer) {
            answer = nums.length/2;
        }
        
        return answer;
    }
}