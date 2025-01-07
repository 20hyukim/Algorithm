
import java.util.Scanner;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        String T;
        // 한줄 받아오기
        T = sc.nextLine();

        //""로 분리
        String[] inp = T.split("");
        int n = inp.length;

        int total = 0;
        for (int i = 0; i < n; i++) {
            total += Integer.parseInt(inp[i]);
        }

        System.out.println(total);

        sc.close();
    }
}