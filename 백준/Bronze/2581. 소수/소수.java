import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int m = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());

        int total = 0;
        int minVal = 0;

        for (int i = m; i < n+1; i++) {
            if (isPrime(i)) {
                total += i;
                if (total == i) {
                    minVal = i;
                }
            }
        }

        if (total == 0) {
            bw.write(String.valueOf(-1));
        } else {
            bw.write(total + "\n");
            bw.write(String.valueOf(minVal));
        }
        bw.flush();
        bw.close();
        br.close();
    }

    private static boolean isPrime(int n) {
        if (n==1) return false;
        int rooted = (int)Math.sqrt(n) + 1;
        for (int i = 2; i < rooted; i++) {
            if ( n % i == 0) return false;
        }
        return true;
    }
}
