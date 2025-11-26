import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int cases = Integer.parseInt(br.readLine());

        for (int c = 0; c < cases; c++) {
            String[] nums = br.readLine().split(" ");

            int[] num = new int[Integer.parseInt(nums[0])];

            for (int i = 1 ; i < nums.length; i++) {
                num[i-1] = Integer.parseInt(nums[i]);
            }

            long total = 0;
            for (int i = 0; i < num.length -1 ; i++) {
                for (int j = i+1; j < num.length; j++) {
                    total += gcd(num[i], num[j]);
                }
            }

            System.out.println(total);
        }
    }

    private static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a%b);
    }
}
