import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        
        for(String p : participant){
            map.put(p, 0);
        }
        
        for(String p : participant){
            int count = map.get(p) + 1;
            map.put(p, count);
        }
        
        for(String c : completion){
            int count = map.get(c) - 1;
            map.put(c, count);
        }
        
        for(Map.Entry<String, Integer> entry : map.entrySet()){
            if(entry.getValue() != 0){
                return entry.getKey();
            }
        }
        return "";
    }
}