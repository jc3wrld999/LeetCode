import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Map<String, String> closeToOpen = new HashMap<String, String>();
        closeToOpen.put(")", "(");
        closeToOpen.put("}", "{");
        closeToOpen.put("]", "[");
        
        String[] list = s.split("");    
        Stack<String> stack = new Stack<>();
        for(int i = 0; i < list.length; i++){
            
            if(closeToOpen.containsKey(list[i])){
                if(!stack.empty() && stack.peek().equals(closeToOpen.get(list[i]))){
                    stack.pop();
                }else{
                    return false;
                }
            } else{
                stack.push(list[i]);
            }

        }
        if(stack.empty()){
            return true;
        }
        return false;
    }
}