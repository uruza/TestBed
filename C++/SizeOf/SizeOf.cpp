// SizeOf.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int var[2];

	printf( "SizeOf int : %d\n", sizeof ( int[2] ) );
	printf( "SizeOf var : %d\n", sizeof ( var ) );

	int* pVar = new int[2];

	printf( "SizeOf int : %d\n", sizeof ( int[2] ) );
	printf( "SizeOf pVar : %d\n", sizeof ( pVar ) );

	delete [] pVar;
	pVar = NULL;

	char szDesc[128];
	printf( "SizeOf char[128] : %d\n", sizeof ( char ) * 128  );
	printf( "SizeOf szDesc : %d\n", sizeof ( szDesc ) );

	return 0;
}

