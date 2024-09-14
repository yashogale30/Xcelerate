// } Driver Code Ends
class Solution{
    public:
    //arr1,arr2 : the arrays
    // n, m: size of arrays
    //Function to return a list containing the union of the two arrays. 
    vector<int> findUnion(int arr1[], int arr2[], int n, int m)
    {
        //https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays
        
        //APPROACH 1:
        //First humlog dono arrays ke element ko ek arrat mai store kar
        //denge then sorting and then remove duplicates 
        //par ise bohot lamba zyata hai :(
        
        
        
        
        //Approach 2:0.7
        //Use set , ek ordered set mai elements repeat nhi hote aur store 
        //hote hai
        // set <int> st;
        
        // for(int i = 0 ; i < n ; i++){
        //     st.insert(arr1[i]);
        // }
        // for(int i = 0 ; i < m ; i++){
        //     st.insert(arr2[i]);
        // }
        
        // vector<int> vec;
        // for(auto it: st){
        //     vec.push_back(it);
        // }
        
        // return vec;
        
        
        
        //approach2:0.34
        //This was the optimal solution given by striver
        //so isme humne kya kiya basically do bar iterate kia 
        //along arr1 and arr2 and jo chota number hai usko vec 
        //me push kiya , phir next time compare kiya ki jo next
        //numebr hai who na tho repeat ho , aur agar end mai kuh 
        //bajta hai tho usko directly pushback kardo , 
        //since arr sorted hai
        
        
        vector <int> vec;
        int i = 0;
        int j= 0;
        
        while(i<n && j <m){
            if(arr1[i]<arr2[j]){
                if(vec.size() == 0 || vec.back() != arr1[i]){
                    vec.push_back(arr1[i]);
                }
                i++;
            }
            else{
                if(vec.size() == 0 || vec.back() != arr2[j]){
                    vec.push_back(arr2[j]);
                }
                j++;
                
            }
            
        }
        
        while(i<n){
            if(vec.size() == 0 || vec.back() != arr1[i]){
                    vec.push_back(arr1[i]);
                }
                i++;
        }
        
        while(j<m){
            if(vec.size() == 0 || vec.back() != arr2[j]){
                    vec.push_back(arr2[j]);
                }
                j++;
        }
        
        return vec;
    }
};

//{ Driver Code Starts.

