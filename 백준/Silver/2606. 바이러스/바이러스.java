import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int compN = Integer.parseInt(br.readLine());
        int couple = Integer.parseInt(br.readLine());

        List<Integer>[] networks = new ArrayList[compN+1];

        for (int i = 1; i < compN+1; i++) {
            networks[i] = new ArrayList<>();
        }

        for (int i = 0; i < couple; i++) {
            String[] se = br.readLine().split(" ");
            int s = Integer.parseInt(se[0]);
            int e = Integer.parseInt(se[1]);

            networks[s].add(e);
            networks[e].add(s);
        }

        boolean[] visited = new boolean[compN+1];

        Deque<Integer> queue = new ArrayDeque<>();
        queue.addLast(1);

        while (!queue.isEmpty()) {
            int popped = queue.removeFirst();
            if (!visited[popped]) {
                visited[popped] = true;
                for (int node: networks[popped]) queue.addLast(node);
            }
        }
        int cnt = 0;

        for (int i = 2; i < compN+1; i++) {
            if (visited[i]) cnt++;
        }

        bw.write(cnt+"");

        bw.flush();

        bw.close();
        br.close();
    }
}
