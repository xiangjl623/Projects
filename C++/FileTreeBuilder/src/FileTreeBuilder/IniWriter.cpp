#include "stdafx.h"
#include "IniWriter.h"
#include <iostream>
#include <Windows.h> 

CIniWriter::CIniWriter(const std::wstring & sFileName)
{
    m_sFileName = sFileName;
}

void CIniWriter::WriteInteger(wchar_t* szSection, wchar_t* szKey, int iValue)
{
    wchar_t szValue[255];
    wprintf(szValue, "%d", iValue);
    WritePrivateProfileStringW(szSection,  szKey, szValue, m_sFileName.c_str()); 
}

void CIniWriter::WriteFloat(wchar_t* szSection, wchar_t* szKey, float fltValue)
{
    wchar_t szValue[255];
    wprintf(szValue, "%f", fltValue);
    WritePrivateProfileStringW(szSection,  szKey, szValue, m_sFileName.c_str()); 
}

void CIniWriter::WriteBoolean(wchar_t* szSection, wchar_t* szKey, bool bolValue)
{
    wchar_t szValue[255];
    wprintf(szValue, "%s", bolValue ? "True" : "False");
    WritePrivateProfileStringW(szSection,  szKey, szValue, m_sFileName.c_str()); 
}

void CIniWriter::WriteString(wchar_t* szSection, wchar_t* szKey, wchar_t* szValue)
{
    WritePrivateProfileStringW(szSection,  szKey, szValue, m_sFileName.c_str());
}