import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] words = new String[5];

        int max_len = 0;

        for (int i = 0; i < 5; i++) {
            words[i] = br.readLine();
            max_len = Math.max(max_len, words[i].length());
        }

        for (int l = 0; l < max_len; l++) {
            for (int w = 0; w < 5; w++) {

                if (words[w].length() > l) {
                    sb.append(words[w].charAt(l));
                }
            }
        }

        System.out.println(sb);
    }
}
