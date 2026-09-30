class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == nums[i+1]){
                return true;
            }
        } return false;
    } 
};
