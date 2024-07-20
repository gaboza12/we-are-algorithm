package zxzxvcdd.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;


public class Q_24479{
    
    static List<Integer>[] nodeList;
    static boolean[] checkList;
    static int[] visited;
    static int cnt;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer inputToken = new StringTokenizer(br.readLine());

        int nodes = Integer.parseInt(inputToken.nextToken());
        int lines = Integer.parseInt(inputToken.nextToken());
        int root = Integer.parseInt(inputToken.nextToken());

        checkList = new boolean[nodes + 1];
        visited = new int[nodes + 1];

        nodeList = new ArrayList[nodes+1];

        for (int i = 1; i <= nodes; i++) {
            nodeList[i] = new ArrayList<>();
        }

        for (int i = 0; i < lines; i++) {
            inputToken = new StringTokenizer(br.readLine());
            int parentIndex = Integer.parseInt(inputToken.nextToken());
            int linkedIndex = Integer.parseInt(inputToken.nextToken());

            nodeList[parentIndex].add(linkedIndex);
            nodeList[linkedIndex].add(parentIndex);

        }
        
        for (int i = 1; i <= nodes; i++) {
            Collections.sort(nodeList[i]);
        }

        cnt = 1;
        getResult(root);

        StringBuffer result = new StringBuffer();
        for (int i = 1; i <= nodes; i++) {
            result.append(visited[i]).append("\n");

        }
        System.out.print(result.toString());
    }

    static void getResult(int index) {
        checkList[index] = true;
        visited[index] = cnt++;

        for (int i : nodeList[index]) {
            if (!checkList[i]) {
                getResult(i);
            }
        }
    }

}