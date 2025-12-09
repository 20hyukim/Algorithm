import java.io.*;

// 백준 : 15649번 N과 M (1)
public class Main {
    static boolean[] visited;
    static int[] numArr;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inp = br.readLine().split(" ");
        int n = Integer.parseInt(inp[0]);
        int m = Integer.parseInt(inp[1]);
        numArr = new int[m];
        visited = new boolean[n];

        dfs(0, n, m);

        bw.write(sb.toString());

        bw.flush();
        bw.close();
        br.close();
    }

    public static void dfs(int currDepth, int num, int maxDepth) {
        if (currDepth == maxDepth) {
            for (int n : numArr) {
                sb.append(n + 1).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 0; i < num; i++) {
            if (!visited[i]) {
                visited[i] = true;
                numArr[currDepth] = i;
                dfs(currDepth + 1, num, maxDepth);
                visited[i] = false;
            }
        }
    }
}
