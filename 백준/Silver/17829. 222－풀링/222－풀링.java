import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    static int[][] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int len = Integer.parseInt(br.readLine());
        int repeat = (int)(Math.log(len) / Math.log(2));;
        arr = new int[len][len];

        for (int i = 0; i < len; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < len; j++) {
                arr[i][j] = Integer.parseInt(line[j]);
            }
        }

        System.out.println(getResult(repeat, 0, 0));

    }

    private static int getResult(int repeat, int i, int j) {
        if (repeat == 1) {
            List<Integer> secondList = new ArrayList<>();

            secondList.add(arr[i][j]);
            secondList.add(arr[i][j+1]);
            secondList.add(arr[i+1][j]);
            secondList.add(arr[i+1][j+1]);

            secondList.sort(Collections.reverseOrder());

            return secondList.get(1);
        }

        repeat --;
        int len = (int)Math.pow(2, repeat);

        List<Integer> secondList = new ArrayList<>();
        secondList.add(getResult(repeat, i, j));
        secondList.add(getResult(repeat, i, j+len));
        secondList.add(getResult(repeat, i+len, j));
        secondList.add(getResult(repeat, i+len, j+len));

        secondList.sort(Collections.reverseOrder());

        return secondList.get(1);
    }
}
