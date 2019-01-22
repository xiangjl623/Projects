#ifndef STRINGCOMMON_H
#define STRINGCOMMON_H
#include <string>

using namespace std;

wstring getSuffix(const wstring& fileName);
wstring trim(const wstring& str);
wstring tolower(const wstring& str);
wstring removeChars(const wstring &sName, const wstring &sRemove);

#endif // STRINGCOMMON_H
