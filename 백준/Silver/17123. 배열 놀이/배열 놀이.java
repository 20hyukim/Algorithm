
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int cases = Integer.parseInt(br.readLine());

        for (int i = 0; i < cases; i ++) {
            getResult(br);
        }
    }

    private static void getResult(BufferedReader br) throws IOException {
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        int[][] arrs = new int[n+1][n+1];

        // 초기 배열 입력
        for (int i = 1; i <= n; i++) {
            String[] row = br.readLine().split(" ");
            for (int j = 1; j <= n; j++) {
                arrs[i][j] = Integer.parseInt(row[j-1]);
            }
        }

        int[][] diffs = new int[n+2][n+2];

        // 업데이트 연산
        for (int i = 0; i < m; i++) {
            String[] rcs = br.readLine().split(" ");
            int r1 = Integer.parseInt(rcs[0]);
            int c1 = Integer.parseInt(rcs[1]);
            int r2 = Integer.parseInt(rcs[2]);
            int c2 = Integer.parseInt(rcs[3]);
            int v = Integer.parseInt(rcs[4]);

            diffs[r1][c1] += v;
            diffs[r2+1][c1] -= v;
            diffs[r1][c2+1] -= v;
            diffs[r2+1][c2+1] += v;
        }

        // prefix sum으로 실제 값 복원 및 적용
        for (int r = 1; r <= n; r++) {
            for (int c = 1; c <= n; c++) {
                diffs[r][c] = diffs[r-1][c] + diffs[r][c-1] + diffs[r][c] - diffs[r-1][c-1];
                arrs[r][c] += diffs[r][c];
            }
        }

        // 행의 합 출력
        for (int i = 1; i <= n; i++) {
            int result = 0;
            for (int j = 1; j <= n; j++) {
                result += arrs[i][j];
            }
            System.out.print(result + " ");
        }
        System.out.println();

        // 열의 합 출력
        for (int i = 1; i <= n; i++) {
            int result = 0;
            for (int j = 1; j <= n; j++) {
                result += arrs[j][i];
            }
            System.out.print(result + " ");
        }
        System.out.println();
    }
}
