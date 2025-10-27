

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inps = br.readLine().split(" ");
        int n = Integer.parseInt(inps[0]);
        int k = Integer.parseInt(inps[1]);

        // 최소 필요한 공의 개수: 1+2+3+...+k
        int minBalls = k * (k + 1) / 2;

        if (n < minBalls) {
            System.out.println(-1);
            return;
        }

        // 남은 공
        int remaining = n - minBalls;

        // 남은 공을 k개 바구니에 균등 분배
        // 각 바구니에 remaining/k 개씩 추가하면
        // 최소: 1 + remaining/k
        // 최대: k + remaining/k
        // 만약 remaining이 k로 나누어떨어지면 차이는 k-1
        // 나누어떨어지지 않으면 차이는 k

        if (remaining % k == 0) {
            System.out.println(k - 1);
        } else {
            System.out.println(k);
        }

        br.close();
    }
}
