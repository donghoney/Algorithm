import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    public static int N;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        String num;

        ArrayList<String> list = new ArrayList<String>();

        for(int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            switch (st.nextToken()) {
                case "add":
                    num = st.nextToken();
                    if (list.contains(num)) continue;
                    else list.add(num);
                    break;
                case "remove":
                    num = st.nextToken();
                    if (list.contains(num)) list.remove(num);
                    break;
                case "check":
                    num = st.nextToken();
                    if (list.contains(num)) sb.append("1\n");
                    else sb.append("0\n");
                    break;
                case "toggle":
                    num = st.nextToken();
                    if (list.contains(num)) list.remove(num);
                    else list.add(num);
                    break;
                case "all":
                    list.clear();
                    for(int j=1; j<=20; j++){
                        list.add(Integer.toString(j));
                    }
                    break;
                case "empty":
                    list.clear();
                    break;
            }
        }

        System.out.println(sb);
    }
}