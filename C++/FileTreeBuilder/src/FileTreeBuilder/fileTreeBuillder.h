#include "stdafx.h"
#include <string>
#include <vector>

using namespace std;

struct Configs
{
    int runMode; // 0 �ݹ���������ID�̶�������ά����  1������
    wstring removeChars;
    wstring ignoreFolders;
    wstring ignoreFiles;
    wstring fileTypes;
    wstring blankFile;
    wstring outputFile;
public:
    void init(wstring file);
};

struct FileNode
{
    int id;
    int pid;
    wstring name;
    wstring file;

    FileNode(int pid, int id, wstring name)
    {
        this->id = id;
        this->pid = pid;
        this->name = name;
    }
};

class FileTreeBuilder
{
private:
    wstring basePath;
    Configs configs;
    vector<FileNode *> fileNodeVector;
    void getAllFiles(wstring path, int pid = 0, int ppid = 0);
    void createZTreeFile();
public:
   FileTreeBuilder();
   ~FileTreeBuilder();
   void build();
};
