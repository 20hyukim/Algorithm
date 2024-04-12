class Solution {
    int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, 0, 0, target);
        return answer;
    }
    
    public void dfs(int[] numbers, int depth, int total, int target){
        if(depth == numbers.length){
            if (total == target){
                answer += 1;
            }
            return;
        }
        
        dfs(numbers, depth +1, total + (-1*numbers[depth]), target);
        dfs(numbers, depth +1, total + numbers[depth], target);
    }
}