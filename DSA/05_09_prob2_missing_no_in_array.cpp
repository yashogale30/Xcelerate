class Solution {
public:
//https://leetcode.com/problems/missing-number/

    int missingNumber(vector<int>& nums) {

      // APPROACH 1 : BRUTE FORCE 
      //time complexity = O(nlogn)
        //brute force first sort then check the numbers

        // int n = nums.size();
        // for(int i = 0 ; i < n-1 ; i++){
        //     for(int j=i+1 ; j < n ; j++){
        //         if(nums[j]<nums[i]){
        //             int c = nums[i];
        //             nums[i]=nums[j];
        //             nums[j] = c;

        //         }
        //     }
        // }

        // int i = 0;

        // for(; i < nums.size(); i++){
        //     if(nums[i] != i){
        //         break;
        //     }
        // }
        // return i;

// Approach 2 : addition 
//time complexity = O(N)

// here humlog first who range ke numbers ka addition lenge , aur array 
// ke under ke numbers ka bhi , sirf 1 number missing hai tho jo difference
//hoga who number who hoga
        int n = nums.size();
        int sum = (n * (n+1))/2 ;
        int arr_sum = 0;
        for(int i = 0 ; i<n ; i++){
            arr_sum = arr_sum + nums[i];
        }

        return sum - arr_sum ;

    }
};