import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Objects;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Deque<String> stack = new ArrayDeque<>();

        int cases = Integer.parseInt(br.readLine());

        for (int i = 0; i < cases; i++) {
            String[] inp = br.readLine().split(" ");

            if (inp[0].equals("push")) {
                stack.addLast(inp[1]);
                continue;
            }
            if (inp[0].equals("top")) {
                bw.write(stack.isEmpty() ? "-1" : stack.peekLast());
                bw.write("\n");
                continue;
            }
            if (inp[0].equals("size")) {
                bw.write(stack.isEmpty() ? "0" : String.valueOf(stack.size()));
                bw.write("\n");
                continue;
            }
            if (inp[0].equals("empty")) {
                bw.write(stack.isEmpty()? "1" : "0");
                bw.write("\n");
                continue;
            }
            if (inp[0].equals("pop")) {
                bw.write(stack.isEmpty()? "-1" : stack.removeLast());
                bw.write("\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
