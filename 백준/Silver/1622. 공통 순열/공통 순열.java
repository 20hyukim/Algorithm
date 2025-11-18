import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String first;
        
        while ((first = br.readLine()) != null) {
            String second = br.readLine();
            if (second == null) break;
            
            TreeMap<Character, Integer> fMap = new TreeMap<>();
            TreeMap<Character, Integer> sMap = new TreeMap<>();
            
            for (char c : first.toCharArray()) {
                fMap.put(c, fMap.getOrDefault(c, 0) + 1);
            }
            
            for (char c : second.toCharArray()) {
                sMap.put(c, sMap.getOrDefault(c, 0) + 1);
            }
            
            StringBuilder result = new StringBuilder();
            for (Character c : fMap.keySet()) {
                if (sMap.containsKey(c)) {
                    int maxDup = Math.min(fMap.get(c), sMap.get(c));
                    for (int i = 0; i < maxDup; i++) {
                        result.append(c);
                    }
                }
            }
            
            System.out.println(result);
        }
    }
}