// MemoryLeakForStatic.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

//#define _CRTDBG_MAP_ALLOC
//
//#include <stdlib.h>
#include <crtdbg.h>

class A
{
public:
	A();
	~A();

	int* pInt;
};

A::A()
{
	pInt = new int;
}

A::~A()
{
//	delete pInt;
}

static A a;

int _tmain(int argc, _TCHAR* argv[])
{
	// 시작시점에 넣어주는 코드
	_CrtSetDbgFlag( _CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF );
//	_CrtSetBreakAlloc( 2666890 );

	// 종료시점에 넣어 주는 코드
	// 아래것을 사용하면 Static에서 릭이 발생된다.
	//_CrtDumpMemoryLeaks();

	return 0;
}