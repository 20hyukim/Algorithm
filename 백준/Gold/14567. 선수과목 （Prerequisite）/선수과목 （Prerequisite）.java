import java.io.*;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

// 백준 14567번 : 선수과목 (Prerequisite)
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        List<Integer>[] pre = new ArrayList[n+1];
        int[] indegree = new int[n+1];

        for (int i = 1; i < n+1; i++) {
            pre[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            String[] se = br.readLine().split(" ");
            int s = Integer.parseInt(se[0]);
            int e = Integer.parseInt(se[1]);
            pre[s].add(e);
            indegree[e] += 1;
        }

        int[] cost = new int[n+1];

        Deque<Integer> queue = new ArrayDeque<>();

        for (int i = 1; i < n+1; i++) {
            if (indegree[i] == 0) {
                queue.addLast(i);
            }
        }

        int semester = 0;
        while(!queue.isEmpty()) {
            int size = queue.size();
            semester++;

            for (int i = 0; i < size; i++) {
                int now = queue.removeFirst();
                cost[now] = semester;

                for (int c : pre[now]) {
                    indegree[c] --;

                    if (indegree[c] == 0) {
                        queue.addLast(c);
                    }
                }
            }
        }

        for (int i = 1; i < n+1; i++) {
            bw.write(cost[i] + " ");
        }

        bw.flush();

        bw.close();
        br.close();
    }
}
