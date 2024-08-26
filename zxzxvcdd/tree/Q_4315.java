package zxzxvcdd.tree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_4315 {

    static int moveCount;
    static int[] tree = null;
    static int[] treeValue = null;

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer results = new StringBuffer();
        StringTokenizer inputToken;
        
        while (true) {

            int nodeCount = Integer.parseInt(br.readLine());
            if (nodeCount == 0)
                break;

            tree = new int[nodeCount + 1];
            treeValue = new int[nodeCount + 1];

            moveCount = 0;
            for (int i = 0; i < nodeCount; i++) {
                inputToken = new StringTokenizer(br.readLine());
                int parentNode = Integer.parseInt(inputToken.nextToken());
                int beads = Integer.parseInt(inputToken.nextToken());
                treeValue[parentNode] = beads;
                int childNodes = Integer.parseInt(inputToken.nextToken());
                for (int j = 0; j < childNodes; j++) {
                    int childNode = Integer.parseInt(inputToken.nextToken());
                    tree[childNode] = parentNode;
                }
            }
            int root = findRootNode();
            distribute(root);
            results.append(moveCount + "\n");

        }

        System.out.println(results.toString());
    }

    private static int findRootNode() {
        for (int i = 1; i <= tree.length; i++) {
            if (tree[i] == 0) {
                return i;
            }
        }
        return 1;
    }

    static int distribute(int index) {

        int beads = treeValue[index];

        for (int i = 1; i < tree.length; i++) {
            if (tree[i] == index) {
                beads += distribute(i);
            }
        }

        moveCount += Math.abs(beads - 1);
        return beads - 1;

    }
}
