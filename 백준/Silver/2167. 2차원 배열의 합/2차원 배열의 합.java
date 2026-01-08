import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 백준 2167번 : 2차원 배열의 합
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] arr;
    public static void main(String[] args) throws IOException {
        String[] inp = br.readLine().split(" ");
        int n = Integer.parseInt(inp[0]);
        int m = Integer.parseInt(inp[1]);

        arr = new int[n+1][m+1];

        for (int i = 0; i< n; i++) {
            String[] line = br.readLine().split(" ");

            for (int j = 0; j < m; j++) {
                arr[i+1][j+1] = Integer.parseInt(line[j]) + arr[i][j+1] + arr[i+1][j] - arr[i][j];
            }
        }

        int cases = Integer.parseInt(br.readLine());

        for (int i = 0; i < cases; i++) {
            getSum();
        }
    }

    private static void getSum() throws IOException {
        String[] inp = br.readLine().split(" ");
        int i = Integer.parseInt(inp[0]);
        int j = Integer.parseInt(inp[1]);
        int x = Integer.parseInt(inp[2]);
        int y = Integer.parseInt(inp[3]);

        System.out.println(arr[x][y] - arr[i-1][y] - arr[x][j-1] + arr[i-1][j-1]);
    }
}
