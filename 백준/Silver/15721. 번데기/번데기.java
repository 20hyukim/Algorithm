import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 백준 15721: 번데기
public class Main {
    static int a;
    static int t;
    static int isDeggi;

    static int deggi = 0;
    static int bbun = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        a = Integer.parseInt(br.readLine());
        t = Integer.parseInt(br.readLine());
        isDeggi = Integer.parseInt(br.readLine());
        int cnt = -1;
        int repeat = 2;
        while (true) {
            for (int i = 0; i < 4; i++) {
                cnt++;
                if (i%2 == 0) {
                    bbun++;
                    if (bbunTime(cnt)) return;
                } else {
                    deggi++;
                    if (deggiTime(cnt)) return;
                }
            }

            for (int i = 0; i < repeat; i++) {
                cnt++;
                bbun++;
                if (bbunTime(cnt)) return;
            }

            for (int i = 0; i < repeat; i++) {
                cnt++;
                deggi++;
                if (deggiTime(cnt)) return;
            }
            repeat++;
        }
    }


    private static boolean deggiTime(int cnt) {
        if (isDeggi == 1 && deggi == t) {
            System.out.println(cnt % a);
            return true;
        }
        return false;
    }

    private static boolean bbunTime(int cnt) {
        if (isDeggi == 0 && bbun == t) {
            System.out.println(cnt % a);
            return true;
        }
        return false;
    }


}
