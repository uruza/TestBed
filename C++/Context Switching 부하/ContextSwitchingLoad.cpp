// ContextSwitchingLoad.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <Windows.h>

DWORD WINAPI ThreadFunc (PVOID pvParam)
{
	DWORD dwResult = 0;

	return (dwResult);
}



int _tmain(int argc, _TCHAR* argv[])
{
	DWORD dwThreadID;

	HANDLE hThread;

	for ( int i = 0 ; i < 10; i++ )
	{

		hThread = CreateThread( NULL, 0, ThreadFunc, 0, 0, &dwThreadID);

	}

//	GetExitCodeThread(hThread, &dwThreadID);

//	CloseHandle(hThread);

	while( true )
	{
		int a = 100;
	}

	return 0;
}

