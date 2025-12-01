import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Set<String> set = new HashSet<>();

        br.readLine();

        String[] cards = br.readLine().split(" ");

        set.addAll(Arrays.asList(cards));

        int cont_num = Integer.parseInt(br.readLine());
        String[] cont_card = br.readLine().split(" ");
        int[] answer = new int[cont_num];

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < cont_num; i++) {
            if (set.contains(cont_card[i])) answer[i] = 1;
            sb.append(answer[i]).append(" ");
        }

        System.out.println(sb);
    }
}
