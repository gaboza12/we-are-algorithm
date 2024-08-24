package zxzxvcdd.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q_4179 {
    public static int n, m, result;
    public static int[] dr = {0, 0, -1, 1};
    public static int[] dc = {-1, 1, 0, 0};
    public static char[][] map;

    public static class Node {
        int r;
        int c;
        int time;

        public Node(int r, int c, int time) {
            this.r = r;
            this.c = c;
            this.time = time;
        }
    }

    public static Queue<Node> user, fire;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer input = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(input.nextToken());
        m = Integer.parseInt(input.nextToken());
        user = new LinkedList<>();
        fire = new LinkedList<>();

        map = new char[n][m];
        for (int i = 0; i < n; i++) {
            map[i] = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 'J') {
                    user.offer(new Node(i, j, 0));
                }

                if (map[i][j] == 'F') {
                    fire.offer(new Node(i, j, 0));
                }
            }
        }

        result = 0;

        if (getResult()) {
            System.out.println("IMPOSSIBLE");
        } else {
            System.out.println(result);
        }
    }

    public static boolean getResult() {

        while (!user.isEmpty()) {
            int fireCount = fire.size();
            for (int i = 0; i < fireCount; i++) {
                Node node = fire.poll();

                for (int d = 0; d < 4; d++) {
                    int nr = node.r + dr[d];
                    int nc = node.c + dc[d];
                    if (0 <= nr && 0 <= nc && nr < n && nc < m ) {
                        if (map[nr][nc] != '#' && map[nr][nc] != 'F') {
                            map[nr][nc] = 'F';
                            fire.offer(new Node(nr, nc, node.time + 1));
                        }
                    }
                }
            }

            int userCount = user.size();

            for (int i = 0; i < userCount; i++) {
                Node node = user.poll();

                for (int d = 0; d < 4; d++) {
                    int nr = node.r + dr[d];
                    int nc = node.c + dc[d];
                    if (nr<0 || nc<0 || nr>=n || nc>=m) {
                        result = node.time + 1;
                        return false;
                    }

                    if (map[nr][nc] != '#' && map[nr][nc] != 'F' && map[nr][nc] != 'J') {
                        user.offer(new Node(nr, nc, node.time + 1));
                        map[nr][nc] = 'J';
                    }
                }
            }
        }
        return true;
    }
}
