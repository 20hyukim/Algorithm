import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n+3];

        dp[0] = 0;
        dp[1] = 0;
        dp[2] = 1;
        dp[3] = 1;

        int min_cnt = 0;

        for (int i = 4; i < n+1; i++) {
            min_cnt = i;
            if (i%2==0) {
                min_cnt = Math.min(min_cnt, dp[i/2] + 1);
            }
            if (i%3 == 0) {
                min_cnt = Math.min(min_cnt, dp[i/3] + 1);
            }
            min_cnt = Math.min(min_cnt, dp[i-1] + 1);
            dp[i] = min_cnt;
        }
//        System.out.println(Arrays.toString(dp));
        System.out.println(dp[n]);

    }
}
