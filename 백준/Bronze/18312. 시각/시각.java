import java.io.*;

// 백준 18312번 : 시각
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] nk = br.readLine().split(" ");
        int n = Integer.parseInt(nk[0]);
        int k = Integer.parseInt(nk[1]);

        int hours = 0, minutes = 0, seconds= 0, cnt = 0;

        while (hours <= n) {
            if (containsRequiredNum(hours, k) ||
                containsRequiredNum(minutes, k) ||
                containsRequiredNum(seconds, k)) cnt++;

            seconds ++;
            if (seconds == 60) {
                seconds = 0;
                minutes ++;
                if (minutes == 60) {
                    minutes = 0;
                    hours++;
                }
            }
        }

        bw.write(String.valueOf(cnt));
        bw.flush();

        bw.close();
        br.close();
    }

    private static boolean containsRequiredNum(int num, int k) {
        if (num / 10 == 0 && k == 0) return true;
        return String.valueOf(num).contains(String.valueOf(k));
    }
}
