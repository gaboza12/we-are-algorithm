package zxzxvcdd.datastructure;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;
import java.util.TreeSet;
import java.util.stream.IntStream;

public class Q_2800 {


    static class BracketInfo{
        int index;
        char bracket;
        public BracketInfo(int index, char bracket) {
            this.index = index;
            this.bracket = bracket;
        }
    }
    static class IndexMap{
        int start;
        int end;
        public IndexMap(int start, int end) {
            this.start = start;
            this.end = end;
        }
        
    }

    static String input="";
    static List<IndexMap> indexMapList= null;
    static Set<String> resultSet = new TreeSet<>();

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input = br.readLine();
        Stack<BracketInfo> bracketStack = new Stack<>();
        indexMapList = new ArrayList<>();

        for(int i= 0; i < input.length(); i++){
            
            char currentChar = input.charAt(i);
            if(currentChar == '('){
                bracketStack.push(new BracketInfo(i,currentChar));
            }else if(currentChar == ')'){
                BracketInfo bracketInfo = bracketStack.pop();
                indexMapList.add(new IndexMap(bracketInfo.index,i));
            }
        }
        generateResults(0,new ArrayList<IndexMap>());

        resultSet.forEach(System.out::println);
        
    }

    static void generateResults(int index,List<IndexMap> resultList) {

        if (index == indexMapList.size()) {
            if(resultList.size()>0){
                resultSet.add(modifyInput(input, resultList));
            }
            return;
        }
        
        generateResults(index + 1,new ArrayList<>(resultList));
        
        IndexMap indexMap = indexMapList.get(index);
        resultList.add(indexMap);
        generateResults(index + 1,new ArrayList<>(resultList));
    
    }

    static String modifyInput(String input,List<IndexMap> indexMapList){
        StringBuilder modifiedInput = new StringBuilder(input);

        indexMapList.forEach(indexMap ->{
            modifiedInput.setCharAt(indexMap.start, '$');
            modifiedInput.setCharAt(indexMap.end, '$');
        });

        return modifiedInput.toString().replace("$", "");
    }

}
