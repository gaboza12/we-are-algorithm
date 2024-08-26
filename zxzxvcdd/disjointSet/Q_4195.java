package zxzxvcdd.disjointSet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/*
문제
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
 */

public class Q_4195 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        class Union {

            int[] parent;
            int[] count;

            public Union(int size) {
                parent = new int[size];
                count = new int[size];
                for (int i = 0; i < size; i++) {
                    parent[i] = i;
                    count[i] = 1;
                }
            }

            int getParent(int i) {
                if (parent[i] == i) return i;

                return parent[i] = getParent(parent[i]);
            }

            void union(int a, int b) {
                a = getParent(a);
                b = getParent(b);
                if (a != b) {
                    boolean flag = a > b;
                    int min = flag ? b : a;
                    int max = flag ? a : b;
                    count[min] += count[max];
                    parent[max] = min;
                }
            }

            int getCount(int a) {
                return count[getParent(a)];
            }
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder();

        int testCount = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCount; i++) {

            int friendshipCount = Integer.parseInt(br.readLine());

            Union union = new Union(friendshipCount * 2);
            Map<String, Integer> userMap = new HashMap<>();
            int index = 0;

            for (int j = 0; j < friendshipCount; j++) {

                StringTokenizer inputToken = new StringTokenizer(br.readLine());
                String userA = inputToken.nextToken();
                String userB = inputToken.nextToken();

                if (!userMap.containsKey(userA)) userMap.put(userA, index++);
                if (!userMap.containsKey(userB)) userMap.put(userB, index++);

                union.union(userMap.get(userA), userMap.get(userB));

                result.append(union.getCount(userMap.get(userA)) + "\n");
            }
        }
        System.out.println(result.toString());
    }
}
