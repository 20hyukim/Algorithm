import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        bw.write(isYoon(n) + "");

        bw.flush();
        bw.close();
        br.close();
    }

    private static int isYoon(int n) {
        boolean req1 = getReq1(n);
        boolean req2 = getReq2(n);

        if (req1 || req2) return 1;
        return 0;
    }

    private static boolean getReq1(int n) {
        return n % 4 == 0 && n % 100 != 0;
    }

    private static boolean getReq2(int n) {
        return n % 400 == 0;
    }
}
