import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static int[] parent;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int v = Integer.parseInt(inp[0]);
        int e = Integer.parseInt(inp[1]);

        PriorityQueue<Edge> queue = new PriorityQueue<>(Comparator.comparing(edge -> edge.value));
        parent = new int[v+1];

        for (int i = 1; i < v+1; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < e; i++) {
            String[] line = br.readLine().split(" ");
            int value = Integer.parseInt(line[2]);
            int s1 = Integer.parseInt(line[0]);
            int s2 = Integer.parseInt(line[1]);

            Edge edge = new Edge(value, s1, s2);
            queue.add(edge);
        }
        int total = 0;

        while (!queue.isEmpty()) {
            Edge edge = queue.poll();
            int parent1 = getParent(edge.s1);
            int parent2 = getParent(edge.s2);
            if (parent1 == parent2)
                continue;

            total += edge.value;
            setParent(parent1, parent2);
        }

        System.out.println(total);
    }

    private static void setParent(int s1, int s2) {
        parent[s1] = s2;
    }

    private static int getParent(int s) {
        if (parent[s] != s) {
            parent[s] = getParent(parent[s]);
        }
        return parent[s];
    }



    static class Edge {
        int value;
        int s1;
        int s2;

        public Edge(int value, int s1, int s2) {
            this.value = value;
            this.s1 = s1;
            this.s2 = s2;
        }
    }
}

