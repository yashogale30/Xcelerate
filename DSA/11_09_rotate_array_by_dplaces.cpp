class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        //https://leetcode.com/problems/rotate-array/


        //APPROACH1: Brute like , isme humlog jo numbers right se rotate
        //karne pe bahar ja rahe the unko separate isme stoe kiya and then 
        //move aur phir who stored wale ko vapas insert kiya


        // int n = nums.size();
        // k = k % n;

        // vector<int> helper;
        // auto first = nums.end() - k;
        // auto last = nums.end();
        // helper.insert(helper.end(), first, last);
        


        // for(int i = n-k-1 ; i >=0 ; i-- ){
        //     nums[k+i]=nums[i];
        // }

        // for (int i = 0; i < k; ++i) {
        //     nums[i] = helper[i];
        // }



        //Approach2:stivers optiomal solution (by pure observation)
        //isme jo k diya hai utna , matlab end ke jo numbers hai jinko age lana hai 
        //unko first reverse , aur waise hi remaining ko ulta and finally whole thing ko reverse

        int n=nums.size();
        k = k % n;

        reverse(nums.begin(),nums.begin()+n-k);
        reverse(nums.begin()+n-k,nums.end());
        reverse(nums.begin(),nums.end());
    }
};