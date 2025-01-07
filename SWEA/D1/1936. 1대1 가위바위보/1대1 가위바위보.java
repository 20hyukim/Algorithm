
import java.io.File;
import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
    public static void main(String args[]) throws Exception
    {

        Scanner sc = new Scanner(System.in);
//        int T; // 테스트 케이스 수
//        T = sc.nextInt(); // 테스트 케이스 수 입력 받기

        // T개의 테스트 케이스 처리
        for (int test_case = 1; test_case <= 1; test_case++) {
            // A와 B의 입력값을 읽음
            int A = sc.nextInt(); // A가 낸 가위(1), 바위(2), 보(3)
            int B = sc.nextInt(); // B가 낸 가위(1), 바위(2), 보(3)

            // 가위바위보 규칙에 따라 승자 판별
            if ((A == 1 && B == 3) || (A == 2 && B == 1) || (A == 3 && B == 2)) {
                System.out.println("A"); // A가 승리
            } else {
                System.out.println("B"); // B가 승리
            }
        }

        sc.close(); // Scanner 객체 닫기
    }
}