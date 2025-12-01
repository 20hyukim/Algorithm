import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 백준 1543번 : 문서 검색 - 틀린 답
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String doc = br.readLine();
        String word = br.readLine();

        int cnt = 0;
        int idx = 0;

        while(true) {
            idx = doc.indexOf(word, idx);
            if (idx == -1) break;

            cnt++;
            idx += word.length();
        }

        System.out.println(cnt);
    }
}
