#ifndef INIWRITER_H
#define INIWRITER_H

#include <xstring>

class CIniWriter
{
public:
    CIniWriter(const std::wstring & sFileName); 
    void WriteInteger(wchar_t* szSection, wchar_t* szKey, int iValue);
    void WriteFloat(wchar_t* szSection, wchar_t* szKey, float fltValue);
    void WriteBoolean(wchar_t* szSection, wchar_t* szKey, bool bolValue);
    void WriteString(wchar_t* szSection, wchar_t* szKey, wchar_t* szValue);
private:
    std::wstring m_sFileName;
};
#endif //INIWRITER_H