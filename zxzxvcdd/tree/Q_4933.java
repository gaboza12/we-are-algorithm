package zxzxvcdd.tree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;
import java.util.StringTokenizer;

public class Q_4933 {

    public static void main(String[] args) throws NumberFormatException, IOException {
        

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder result = new StringBuilder();
        int testcase = Integer.parseInt(br.readLine());
        
        for(int i = 0; i < testcase; i++){

            Map<String,List<String>> treeMap1 = getTreeMap(br.readLine());
            Map<String,List<String>> treeMap2 = getTreeMap(br.readLine());
            result.append(isEqualsMap(treeMap1,treeMap2)+"\n");
            
        }
    
        System.out.println(result.toString());

    }

    private static boolean isEqualsMap(Map<String, List<String>> treeMap1, Map<String, List<String>> treeMap2) {

        if (treeMap1.size() != treeMap2.size()) {
            return false;
        }
        
        for (String key : treeMap1.keySet()) {
            
            List<String> list1 = treeMap1.get(key);
            List<String> list2 = treeMap2.get(key);
            try{
                if (list1.size() != list2.size()) {
                    return false;
                }
            }catch(NullPointerException e){
                return false;
            }

            Collections.sort(list1);
            Collections.sort(list2);
            
            if (!list1.equals(list2)) {
                return false;
            }
        }

        return true;
    }

    private static Map<String, List<String>> getTreeMap(String line) {

        Map<String,List<String>> treeMap = new HashMap<>();
        
        Stack<String> appleTree = new Stack<>();
            
        StringTokenizer inputToken = new StringTokenizer(line);

        while(true){

            String input = inputToken.nextToken();
            if(input.equals("end")) break;

            if(appleTree.size() > 1 && !input.equals("nil")){                    
                String right = appleTree.pop();
                String left = appleTree.pop();

                List<String> childList;
                if(treeMap.containsKey(input)){
                    childList = treeMap.get(input);
                }else{
                    childList =  new ArrayList<>();
                    treeMap.put(input, childList);
                }
                addChild(childList, left);                        
                addChild(childList, right);                        
                
            }
            appleTree.push(input);
        }
        return treeMap;

    }

    static void addChild(List<String> childList, String child){
        if(!child.equals("nil")) childList.add(child);
    }
    
}
