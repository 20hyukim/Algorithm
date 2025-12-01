import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    static int[] parent;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        PriorityQueue<Edge> queue = new PriorityQueue<>(Comparator.comparing(e -> e.value));

        int n = Integer.parseInt(br.readLine());
        parent = new int[n+1];

        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = i + 1 ; j < n; j++) {
                queue.add(new Edge(i, j, Integer.parseInt(line[j])));
            }
        }

        for (int i = 0; i < n+1; i++) {
            parent[i] = i;
        }
        long total = 0;
        int cnt = 0;

        while(cnt < n-1) {
            Edge e = queue.poll();

            if (getParent(e.s) != getParent(e.e)) {
                total += e.value;
                cnt++;
                setParent(e.s, e.e);
            }
        }

        System.out.println(total);

    }

    private static void setParent(int s, int e) {
        s = getParent(s);
        e = getParent(e);

        if (s != e) {
            parent[s] = e;
        }
    }

    private static int getParent(int s) {
        if (parent[s] != s) {
            parent[s] = getParent(parent[s]);
        }
        return parent[s];
    }

    public static class Edge{
        private int s;
        private int e;
        private int value;


        public Edge(int s, int e, int value) {
            this.s = s;
            this.e = e;
            this.value = value;
        }
    }
}
