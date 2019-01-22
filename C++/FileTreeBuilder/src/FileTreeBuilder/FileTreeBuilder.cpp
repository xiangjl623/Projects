// FileTreeBuilder.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include <windows.h>
#include <iostream>
#include <io.h>
#include <fstream>
#include <sstream>
#include <codecvt>
#include "fileTreeBuillder.h" 
#include "IniReader.h"
#include "common.h"
#include "stringCommon.h"

int GID = 0;

void Configs::init(wstring file)
{   
    CIniReader iniReader(file);
    runMode = iniReader.ReadInteger(L"configs", L"runMode", 0);   
    removeChars = iniReader.ReadString(L"configs", L"removeChars", L"0123456789-");  
    ignoreFolders = iniReader.ReadString(L"configs", L"ignoreFolders", L"common");
    ignoreFiles = iniReader.ReadString(L"configs", L"ignoreFiles", L"index.html index.htm");
    fileTypes = iniReader.ReadString(L"configs", L"fileTypes", L" .html, .htm");
    blankFile = iniReader.ReadString(L"configs", L"blankFile", L"");
    outputFile = iniReader.ReadString(L"configs", L"outputFile", L"setting.js");
}

FileTreeBuilder::FileTreeBuilder()
{
   basePath = getExePath();
   configs.init(basePath + L"\\configs.ini");
}

FileTreeBuilder::~FileTreeBuilder()
{
    vector<FileNode *>::iterator it = fileNodeVector.begin();  
    for(it; it != fileNodeVector.end(); it++)  
    {  
        delete (*it);
    }
}

void FileTreeBuilder::createZTreeFile()
{
    wstring sOutputFile = basePath + L"\\" + configs.outputFile;
    wofstream ofn(sOutputFile.c_str());
    const locale utf8_locale = locale(locale(), new codecvt_utf8<wchar_t>()); //存储为UTF-8文件
    ofn.imbue(utf8_locale); 
    int size = fileNodeVector.size();
    if(size > 0)
    {
        ofn << "var zNodes =[ " << endl;
        for (int i = 0; i < size; i++)
        {   
            ofn << "   { id:" << fileNodeVector[i]->id;
            ofn << ",  pId:"  << fileNodeVector[i]->pid;
            ofn << ",  name:\"" << fileNodeVector[i]->name;
            ofn << "\", file:\"" <<  fileNodeVector[i]->file;
            ofn << "\"}"; 
            if (i == size - 1)
            {
                ofn << "]" << endl;
            }
            else 
            {
                ofn << "," << endl;
            }
        }
        wcout << "-----------------------------------------------------------------" << endl;
        wcout << L"共生成文件索引数目为：" << size << endl;
        wcout << "OutputFile:" << sOutputFile << endl;
    }
    ofn.close();
}

void FileTreeBuilder::getAllFiles(wstring path, int pid, int ppid)
{    
    HANDLE hFile = 0; //文件句柄 
    WIN32_FIND_DATAW fileinfo;  //文件信息  //很少用的文件信息读取结构
    int index; 
    index = pid*100 + 1;
    GID++;
    int num = 0;
    wcout << L"---Folder---" << path << endl;
    if ((hFile = FindFirstFileW((path + L"\\*").c_str(), &fileinfo)) != INVALID_HANDLE_VALUE)
    {
        do
        {
            wstring sName = fileinfo.cFileName;
            wstring sTrim = removeChars(sName, configs.removeChars);
            if ((fileinfo.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY))  //比较文件类型是否是文件夹
            {   
                if ((wcscmp(fileinfo.cFileName, L".") != 0) && (wcscmp(fileinfo.cFileName, L"..") != 0) 
                    &&(configs.ignoreFolders.find(tolower(sTrim)) == -1))
                {   
                    FileNode* pNode = new FileNode(pid, configs.runMode == 0 ? index : GID, sTrim);
                    pNode->file = configs.blankFile;
                    fileNodeVector.push_back(pNode);
                    getAllFiles(path + L"/" + sName, pNode->id, pid);    
                    index++;
                }
            }
            else
            {   
                wstring sSuffix = getSuffix(sTrim);
                if ((configs.fileTypes.find(sSuffix) != -1) && (configs.ignoreFiles.find(sTrim) == -1))
                {   
                    sTrim = trim(sTrim.substr(0, sTrim.find(sSuffix)));
                    //if ((num == 0) && (sTrim == fileNodeVector[fileNodeVector.size() - 1]->name))
                    //{
                    //    fileNodeVector[fileNodeVector.size() - 1]->file = (path + L"/" + sName).substr(basePath.length() + 1);
                    //}
                    //else {
                        FileNode* pNode = new FileNode(pid, configs.runMode == 0 ? index : GID, sTrim);
                        pNode->file = (path + L"/" + sName).substr(basePath.length() + 1);
                        wcout << L"******File******" << sName << endl;
                        fileNodeVector.push_back(pNode);
                        index++;
                        GID++;
                    //};    
                    num++;
                }     
            }
        } while (FindNextFileW(hFile, &fileinfo));  //寻找下一个，成功返回0，否则-1
        FindClose(hFile);
    }
}

void FileTreeBuilder::build()
{
    setlocale(LC_ALL, "");
    ios_base::sync_with_stdio(false); // 缺少的话，wcout wchar_t 会漏掉中文
    wcout.imbue(locale(""));
    wcout << "Start......!" << endl;
    Sleep(1000);
    wcout << "-----------------------------------------------------------------" << endl;
    wcout << "Current Path:" << basePath << endl;
    Sleep(1000);
    wcout << "-----------------------------------------------------------------" << endl;
    getAllFiles(basePath);
    createZTreeFile();
    Sleep(2000);
    wcout << "-----------------------------------------------------------------" << endl;
    wcout << "Finish!" << endl;
    system("pause");
}




