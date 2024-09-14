class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        //https://leetcode.com/problems/two-sum/
        
        //Approach1 : simple O(N^2) , DO BAR ITERATE KARDENA
        int n = nums.size();
        // int i = 0 ;
        // int j =n-1;
        // pair<int,int> match;

        // for(int i = 0 ; i < n ; i++){
        //     for(int j = i+1 ; j <n ; j++){
        //         if(nums[i]+nums[j] == target && i != j){
        //             return {i,j};
        //         }
        //     }
        // }

        // return {};



        //APPROACH2:
        // isme we use hashmap, we take a numebr and see whether
        //  the remaing part is presetn or not , if not just map 
        // with index and move on
        map <int,int> mp;
        for(int i = 0 ; i < n ; i++ ){
            int a = nums[i];
            int more = target - a;
            if(mp.find(more) != mp.end()){
                return {mp[more] , i};
            }
            mp[a] = i;
        }
        return {};
    }
};