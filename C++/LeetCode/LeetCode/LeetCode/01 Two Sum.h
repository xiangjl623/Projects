#include "stdafx.h"
#include <vector>
#include <map>
#include <iostream>
#include <string>

/*
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, w
here index1 must be less than index2. Please note that your returned answers (both index1 and index
2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

给定一个整型数组，找出能相加起来等于一个特定目标数字的两个数。
函数 twoSum 返回这两个相加起来等于目标值的数字的索引，且 index1 必须小于 index2。 请记住你返回的答
案（包括 index1 和 index2）都不是从 0 开始的。
你可以假定每个输入都有且仅有一个解决方案。
输入: numbers={2, 7, 11, 15}, target=9
输出: index1=1, index2=2

*/

using namespace std;
class Solution01{
public:
    static vector<int> twoSum(vector<int>& numbers, int target)
    {
        vector<int> output;
        map<int, int> mapping;

        for (int i = 0; i < numbers.size(); i++)
        {
            mapping[numbers[i]] = i;
        }

        for (int i = 0; i < numbers.size(); i++)
        {
            int searched = target - numbers[i];
            if (mapping.find(searched) != mapping.end() && mapping.at(searched) != i)
            {
                output.push_back(i + 1);
                output.push_back(mapping.at(searched) + 1);
                break;
            }
        }

        return output;
    }

    static void test(){
        vector<int> numbers = { 2, 7, 11, 15 };
        vector<int> output = twoSum(numbers, 18);
        for (int i = 0; i < output.size(); i++)
        {
            cout << "Index" + to_string(i+1) + ":" + to_string(output[i]) << endl;
        }
    }
};
