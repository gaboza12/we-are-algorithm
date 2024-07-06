package zxzxvcdd.tree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Q_3548 {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCount = Integer.parseInt(br.readLine());

        StringBuffer results = new StringBuffer();
        StringTokenizer inputToken;
        for (int i = 0; i < testCount; i++) {

            int nodeCount = Integer.parseInt(br.readLine());

            int[] tree = new int[nodeCount + 1];
            for (int j = 0; j < nodeCount - 1; j++) {

                inputToken = new StringTokenizer(br.readLine());

                int parentNode = Integer.parseInt(inputToken.nextToken());
                int childNode = Integer.parseInt(inputToken.nextToken());
                tree[childNode] = parentNode;

            }

            inputToken = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(inputToken.nextToken());
            int node2 = Integer.parseInt(inputToken.nextToken());

            String result = getResult(node1, node2, tree);
            results.append(result);

        }

        System.out.println(results.toString());

    }

    static String getResult(int node1, int node2, int[] tree) {

        Set<Integer> parentSet = new HashSet<>();
        String result = "";

        parentSet.add(node1);
        parentSet.add(node2);
        for (int i = 0; i < 2; i++) {
            int target = (i == 0) ? node1 : node2;

            while (true) {
                int parentNode = tree[target];

                if (parentNode == 0)
                    break;

                if (parentSet.contains(parentNode)) {
                    result = parentNode + "\n";
                    break;
                } else {
                    parentSet.add(parentNode);
                    target = parentNode;
                }
            }
        }
        return result;
    }

}
