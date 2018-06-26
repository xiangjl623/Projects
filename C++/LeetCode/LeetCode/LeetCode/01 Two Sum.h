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

����һ���������飬�ҳ��������������һ���ض�Ŀ�����ֵ���������
���� twoSum ���������������������Ŀ��ֵ�����ֵ��������� index1 ����С�� index2�� ���ס�㷵�صĴ�
�������� index1 �� index2�������Ǵ� 0 ��ʼ�ġ�
����Լٶ�ÿ�����붼���ҽ���һ�����������
����: numbers={2, 7, 11, 15}, target=9
���: index1=1, index2=2

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
