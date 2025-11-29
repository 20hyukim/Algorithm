import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

// 백준 2407번 : 조합
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");

        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        BigInteger combination;

        combination = factorial(BigInteger.valueOf(n))
                .divide(factorial(BigInteger.valueOf(m)));


        combination = combination.divide(factorial(BigInteger.valueOf(n-m)));

        System.out.println(combination);
    }

    private static BigInteger factorial(BigInteger n) {
        if (n.equals(BigInteger.ONE) || n.equals(BigInteger.ZERO)) {
            return BigInteger.ONE;
        }

        return n.multiply(factorial(n.subtract(BigInteger.ONE)));
    }
}
