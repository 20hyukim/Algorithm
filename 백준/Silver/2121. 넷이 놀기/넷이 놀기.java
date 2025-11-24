import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Set<Point> set = new HashSet<>();

        int points = Integer.parseInt(br.readLine());
        String[] nm = br.readLine().split(" ");
        int a = Integer.parseInt(nm[0]);
        int b = Integer.parseInt(nm[1]);

        for (int i = 0; i < points; i++) {
            String[] xy = br.readLine().split(" ");
            int x = Integer.parseInt(xy[0]);
            int y = Integer.parseInt(xy[1]);

            set.add(new Point(x, y));
        }

        int cnt = 0;
        for (Point p : set) {
            if (set.contains(new Point(p.x + a, p.y)) &&
                    set.contains(new Point(p.x+a, p.y + b)) &&
                    set.contains(new Point(p.x, p.y + b))
            ) cnt++;
        }

        System.out.println(cnt);

    }
}
