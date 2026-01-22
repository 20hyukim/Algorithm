import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;

// 백준 22864번 : 피로도
public class Main {
    static int workH = 0;
    static int tired = 0;
    static int a;
    static int b;
    static int c;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inp = br.readLine().split(" ");

        a = Integer.parseInt(inp[0]);
        b = Integer.parseInt(inp[1]);
        c = Integer.parseInt(inp[2]);
        int m = Integer.parseInt(inp[3]);

        for (int i = 0; i < 24; i++) {
            if (tired + a > m) {
                rest();
                continue;
            }
            work();
        }

        System.out.println(workH);
    }

    private static void rest() {
        tired -= c;
        if (tired < 0) tired = 0;
    }

    private static void work() {
        tired += a;
        workH += b;
    }
}
