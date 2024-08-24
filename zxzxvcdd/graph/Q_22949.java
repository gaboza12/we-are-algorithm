package zxzxvcdd.graph;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class Q_22949 {
    static class Pos{
        int r, c, rotateState, time;
        public Pos(int r, int c, int rotateState, int time) {
            this.r = r;
            this.c = c;
            this.rotateState = rotateState;
            this.time = time;
        }
    }

    private static final int[] dr = {0, 1, -1, 0, 0};
    private static final int[] dc = {0, 0, 0, 1, -1};
    static int n;
    static Queue<Pos> q;
    static boolean[][][] visited;
    static char[][][] map;

    public static void main(String[] args) throws Exception {
       
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in), 1<<16);

        n = Integer.parseInt(br.readLine());
        map = new char[4][n*4][n*4];
        Pos start = null;
        for (int i = 0; i < 4*n; i++) {
            map[0][i] = br.readLine().toCharArray();
            for (int j = 0; j < 4*n; j++) {
                if (map[0][i][j]=='S') {
                    start = new Pos(i, j, 0, 0);
                }
                int tmpI = i;
                int tmpJ = j;
                for (int x = 1; x <= 3; x++) {
                    int[] nextPos = getRotatedPos(tmpI, tmpJ);
                    tmpI = nextPos[0];
                    tmpJ = nextPos[1];
                    map[x][tmpI][tmpJ] = map[0][i][j];
                }
            }
        }

        visited = new boolean[4][n*4][n*4];
        q = new ArrayDeque<>();
        q.add(start);
        visited[0][start.r][start.c] = true;

        getResult();

    }

    public static void getResult(){
        
        while (!q.isEmpty()) {
            Pos user = q.poll();
            int r = user.r;
            int c = user.c;
            int rotateState = user.rotateState;

            if (map[rotateState][r][c] == 'E') {
                System.out.println(user.time+1);
                return;
            }

            int currentDiv = getDivision(r, c);
            for (int dir = 0; dir < 5; dir++) {
                int nr = r+dr[dir];
                int nc = c+dc[dir];
                int newDiv = getDivision(nr, nc);
                if (newDiv == -1) continue;
                int nd = currentDiv == newDiv ? (rotateState+1)%4 : 1;
                int[] nrc = getRotatedPos(nr, nc);
                nr = nrc[0];
                nc = nrc[1];

                if (visited[nd][nr][nc] || map[nd][nr][nc] == '#') continue;
                visited[nd][nr][nc] = true;
                q.add(new Pos(nr, nc, nd, user.time+1));
            }
        }
        System.out.println(-1);
    }

    
    private static int getDivision(int r, int c) {
        if (r<0 || c<0 || r>=4*n || c>=4*n) return -1;
        return r/4*4+c/4;
    }

    private static int[] getRotatedPos(int r, int c) {
        int baseR = r/4*4;
        int baseC = c/4*4;
        r %= 4;
        c %= 4;
        return new int[]{baseR+c, baseC+3-r};
    }
}

