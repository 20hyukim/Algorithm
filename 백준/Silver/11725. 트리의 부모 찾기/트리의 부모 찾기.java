import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, List<String>> graph = new HashMap<>();

        int cases = Integer.parseInt(br.readLine());

        for (int i = 0; i < cases - 1; i++) {
            String[] inp = br.readLine().split(" ");
            String n1 = inp[0];
            String n2 = inp[1];

            graph.computeIfAbsent(n1, k -> new ArrayList<>()).add(n2);
            graph.computeIfAbsent(n2, k -> new ArrayList<>()).add(n1);
        }

        String[] parents = new String[cases+1];
        boolean[] visited = new boolean[cases+1];
        Deque<String> queue = new ArrayDeque<>();
        queue.addLast("1");
        visited[1] = true;
        while(!queue.isEmpty()) {
            String p = queue.removeFirst();
            for (String child: graph.get(p)) {
                if (!visited[Integer.parseInt(child)])  {
                    parents[Integer.parseInt(child)] = p;
                    queue.addLast(child);
                    visited[Integer.parseInt(child)] = true;
                }
            }
        }

        for (int i = 2; i < cases + 1; i++) {
            System.out.println(parents[i]);
        }

    }
}
