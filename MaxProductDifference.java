import java.util.*;
class MaxProductDifference {
    public static void main(String[] args) {
        int[] nums = {5,6,2,7,4};
        Arrays.sort(nums);
        int ans = (nums[nums.length-1]*nums[nums.length-2]) - (nums[0]*nums[1]);
        System.out.println(ans);
    }
}
