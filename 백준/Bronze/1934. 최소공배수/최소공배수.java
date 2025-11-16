// 백준 1934번 : 최대공배수

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
  유클리드 호제법''
  GCD = Greatest Common Divisor ( 최대공약수 )
  GCD(a,b) = GCD(b,r)
  최대공배수 = a * b / GCD(a,b)
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cases = Integer.parseInt(br.readLine());

        for (int c = 0; c < cases; c++) {
            String[] line = br.readLine().split(" ");
            int a = Integer.parseInt(line[0]);
            int b = Integer.parseInt(line[1]);

            int gcd = getGCD(a, b);
            System.out.println((a*b)/gcd);
        }
    }

    private static int getGCD(int a, int b) {

        if (b == 0) return a;

        return getGCD(b,a%b);

    }

}
