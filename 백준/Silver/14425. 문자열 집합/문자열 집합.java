import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");

        int n = Integer.parseInt(inp[0]);
        int m = Integer.parseInt(inp[1]);

        HashMap<String, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            map.put(word, 1);
        }

        int cnt = 0;
        for (int i = 0; i < m; i++) {
            String word = br.readLine();
            if (map.getOrDefault(word, 0) != 0) cnt ++;

        }

        System.out.println(cnt);
    }
}
