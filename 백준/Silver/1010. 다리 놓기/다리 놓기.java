import java.io.*;
import java.math.BigInteger;

public class Main {
    static BigInteger[] fact = new BigInteger[31];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int cases = Integer.parseInt(br.readLine());

        for (int i = 0; i < cases; i++ ) {
            String[] nm = br.readLine().split(" ");

            int n = Integer.parseInt(nm[0]);
            int m = Integer.parseInt(nm[1]);

            BigInteger result = factorial(m).divide((factorial(n).multiply(factorial(m-n))));
            bw.write(result + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    private static BigInteger factorial(long n) {
        if (n==1 || n==0) return BigInteger.ONE;
        if (fact[(int) n] != null) return fact[(int)n];

        fact[(int)n] = BigInteger.valueOf(n).multiply(factorial(n-1));

        return fact[(int)n];
    }

}
