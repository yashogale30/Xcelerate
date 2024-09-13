class Solution {
  public:
    // Function to find element in sorted array
    // arr: input array
    // N: size of array
    // K: element to be searched
    int searchInSorted(int arr[], int N, int K) {
        
        
        //https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=who-will-win
        
        // basics sirf iterate karna hai
        for(int i = 0 ; i < N ; i++){
            if(arr[i] == K){
                return 1;
            }
        }
        
        return -1;
    }