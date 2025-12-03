import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inp = br.readLine().split(" ");

        int n = Integer.parseInt(inp[0]);
        int k = Integer.parseInt(inp[1]);

        String[] nums = br.readLine().split(" ");

        int cur_value = 0;
        for (int i = 0; i < k; i++) {
            cur_value += Integer.parseInt(nums[i]);
        }


        int start_idx = 0;
        int end_idx = k;
        int max_value = cur_value;

        for (int i = 0; i < n-k; i++) {

            cur_value = cur_value + Integer.parseInt(nums[end_idx]) - Integer.parseInt(nums[start_idx]);

            max_value = Math.max(max_value, cur_value);
            end_idx++;
            start_idx++;

        }

        System.out.println(max_value);
    }
}
