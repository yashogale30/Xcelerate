class Solution {

    //https://leetcode.com/problems/move-zeroes/
    //O(N)
    //I was stuck on this question , so i took a hint :(
    //Isme basically we take all the zeros jo way mai ate hai and then
    //phir pure grp ko swap with the nonzero number
public:
    void moveZeroes(vector<int>& nums) {
        int collector = 0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                collector += 1;
            }
            else if( collector >0 ){
                int c = nums[i];
                nums[i] = 0;
                nums[i-collector] = c;
            }
        }       
    }
};