#include "stdafx.h"
#include "stringCommon.h"

wstring trim(const wstring& str)
{
    size_t first = str.find_first_not_of(' ');
    if (string::npos == first)
    {
        return str;
    }
    size_t last = str.find_last_not_of(' ');
    return str.substr(first, (last - first + 1));
}

wstring tolower(const wstring& str)
{
    wstring s = str;
    for (size_t i = 0; i < s.length(); i++)  
    {  
        s[i] = tolower(s[i]);  
    }; 
    return s;
}

wstring getSuffix(const wstring& fileName)
{
    int pos = fileName.find_last_of(L"."); //获取. 的位置 
    if(pos == -1)
    {  
        return L"";  
    }
    else
    {   
        return fileName.substr(pos, fileName.length());
    } 
} 

wstring removeChars(const wstring &sName, const wstring &sRemove)
{
    wstring sTrim = sName;
    if (sRemove != L"") 
    {
        int pos = sName.find_first_not_of(sRemove);
        if (pos > 0) 
        {
            sTrim = trim(sName.substr(pos, sName.length() - pos));
            if(sTrim.length() == 0) 
                sTrim = sName;
        }
    }
    return sTrim;
}