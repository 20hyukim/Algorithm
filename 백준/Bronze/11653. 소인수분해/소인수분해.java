import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int max_n = n;

        INIT : while (n != 1) {
            for (int i = 2; i < max_n + 1; i++) {
                if (n % i == 0) {
                    System.out.println(i);
                    n = n/i;
                    continue INIT;
                }
            }
        }
    }
}
