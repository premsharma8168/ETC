class CountingSort {
    static void sort(int[] arr) {
        int max=arr[0];
        for(int x:arr) if(x>max) max=x;
        int[] count=new int[max+1];
        for(int x:arr) count[x]++;
        int idx=0;
        for(int i=0;i<count.length;i++) while(count[i]-- >0) arr[idx++]=i;
    }
    public static void main(String[] args) {
        int[] arr={4,2,2,8,3,3,1};
        sort(arr);
        for(int x:arr) System.out.print(x+" ");
    }
}
