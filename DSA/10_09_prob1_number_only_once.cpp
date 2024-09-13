class Solution {
public:
    int singleNumber(vector<int>& nums) {
        //https://leetcode.com/problems/single-number/


        // //Approach 1 :Brute Force O(N^2)
        // //So haya humlog ne ek loop ke andar loop run kiya 
        // //iterate through the array and agar repeat hua tho add one
        // //aur jaha pe sirf 1 time add hoga who answer hai 
        // int counter = 0;
        // int result = 0;
        // for(int i =0 ; i <nums.size();i++){
        //     for(int j = 0 ; j < nums.size();j++){
                
        //         if(nums[j] == nums[i]){
        //             counter = counter +1 ;
        //         }
                
        //     }
        //     // cout<<counter<<endl;
        //     if(counter == 2 ){
        //         counter = 0;
        //         }
        //     if(counter == 1){
        //             result = nums[i];
        //             break;
        //         }  
        // }
        // return result;



        //Approach 2
        //we can use sorting and phir jaha pe 2 pairs same nhi honge who
        //answer hoga

        //Approach 3
        //Mapping
        //isme humlog basically mapping use karte hai and ++1
        map<int,int> mp;
        for(int i=0 ; i < nums.size() ; i++){
            mp[nums[i]]++;
        }
        for(auto it : mp){
            if(it.second==1){

                return it.first;
            }
        }

        return 0;
    }
};