import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i = 0; i< commands.length; i++){
            PriorityQueue<Integer> minHeap = new PriorityQueue<>();
            for (int n = commands[i][0]-1; n < commands[i][1]; n++){
                minHeap.add(array[n]);
            } 
            for(int k=0; k<commands[i][2];k++){
                int v = minHeap.poll();
                answer[i] = v;
            }
        }
        return answer;
    }
}