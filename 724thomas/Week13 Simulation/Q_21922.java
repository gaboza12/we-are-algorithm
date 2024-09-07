// https://www.acmicpc.net/problem/
package 백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Q_21922 {

    static int getDirection(int direction, int value) { // 1 Up, 2 Down, 3 Left, 4 Right
        if (value == 1) {
            if (direction == 1) {
                return 1;
            } else if (direction == 2){
                return 2;
            } else if (direction == 3){
                return 4;
            } else if (direction == 4){
                return 3;
            }
        } else if (value == 2) {
            if (direction == 1) {
                return 2;
            } else if (direction == 2){
                return 1;
            } else if (direction == 3){
                return 3;
            } else if (direction == 4){
                return 4;
            }
        } else if (value == 3) {
            if (direction == 1) {
                return 4;
            } else if (direction == 2){
                return 3;
            } else if (direction == 3){
                return 2;
            } else if (direction == 4){
                return 1;
            }
        } else if (value == 4) {
            if (direction == 1) {
                return 3;
            } else if (direction == 2) {
                return 4;
            } else if (direction == 3) {
                return 1;
            } else if (direction == 4) {
                return 2;
            }
        }
        return direction;
    }

    static int bfs(int[][] matrix, int row, int col, Map<Integer, int[]> directions, boolean[][] visited){
        int count = 1;
        Queue<int[]> queue = new LinkedList<>();
        for (int i=1; i<=4; i++) {
            queue.offer(new int[]{row, col, i});
            visited[row][col] = true;
        }

        while (!queue.isEmpty()) {
            int[] temp = queue.poll();
            int x = temp[0], y = temp[1], dir = temp[2];

            int nextDirection = getDirection(dir, matrix[x][y]);
            int[] next_dir = directions.get(nextDirection);
            x += next_dir[0];
            y += next_dir[1];

            if (x >= 0 && y >= 0 && x < matrix.length && y < matrix[0].length && matrix[x][y] != 9) {
                queue.offer(new int[]{x, y, nextDirection});
                if (!visited[x][y]){
                    count++;
                    visited[x][y] = true;
                }
            }
        }
        return count;
    }
    public static void main(String[] args) throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] firstLine = br.readLine().split(" ");
        int trow = Integer.parseInt(firstLine[0]), tcol = Integer.parseInt(firstLine[1]);

        int[][] matrix = new int[trow][tcol];
        for (int i = 0; i < trow; i++) {
            String[] row = br.readLine().split(" ");
            for (int j = 0; j < tcol; j++) {
                matrix[i][j] = Integer.parseInt(row[j]);
            }
        }

        Map<Integer, int[]> directions = new HashMap<>();
        directions.put(1, new int[]{-1,0});
        directions.put(2, new int[]{1,0});
        directions.put(3, new int[]{0,-1});
        directions.put(4, new int[]{0,1});

        boolean [][] visited = new boolean[trow][tcol];
        int ans = 0;
        for (int row=0; row<trow; row++) {
            for (int col=0; col<tcol; col++) {
                if (matrix[row][col] == 9){
                    ans += bfs(matrix, row, col, directions, visited);
                }
            }
        }
        System.out.println(ans);
    }
}
