
#include "System.h"

using namespace std;

UINT gData = 0;
UINT gMaxCnt = 100;
UINT gSleep = 3000;

DWORD WINAPI ThreadFunc( LPVOID pArg )
{
	System* pSys = (System*)pArg;
	UINT threadCnt = pSys->mThreadCnt++;

	for ( UINT i = 0; i < gMaxCnt; i++ )
	{
		pSys->mCnt++;
		cout << "Sub" << threadCnt << " Tread : " << pSys->mCnt << endl;
	}

	return 0;
}


System::System(void)
{
	mCnt = 0;
	mThreadCnt = 0;
}

System::~System(void)
{
}

void System::Run()
{
	HANDLE hThreadSub0, hThreadSub1;
	DWORD dwThreadID;

	hThreadSub0 = CreateThread( NULL, 0, ThreadFunc, this, NULL, &dwThreadID );
	hThreadSub1 = CreateThread( NULL, 0, ThreadFunc, this, NULL, &dwThreadID );

	if ( NULL == hThreadSub0 )
	{
	}

	if ( NULL == hThreadSub0 )
	{
	}

	//for ( UINT i = 0; i < gMaxCnt; i++ )
	//{
	//	gData++;
	//	cout << "Main Thread : " << gData << endl;
	//	Sleep( gSleep );
	//}

	Sleep( gSleep );

	CloseHandle( hThreadSub0 );
	CloseHandle( hThreadSub1 );
}
