import java.io.*;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

// 백준 11725번 : 트리의 부모 찾기
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] parent = new int[n+1];

        List<Integer>[] tree = new ArrayList[n+1];

        for (int i = 1; i < n+1; i++) {
            tree[i] = new ArrayList<>();
        }

        for(int i = 0; i < n-1; i++) {
            String[] inps = br.readLine().split(" ");
            int n1 = Integer.parseInt(inps[0]);
            int n2 = Integer.parseInt(inps[1]);
            tree[n1].add(n2);
            tree[n2].add(n1);
        }

        Deque<Integer> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[n+1];
        queue.addLast(1);

        while (!queue.isEmpty()) {
            int p = queue.removeFirst();
            List<Integer> child = tree[p];
//            System.out.println(p);
            for (Integer c : child) {
                if (visited[c]) continue;
                parent[c] = p;
                visited[c] = true;
                queue.addLast(c);
            }
        }

        for (int i = 2; i < n+1; i++) {
            bw.write(parent[i] + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
