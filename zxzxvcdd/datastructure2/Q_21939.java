package zxzxvcdd.datastructure2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Q_21939 {

    public static void main(String[] args) throws NumberFormatException, IOException {
        
        class Question implements Comparable<Question>{

            int level;
            int num;


            public Question(int num, int level) {
                this.level = level;
                this.num = num;
            }

            @Override
            public int compareTo(Question q) {

                if (level - q.level == 0) {
                    return num - q.num;
                } else {
                    return level - q.level;
                }
            }
            @Override
            public int hashCode() {
                int result = Integer.hashCode(num);
                result = 31 * result + Integer.hashCode(level);
                return result;
            }

            @Override
            public boolean equals(Object obj) {
                if (this == obj) return true;
                if (obj == null || getClass() != obj.getClass()) return false;
                Question question = (Question) obj;
                return num == question.num && level == question.level;
            }

            public String toString(){
                return "num : "+num+" level : "+level;
            }

        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringBuilder resultBuilder = new StringBuilder();
        TreeSet<Question> questionTree = new TreeSet<>();
        Map<Integer,Integer> questionMap = new HashMap<>();
        StringTokenizer inputToken = null;
        
        int questionCount = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < questionCount; i++) {
            
            inputToken = new StringTokenizer(br.readLine());

            int num = Integer.parseInt(inputToken.nextToken());
            int level = Integer.parseInt(inputToken.nextToken());
            Question question = new Question(num,level);
            questionTree.add(question);
            questionMap.put(num,level);

        }

        int commandCount = Integer.parseInt(br.readLine());
        for (int j = 0; j < commandCount; j++) {

            inputToken = new StringTokenizer(br.readLine());
            String command = inputToken.nextToken();
            int param = Integer.parseInt(inputToken.nextToken());
            
            switch (command) {
                case "recommend":
                    int result = (param==1) ? questionTree.last().num : questionTree.first().num;
                    resultBuilder.append(result+"\n");
                    break;
                case "add":
                    int level = Integer.parseInt(inputToken.nextToken());
                    Question question = new Question(param,level);
                    questionTree.add(question);
                    questionMap.put(param,level);
                    break;
                case "solved":
                    questionTree.remove(new Question(param,questionMap.get(param)));
                    questionMap.remove(param);
                    break;
            
            }
        }

        System.out.println(resultBuilder.toString());

    }
}
