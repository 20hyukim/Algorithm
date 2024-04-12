import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        ArrayList<String> strNumbers = new ArrayList<>();
        
        for (int n : numbers){
            String str = Integer.toString(n);
            strNumbers.add(str);
        }        
        
        Collections.sort(strNumbers, (s1, s2) -> (s1+s1+s1+s1+s1).compareTo(s2+s2+s2+s2+s2));
        Collections.reverse(strNumbers);
        
        String answer = "";
        for (String s : strNumbers){
            answer += s;
        }
        if (answer.startsWith("0")){
            return "0";
        }
        return answer;
    }
}