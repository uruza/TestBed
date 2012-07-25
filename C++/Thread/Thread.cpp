// Thread.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

using namespace std;

UINT gData = 0;
UINT gMaxCnt = 100;
UINT gSleep = 1;

DWORD WINAPI ThreadFunc( LPVOID pArg )
{
	for ( UINT i = 0; i < gMaxCnt; i++ )
	{
		gData++;
		cout << "Sub0 Tread : " << gData << endl;
	}

	return 0;
}


int _tmain(int argc, _TCHAR* argv[])
{
	HANDLE hThread;
	DWORD dwThreadID;

	hThread = CreateThread( NULL, 0, ThreadFunc, NULL, NULL, &dwThreadID );

	if ( NULL == hThread )
	{
		return -1;
	}

	for ( UINT i = 0; i < gMaxCnt; i++ )
	{
		gData++;
		cout << "Main Thread : " << gData << endl;
		Sleep( gSleep );
	}

	CloseHandle( hThread );

	return 0;
}

