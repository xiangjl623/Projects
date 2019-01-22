#include "stdafx.h"
#include "common.h"
#include <windows.h>

wstring getExePath()
{
    wchar_t sFullPath[MAX_PATH];
    memset(sFullPath,0,MAX_PATH);
    GetModuleFileNameW(NULL, sFullPath, MAX_PATH);
    wstring sPath = sFullPath;    // Get full path of the file
    int pos = sPath.find_last_of('\\', sPath.length());
    return sPath.substr(0, pos);
}