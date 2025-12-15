import java.io.*;

// 백준 11659번 : 구간 합 구하기 4
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inp = br.readLine().split(" ");
        int n = Integer.parseInt(inp[0]);
        int m = Integer.parseInt(inp[1]);
        int[] prefixSum = new int[n+1];

        String[] nums = br.readLine().split(" ");

        for (int i = 1; i <= n; i++) {
            prefixSum[i] = prefixSum[i-1] + Integer.parseInt(nums[i-1]);
        }

        for (int i = 0; i < m; i++) {
            inp = br.readLine().split(" ");
            int start = Integer.parseInt(inp[0]);
            int end = Integer.parseInt(inp[1]);

            bw.write((prefixSum[end] - prefixSum[start-1]) + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
