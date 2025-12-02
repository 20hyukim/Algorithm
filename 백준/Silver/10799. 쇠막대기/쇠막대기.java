import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inps = br.readLine();

        inps = inps.replace("()", "R");

        int len = inps.length();

        int cnt = 0;
        int overlap = 0;
        for (int i = 0; i < len; i++) {
            if (inps.charAt(i) == 'R') {
                cnt += overlap;
                continue;
            }
            if (inps.charAt(i) == '(') {
                overlap ++;
                continue;
            }
            cnt ++;
            overlap --;
        }

        System.out.println(cnt);
    }
}
