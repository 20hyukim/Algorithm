import java.io.*;

public class Main {

    static int[][] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] mn = br.readLine().split(" ");
        int m = Integer.parseInt(mn[0]);
        int n = Integer.parseInt(mn[1]);

        arr = new int[m+1][n+1];

        for (int i = 1; i < m+1; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 1; j < n+1; j++) {
                arr[i][j] = Integer.parseInt(line[j-1]) + arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1];
            }
        }

        int cases = Integer.parseInt(br.readLine());

        for (int i = 0; i < cases; i++) {
            String[] xys = br.readLine().split(" ");
            int x1 = Integer.parseInt(xys[0]);
            int y1 = Integer.parseInt(xys[1]);
            int x2 = Integer.parseInt(xys[2]);
            int y2 = Integer.parseInt(xys[3]);

            bw.write(getPeople(x1, y1, x2, y2) + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    private static int getPeople(int x1, int y1, int x2, int y2) {
        return arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1];
    }

}
