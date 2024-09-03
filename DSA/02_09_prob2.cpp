class Solution {
  public:
    // Function returns the second
    // largest elements
    int print2largest(vector<int> &arr) {
        // O(N)
        //ek for loop banake iterate accross the arr to get the max number
        //phir aur ek loop lagake same approach kiya par ek and condition 
        //dala ki jab who jo second_max var hai who jab max ke equal hoga 
        //tab who max ka value nhi lene , ise humlog ko second max mila
         
        int max = 0 ; 
        
        int second_max = 0;
        
        for (int i = 0 ; i < arr.size() ; i++){
            if ( arr [i] > max ){
                max = arr[i];
            }
        }
        
        for (int j = 0 ; j < arr.size() ; j ++ ){
            if (arr[j]>second_max && arr[j] != max){
                second_max = arr[j] ; 
            }
        }
        
        if(second_max == 0 ){
            return -1;
        }
        else{
            return second_max;
        }
    }
};