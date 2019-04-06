import java.util.*;

public class topological{
    public static LinkedList<Integer> order = new LinkedList<>();

    public static void buildGraph(int[][] graph, HashMap<Integer, LinkedList<Integer>> hmap){
        for(int i=0; i<graph.length; i++){
            int parent = graph[i][0];
            int child = graph[i][1];
            if(!hmap.containsKey(parent)) hmap.put(parent, new LinkedList<>());
            hmap.get(parent).add(child);
        }
    }

    public static void dfs(int ele, int[][] graph, HashMap<Integer, LinkedList<Integer>> hmap){
        if(order.contains(ele)) return;
        if(hmap.containsKey(ele)){
        for(int child : hmap.get(ele))
            dfs(child, graph, hmap);}
        order.add(ele);
    }

    public static void topologicalSort(int[][] graph, HashMap<Integer, LinkedList<Integer>> hmap){
        for(int key : hmap.keySet()){
            if(!order.contains(key))
                dfs(key, graph, hmap);
        }
    }

    

    public static void main(String[] args){
        //int[][] graph = {{1,0},{0,2},{2,3},{3,4},{2,4}};
        int[][] graph = {{4,2},{0,3},{2,0},{6,2},{0,1}};
        HashMap<Integer, LinkedList<Integer>> hmap = new HashMap<>();
        buildGraph(graph, hmap);
        topologicalSort(graph, hmap);
        System.out.println(order);
    }
}