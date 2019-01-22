#ifndef INIREADER_H
#define INIREADER_H

#include <xstring>

class CIniReader
{
public:
    CIniReader(const std::wstring & sFileName); 
    int ReadInteger(wchar_t* szSection, wchar_t* szKey, int iDefaultValue);
    float ReadFloat(wchar_t* szSection, wchar_t* szKey, float fltDefaultValue);
    bool ReadBoolean(wchar_t* szSection, wchar_t* szKey, bool bolDefaultValue);
    wchar_t* ReadString(wchar_t* szSection, wchar_t* szKey, const wchar_t* szDefaultValue);
private:
    std::wstring m_sFileName;
};
#endif//INIREADER_H