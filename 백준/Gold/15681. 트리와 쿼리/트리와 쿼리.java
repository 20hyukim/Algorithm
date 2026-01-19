import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static List<Integer>[] edges;
    static int[] childNodes;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inp = br.readLine().split(" ");
        int n = Integer.parseInt(inp[0]);
        int r = Integer.parseInt(inp[1]);
        int q = Integer.parseInt(inp[2]);

        edges = new ArrayList[n+1];
        childNodes = new int[n+1];
        boolean[] visited = new boolean[n+1];

        for (int i = 1; i < n+1; i++) {
            edges[i] = new ArrayList<>();
        }

        for (int i = 0; i < n-1; i++) {
            String[] edge = br.readLine().split(" ");
            int s = Integer.parseInt(edge[0]);
            int e = Integer.parseInt(edge[1]);

            edges[s].add(e);
            edges[e].add(s);
        }
        visited[r] = true;
        getChilds(r, visited);

        for (int i = 0; i < q; i++) {
            int qq = Integer.parseInt(br.readLine());
            bw.write(childNodes[qq] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    private static int getChilds(int r, boolean[] visited) {
        int cnt = 0;
        for (int i = 0; i < edges[r].size(); i++) {
            int c = edges[r].get(i);
            if (!visited[c]) {
                visited[c] = true;
                cnt += getChilds(c, visited);
                visited[c] = false;
            }
        }
        return childNodes[r] = cnt + 1;
    }


}
