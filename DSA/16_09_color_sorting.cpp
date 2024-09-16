class Solution {
public:
    void sortColors(vector<int>& nums) {

        //https://leetcode.com/problems/sort-colors/
        

        //APPROACH 1: beats 100% O(N) O(1)
        //Isme iterate through the loop and count the number of 0s 1s 2s
        //Then erase the original array and insert numbers of 0S then 1s then 2s
        
        //Approach 2: Dutch flag method

        
        int red_counter = 0;
        int white_counter = 0 ;
        int blue_counter = 0 ;

        for(int i = 0 ; i < nums.size() ; i++){
            if(nums[i]==0){
                red_counter++;
            }
            if(nums[i]==1){
                white_counter++;
            }
            if(nums[i]==2){
                blue_counter++;
            }
        }

        nums.clear();
        while(red_counter>0){
            nums.push_back(0);
            red_counter--;
        }
        while(white_counter>0){
            nums.push_back(1);
            white_counter--;
        }
        while(blue_counter>0){
            nums.push_back(2);
            blue_counter--;
        }

        
        
    }
};