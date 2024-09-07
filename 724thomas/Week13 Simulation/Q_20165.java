// https://www.acmicpc.net/problem/
package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

class Q_20165 {
    public static void main(String[] args) throws IOException {
        Map<Character, int[]> directions = new HashMap<>();
        directions.put('W', new int[]{0,-1});
        directions.put('E', new int[]{0,1});
        directions.put('N', new int[]{-1,0});
        directions.put('S', new int[]{1,0});

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputs = br.readLine().split(" ");
        int trow = Integer.parseInt(inputs[0]), tcol = Integer.parseInt(inputs[1]), rounds = Integer.parseInt(inputs[2]);

        int[][] matrix= new int[trow][tcol];
        char[][] visited = new char[trow][tcol];

        for (int i=0; i<trow; i++) {
            String[] crow = br.readLine().split(" ");
            for (int j=0; j<tcol; j++){
                matrix[i][j] = Integer.parseInt(crow[j]);
                visited[i][j] = 'S';
            }
        }

        int ans = 0;
        for (int round=0; round<rounds; round++) {
            String[] a = br.readLine().split(" ");
            String[] b = br.readLine().split(" ");

            int x = Integer.parseInt(a[0])-1, y = Integer.parseInt(a[1])-1;
            char d = a[2].charAt(0);
            int[] direction = directions.get(d);
            int nx = direction[0], ny = direction[1];

            if (visited[x][y]=='S') {
                int cmax = matrix[x][y];
                while (cmax > 0 && x>=0 && y>=0 && x<trow && y<tcol) {
                    if (visited[x][y]=='S') {
                        visited[x][y]='F';
                        cmax = Math.max(cmax-1, matrix[x][y]-1);
                        ans++;
                    } else {
                        cmax--;
                    }
                    x += nx;
                    y += ny;
                }
            }
            x = Integer.parseInt(b[0])-1;
            y = Integer.parseInt(b[1])-1;
            visited[x][y]='S';
        }
        System.out.println(ans);

        for (int i = 0; i < trow; i++) {
            for (int j = 0; j < tcol; j++) {
                System.out.print(visited[i][j] + " ");
            }
            System.out.println();
        }
    }
}
