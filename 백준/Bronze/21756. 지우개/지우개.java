import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        if (n == 1) {
            System.out.println(1);
            return;
        }

        int root_n = (int)Math.sqrt(n);
        int result = (int)Math.pow(2, root_n);


        if (result*2 == n) {
            System.out.println(result * 2);
            return;
        }

        System.out.println((int)Math.pow(2, root_n));
    }
}
