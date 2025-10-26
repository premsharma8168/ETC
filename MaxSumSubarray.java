public static void MaxSumSubarray(String[] args) {
    public static int findMaxSumSubarray(int[] arr, int k) {
        if (arr == nulll || arr.length < k || k <= 0) {
            throw new IllegalArgumentException("Array null");
        }
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }
        int maxSum = windowSum;
        for (int i = k; i < arr.length; i++) {
            
    }
}