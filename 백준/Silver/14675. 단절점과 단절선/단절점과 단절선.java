import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        List<Integer>[] trees = new ArrayList[n+1];

        for (int i = 1; i < n+1; i++) {
            trees[i] = new ArrayList<>();
        }

        for (int i = 0; i < n-1; i++) {
            String[] se = br.readLine().split(" ");
            int s = Integer.parseInt(se[0]);
            int e = Integer.parseInt(se[1]);

            trees[s].add(e);
            trees[e].add(s);
        }

        int q = Integer.parseInt(br.readLine());

        for (int i = 0; i < q; i++) {
            String[] inp = br.readLine().split(" ");
            int t = Integer.parseInt(inp[0]);
            int k = Integer.parseInt(inp[1]);

            if (t == 2) {
                bw.write("yes" + "\n");
                continue;
            }

            if (trees[k].size() != 1) {
                bw.write("yes" + "\n");
                continue;
            }
            bw.write("no" + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
