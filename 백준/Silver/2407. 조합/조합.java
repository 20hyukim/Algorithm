import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

import static java.math.BigInteger.ZERO;

// 백준2407번 : 조합
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int n = Integer.parseInt(inp[0]);
        int m = Integer.parseInt(inp[1]);

        BigInteger answer = ZERO;

        answer = factorial(n).divide((factorial(n-m).multiply(factorial(m))));

        System.out.println(answer);
    }

    public static BigInteger factorial(int n){
        if (n == 1) {
            return BigInteger.ONE;
        }

        return BigInteger.valueOf(n).multiply(factorial(n-1));
    }

}
