class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {

//https://leetcode.com/problems/max-consecutive-ones/
//so i basically, counted the max number of times 1 comes consecutively
//if the streak is broken who wapas 0 ko set karta hai 
//iske 2 approaches hai
//1. ek ki jo max_streak ke values aa rahe hai usko ek vector mai store kardo
//2. or else who value ko ek ans var mai bhardo and then next time compaer the newer one to old wala

//par dono ka runtime bohot zyada aa raha hai :( , next time wapas karta hu
        // int max_streak = 0;
        // vector<int> max;
        // for(int i =0 ; i < nums.size(); i++){
        //     if(nums[i]==1){
        //         max_streak++;
        //     }
        //     else{
        //         max.push_back(max_streak);
        //         max_streak = 0;
        //     }
        //     if(i==nums.size()-1){
        //         max.push_back(max_streak);
        //     }
        // }

        

        // int max_for_return = max[0];
        // for (int i = 0 ; i < max.size(); i++){
        //     // cout<<max[i]<<endl;
        //     if(max[i]>max_for_return){
        //         max_for_return = max[i];
        //     }

        // }

        int max_streak = 0;
        int ans = 0;
        for(int i = 0 ; i < nums.size();i++){
            if(nums[i]==1){
                max_streak++ ;
            }
            else{
                max_streak = 0;
            }

            ans = max(ans,max_streak);
        } 
        return ans;

        

    }
};