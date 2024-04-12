import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for (int s: scoville) {
            minHeap.add(s);
        }
        
        int answer = 0;
        while (minHeap.peek() < K){
            if (minHeap.size() < 2){
                answer = -1;
                break;
            }
            int s = minHeap.poll();
            int ss = minHeap.poll();
            minHeap.add(s + (ss*2));
            answer += 1;
        }
        
        
        return answer;
    }
}