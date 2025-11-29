import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 백준 2121번 : 넷이 놀기
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Set<Point> set = new HashSet<>();

        int cases = Integer.parseInt(br.readLine());

        String[] ab = br.readLine().split(" ");
        int a = Integer.parseInt(ab[0]);
        int b = Integer.parseInt(ab[1]);



        for (int i = 0; i < cases; i++) {
            String[] point = br.readLine().split(" ");
            int x = Integer.parseInt(point[0]);
            int y = Integer.parseInt(point[1]);
            set.add(new Point(x, y));
        }

        int cnt = 0;

        for(Point p: set) {
            if (set.contains(new Point(p.x+a, p.y))
            && set.contains(new Point(p.x, p.y + b))
            && set.contains(new Point(p.x+a, p.y+b))) {
                cnt++;
            }
        }

        System.out.println(cnt);

    }
}
