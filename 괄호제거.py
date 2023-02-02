from itertools import combinations

expression = input()
arr = []
index = []
result=[]
#괄호를 배열에 담기
for i in range(len(expression)):
    if expression[i] == '(':
        arr.append(i)
    elif expression[i] == ')':
        index.append([arr.pop(), i])

#괄호 제거와 result에 append
for i in range(1, len(index)+1):
    combs = list(combinations(index, i))
    for comb in combs:
        check = []
        answer = []
        for com in comb:
            check.append(com[0]); check.append(com[1])

        for j in range(len(expression)):
            if j in check:
                continue
            else:
                answer.append(expression[j])
        result.append(''.join(answer))
# 중복제거
result = set(result)
# 사전순 sort
result = sorted(list(result))
# 출력
for res in result:
    print(res)

    
    
    
    
    
    ######################################################
    for java (dfs version)
    import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.TreeSet;

public class Main {
    static ArrayList<Pair> list;    //괄호쌍 저장 리스트
    static StringBuilder sb;    
    static TreeSet<String> res;     //괄호 삭제된 각 문자열 정렬 및 저장

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        list = new ArrayList<>();
        res = new TreeSet<>();
        Stack<Integer> stack = new Stack<>();     //괄호 쌍 구하기 위한 스택

        for(int i=0; i<str.length(); i++) {
            char c = str.charAt(i);

            if(c=='(')
                stack.push(i);          //여는 괄호면 스택에 인덱스 넣음

            else if(c==')') {         //닫는 괄호 나오면 가까운 여는 괄호 인덱스와 함께 Pair쌍 생성
                list.add(new Pair(stack.pop(), i));
            }
        }

        dfs(str, 0);

        for(String ans : res)
            System.out.println(ans);
    }

    public static void dfs(String str, int idx) {
        if(idx>=list.size()) return;

        for(int i=idx; i<list.size(); i++) {
           Pair temp = list.get(i);

           sb = new StringBuilder(str);
           sb.replace(temp.open, temp.open+1, " ");       //괄호 삭제 쉽게 괄호를 공백으로 치환해서 문자열 길이 유지
           sb.replace(temp.close, temp.close+1, " ");
           res.add(sb.toString().replaceAll(" ", ""));    //셋에 넣을 때는 공백삭제 후 추가
           dfs(sb.toString(), i+1);
           sb.replace(temp.open, temp.open+1, "(");
           sb.replace(temp.close, temp.close+1, ")");
        }
    }

    public static class Pair {        //괄호쌍 저장 위한 클래스 구현
        int open;
        int close;

        public Pair(int open, int close) {
            this.open = open;
            this.close = close;
        }
    }
}
