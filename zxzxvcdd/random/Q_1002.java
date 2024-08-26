package zxzxvcdd.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_1002 {
/*
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
조규현의 좌표 $(x_1, y_1)$와 백승환의 좌표 $(x_2, y_2)$가 주어지고, 조규현이 계산한 류재명과의 거리 $r_1$과 백승환이 계산한 류재명과의 거리 $r_2$가 주어졌을 때, 
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

조규현은 각 좌표에서 r의 길이를 반지름으로 가진 원을 그렸을 때
원의 둘레 중 어딘가에 위치하게 된다. 

따라서 각 좌표에서 원을 그리고 그 원이 만나거나 만나지 않을 경우로 좌표의 수를 구하면 된다.

이석원과 백승환 사이의 거리를 구한다
- 피타고라스의 정리 a^2 + b^2 = c^2 
- x의 차와 y의 차의 제곱을을 더해 두 좌표간 거리의 제곱을 구한다.

거리와 r의 제곱을 비교하여 결과를 연산
 * 
 */
    public static void main(String[] args) throws NumberFormatException, IOException {

        class DistanceInfo {
            int x;
            int y;
            int r;
            public DistanceInfo(StringTokenizer token) {

                this.x = Integer.parseInt(token.nextToken());
                this.y = Integer.parseInt(token.nextToken());
                this.r = Integer.parseInt(token.nextToken());
            }
            @Override
            public String toString() {
                return "x : " + x + " y : " + y + " r : " + r;
            }

            @Override
            public boolean equals(Object obj) {
                return (this.toString().equals(obj.toString()));
            }

        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCount = Integer.parseInt(br.readLine());
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < testCount; i++) {

            StringTokenizer inputToken = new StringTokenizer(br.readLine());

            DistanceInfo lee = new DistanceInfo(inputToken);
            DistanceInfo baek = new DistanceInfo(inputToken);

            if (lee.equals(baek))
                result.append("-1\n");
            else {
                
                double distance = Math.pow(lee.x - baek.x, 2) + Math.pow(lee.y - baek.y, 2);
                double sumRadius = Math.pow(lee.r + baek.r, 2);
                double subRadius = Math.pow(lee.r - baek.r, 2);

                if (distance > sumRadius || distance < subRadius) {
                    result.append("0\n");
                } else if (distance == subRadius || distance == sumRadius) {
                    result.append("1\n");
                } else {
                    result.append("2\n");
                }

            }
        }

        System.out.println(result.toString());

    }
}
