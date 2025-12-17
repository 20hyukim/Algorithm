import java.io.*;
import java.util.PriorityQueue;
import java.util.TreeMap;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        PriorityQueue<Integer> queue = new PriorityQueue<>();

        String[] ab = br.readLine().split(" ");

        for(String n: ab) {
            String[] nums = br.readLine().split(" ");
            for (int i = 0; i < Integer.parseInt(n); i++) {
                queue.add(Integer.parseInt(nums[i]));
            }

        }

        while (!queue.isEmpty()) {
            Integer n = queue.poll();
            bw.write(n+ " ");
        }
        bw.flush();
        bw.close();
        br.close();

    }

//    private static PriorityQueue<String> addNumber(BufferedReader br, int n) throws IOException {
//        String[] nums = br.readLine().split(" ");
//
//        for (int i = 0; i < n; i++) {
//            System.out.println(nums[i]);
//            queue.add(String.valueOf(nums[i]));
//        }
//        return queue;
//    }
}
