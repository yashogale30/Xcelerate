class Solution {
public:
//https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
//So yahe pe humlog ko dekhna hai ki who increasing order kitne 
//bar break hota hai , agar 1 or 0 hua tho chalega , par use zyada 
//hua tho array sorted nhi hogaya , also ek border condition dekhna 
//hai ki first or last element may relation kya hai , 
//coz if we rotate who do beechmai ayenge
    bool check(vector<int>& nums) {
        int counter = 0;
        int n = nums.size();
        bool helper = false;
        for(int i = 1 ; i <n;i++){
            if(nums[i-1]>nums[i]){
                counter++;
            }
        }
        
        if(nums[n-1]>nums[0]){
            counter++;
        }

        if(counter > 1){
            helper = true;
        }

        if(helper){
            return false;
        }
        return true;
        
    }
};