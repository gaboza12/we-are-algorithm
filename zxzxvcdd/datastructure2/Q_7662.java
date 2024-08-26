package zxzxvcdd.datastructure2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Q_7662 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCount = Integer.parseInt(br.readLine());
        StringBuilder resultBuilder = new StringBuilder();
        
        for (int i = 0; i < testCount; i++) {

            int inputCount = Integer.parseInt(br.readLine());
            TreeMap<Integer, Integer> tree = new TreeMap<>();

            for (int j = 0; j < inputCount; j++) {

                
                StringTokenizer inputToken = new StringTokenizer(br.readLine());
                String initial = inputToken.nextToken();
                int value = Integer.parseInt(inputToken.nextToken());

                switch (initial) {
                    case "I":
                        tree.put(value,tree.getOrDefault(value, 0)+1);
                        break;
                    case "D":
                        if (!tree.isEmpty()) {
                            int target = (value == 1) ? tree.lastKey() : tree.firstKey();
                            int targetCount = tree.get(target);
                            if (targetCount == 1) {
                                tree.remove(target);
                            } else {
                                tree.put(target, targetCount - 1);
                            }
                        }
                        break;
                }

            }

            if (tree.isEmpty()) {
                resultBuilder.append("EMPTY\n");
            } else {
                resultBuilder.append(tree.lastKey()).append(" ").append(tree.firstKey()).append("\n");
            }
        }
        System.out.println(resultBuilder.toString());
    }
}
