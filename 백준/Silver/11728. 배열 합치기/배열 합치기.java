import java.io.*;
import java.util.ArrayList;
import java.util.List;

// 백준 11728번 : 배열 합치기 - 새로운 풀이
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] ab = br.readLine().split(" ");
        int a = Integer.parseInt(ab[0]);
        int b = Integer.parseInt(ab[1]);

        String[] aArr = br.readLine().split(" ");
        String[] bArr = br.readLine().split(" ");

        int ai = 0;
        int bi = 0;

        List<String> arr = new ArrayList<>();

        while (ai < a && bi < b) {
            if (Integer.parseInt(aArr[ai]) <= Integer.parseInt(bArr[bi])) {
                arr.add(aArr[ai++]);
            } else {
                arr.add(bArr[bi++]);

            }
        }


        while (ai < a) {
            arr.add(aArr[ai++]);
        }
        while (bi < b) {
            arr.add(bArr[bi++]);
        }

        for(int i = 0; i < a+b; i++) {
            bw.write(arr.get(i)+ " ");
        }

        bw.flush();
        bw.close();
        br.close();
    }

}
