class Solution {
  public:
    int largest(vector<int> &arr) {
        
        //https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array
        //Complexity O(N)
        // approach 1 loop
        //ek loop banano , phir who arr ke across iterate karo and change the value
        //of max number


        int max = 0 ;
        
        for (int i = 0 ; i <arr.size();i++){
            if (arr[i]>max){
                max = arr[i];
            }
        }
        
        return max;
        
        
    }
};