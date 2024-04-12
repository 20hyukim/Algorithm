import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int num: nums){
            map.put(num, 1);
        }
        
        
        int answer = map.size();
        if (nums.length/2 < answer){
            answer = nums.length/2;
        }
        return answer;
    }
}