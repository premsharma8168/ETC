public class MaxSumSubarray {
    
    public static Integer maxSumSubarray(int[] arr, int k) {
        if (arr == null || k <= 0 || k > arr.length) {
            return null;
        }

        int currentSum = 0;
        for (int i = 0; i < k; i++) {
            currentSum += arr[i];
        }

        int maxSum = currentSum;

        for (int i = k; i < arr.length; i++) {
            currentSum += arr[i] - arr[i - k];
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }

        public static void main(String[] args) {
            int[] arr = {1, 4, 2, 10, 23, 3, 1, 0, 20};
            int k = 4;
            Integer result = maxSumSubarray(arr, k);
            System.out.println("Maximum sum of subarray of size " + k + " is: " + result);
        }
        }
