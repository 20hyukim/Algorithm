import java.io.*;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> queue = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            String[] nums = br.readLine().split(" ");
            for (String num : nums) {
                int ni = Integer.parseInt(num);

                if (queue.size() != n) {
                    queue.add(ni);
                    continue;
                }

                if (ni > queue.peek()) {
                    queue.poll();
                    queue.add(ni);
                }
            }
        }

        System.out.println(queue.peek() + "");
    }
}
