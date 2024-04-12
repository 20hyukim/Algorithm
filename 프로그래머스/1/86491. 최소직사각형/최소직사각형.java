class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int a = 1;
        int b = 1;
        for(int i = 0; i<sizes.length; i++ ){
            int bigger;
            int smaller;
            if (sizes[i][0] > sizes[i][1]){
                bigger = sizes[i][0];
                smaller = sizes[i][1];
            }
            else{
                bigger = sizes[i][1];
                smaller = sizes[i][0];
            }
            if (a < bigger){
                a = bigger;
            }
            if (b < smaller){
                b = smaller;
            }
        }
        
        return a*b;
    }
}