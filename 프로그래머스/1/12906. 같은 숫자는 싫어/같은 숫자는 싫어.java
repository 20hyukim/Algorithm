import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answerList = new ArrayList<>();
        
        int n = -1;
        for(int a: arr){
            if (a != n){    
                answerList.add(a);
                n = a;
            }
        }
        
        int[] answer = new int[answerList.size()];
        
        for (int i = 0; i<answerList.size(); i++){
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}