#include "stdafx.h"
#include "IniReader.h"
#include <iostream>
#include <Windows.h>

CIniReader::CIniReader(const std::wstring & sFileName)
{
    m_sFileName = sFileName;
}

int CIniReader::ReadInteger(wchar_t* szSection, wchar_t* szKey, int iDefaultValue)
{
    int iResult = GetPrivateProfileIntW(szSection,  szKey, iDefaultValue, m_sFileName.c_str()); 
    return iResult;
}

float CIniReader::ReadFloat(wchar_t* szSection, wchar_t* szKey, float fltDefaultValue)
{
    wchar_t szResult[255];
    wchar_t szDefault[255];
    float fltResult;
    wprintf(szDefault, "%f", fltDefaultValue);
    GetPrivateProfileStringW(szSection,  szKey, szDefault, szResult, 255, m_sFileName.c_str()); 
    fltResult =  _wtof(szResult);
    return fltResult;
}

bool CIniReader::ReadBoolean(wchar_t* szSection, wchar_t* szKey, bool bolDefaultValue)
{
    wchar_t szResult[255];
    wchar_t szDefault[255];
    bool bolResult;
    wprintf(szDefault, "%s", bolDefaultValue? "True" : "False");
    GetPrivateProfileStringW(szSection, szKey, szDefault, szResult, 255, m_sFileName.c_str()); 
    bolResult =  (wcscmp(szResult, L"True") == 0 || 
        wcscmp(szResult, L"true") == 0) ? true : false;
    return bolResult;
}

wchar_t* CIniReader::ReadString(wchar_t* szSection, wchar_t* szKey, const wchar_t* szDefaultValue)
{
    wchar_t* szResult = new wchar_t[255];
    memset(szResult, 0x00, 255);
    GetPrivateProfileStringW(szSection,  szKey, 
        szDefaultValue, szResult, 255, m_sFileName.c_str()); 
    return szResult;
}