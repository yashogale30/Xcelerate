class Solution {
public:

//https://leetcode.com/problems/remove-duplicates-from-sorted-array/
//O(n^2)
// First ek varible declare karo zisko hum as a container ya reference use karenge
// then who var ko first value assign kardenge aur phir compare it with next elements
// agar same nikla tho erase se hata denge par yaha i ko wapas i-1 rakhegne coz who ek place left shift hote hai
// aur agar same nhi hua tho zo next different var hai uska value de denge 

    int removeDuplicates(vector<int>& nums) {
        int compare = nums[0];
        for(int i = 1 ; i < nums.size(); i++){

            if(nums[i] == compare ){
                nums.erase(nums.begin() + i);
                i=i-1 ; 
            }
            else{
                compare = nums[i];
            }
        }

        int count  = nums.size();
        return count;  
    }
};