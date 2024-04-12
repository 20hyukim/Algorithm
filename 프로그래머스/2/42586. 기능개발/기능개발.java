import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] remain = new int[progresses.length];
        
        for(int i = 0; i < progresses.length; i++){
            int r = 100 - progresses[i];
            int days = r/speeds[i];
            if (r%speeds[i] != 0){
                days += 1;
            }
            remain[i] = days;
            
        }
        
        ArrayList<Integer> result = new ArrayList<>();
        
        int total = 1;
        int max_day = remain[0];
        for (int i = 1; i < remain.length; i++){
            if (max_day >= remain[i]){
                total += 1;
            }
            else{
                result.add(total);
                total = 1;
                max_day = remain[i];
            }
        }
        result.add(total);   
        
        int[] answer = new int[result.size()];
        for (int i = 0; i<result.size(); i++){
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}