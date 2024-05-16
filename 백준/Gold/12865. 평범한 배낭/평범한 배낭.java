import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.io.*;
public class Main {

        // A utility function that returns
        // maximum of two integers
        static int max(int a, int b) { return (a > b) ? a : b; }

        // Returns the value of maximum profit
        static int knapSackRec(int W, List<Integer> wt, List<Integer> val,
                               int n, int[][] dp)
        {

            // Base condition
            if (n == 0 || W == 0)
                return 0;

            if (dp[n][W] != -1)
                return dp[n][W];

            if (wt.get(n - 1) > W)

                // Store the value of function call
                // stack in table before return
                return dp[n][W]
                        = knapSackRec(W, wt, val, n - 1, dp);

            else

                // Return value of table after storing
                return dp[n][W]
                        = max((val.get(n - 1)
                                + knapSackRec(W - wt.get(n - 1), wt, val,
                                n - 1, dp)),
                        knapSackRec(W, wt, val, n - 1, dp));
        }

        static int knapSack(int W, List<Integer> wt, List<Integer> val, int N)
        {

            // Declare the table dynamically
            int dp[][] = new int[N + 1][W + 1];

            // Loop to initially filled the
            // table with -1
            for (int i = 0; i < N + 1; i++)
                for (int j = 0; j < W + 1; j++)
                    dp[i][j] = -1;

            return knapSackRec(W, wt, val, N, dp);
        }

        // Driver code
        public static void main(String args[]) throws IOException
        {

            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String line = reader.readLine();
            String[] lines = line.split("\\s+");
            int num = Integer.parseInt(lines[0]);
            int W = Integer.parseInt(lines[1]);
            List<Integer> wt = new ArrayList<>();
            List<Integer> val = new ArrayList<>();

            for(int i =0; i<num; i++){
                String[] w_v = reader.readLine().split("\\s+");
                wt.add(Integer.valueOf(w_v[0]));
                val.add(Integer.valueOf(w_v[1]));
            }

            System.out.println(knapSack(W, wt, val, num));
        }
    }
    /*This code is contributed by Rajat Mishra */

