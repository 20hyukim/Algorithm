import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> queue = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            queue.add(Integer.parseInt(br.readLine()));
        }
        int max_val = 0;
        int lines = n;

        while (!queue.isEmpty()) {
            int val = queue.poll();
            max_val = Math.max((lines-- * val), max_val);
        }

        System.out.println(max_val);
    }
}
