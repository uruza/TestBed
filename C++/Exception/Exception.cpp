// Exception.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

//#include <excpt.h>
#include <Windows.h>
#include <new.h>
#include <crtdbg.h>  // For _CrtSetReportMode

//---------------------------------------------------------------------------------------
class A
{
public:
	virtual void MemFunc() = 0;
};

//---------------------------------------------------------------------------------------
class B : public A
{
public:
	virtual void MemFunc()
	{
		printf( "B::MemFunc \n" );
		return;
	}
};


//---------------------------------------------------------------------------------------
// CreateMiniDump( pEP );

//---------------------------------------------------------------------------------------
LONG __stdcall MyCustomFilter( EXCEPTION_POINTERS* pEP )
{
	printf( "MyCustomFilter\n" );

//	CreateMiniDump( pEP );

	return EXCEPTION_EXECUTE_HANDLER;
}

//---------------------------------------------------------------------------------------
void Func()
{
	printf ( "Func.. Crash.. \n" );

	int* pA = NULL;
	*pA = 1;
}

//---------------------------------------------------------------------------------------
void FuncVirtual()
{
	printf ( "FuncVirtual.. \n" );

	A* a = new B;
}

//---------------------------------------------------------------------------------------
void FuncThrow()
{
	printf ( "FuncThrow \n" );

	throw "ddd";
}

//---------------------------------------------------------------------------------------
void FuncDynamicNew()
{
	printf ( "FuncDynamicNew \n" );

	int* pI;

	for ( UINT i = 0; i < UINT_MAX; i++ )
	{
		for ( UINT j = 0; j < UINT_MAX; j++ )
		{
			pI = new int;
		}
	}
}

//---------------------------------------------------------------------------------------
void FuncInvalid()
{
	printf ( "FuncInvalid \n" );

	_CrtSetReportMode(_CRT_ASSERT, 0);

	char* formatString;
	formatString = NULL;
	printf(formatString);
}

//---------------------------------------------------------------------------------------
int _set_new_handler_callback( size_t size )
{
	printf ( "set_new_handler \n" );

	RaiseException(EXCEPTION_ACCESS_VIOLATION, 0, 0, NULL);
	exit(0);
}

//---------------------------------------------------------------------------------------
void _set_invalid_parameter_handler_callback(	PCTSTR expression, PCTSTR function, 
												PCTSTR file, unsigned int line, 
												uintptr_t pReserved	)
{
	printf ( "_set_invalid_parameter_handler_callback \n" );

	RaiseException(EXCEPTION_ACCESS_VIOLATION, 0, 0, NULL); 
	exit(0);
}

//---------------------------------------------------------------------------------------
int _tmain(int argc, _TCHAR* argv[])
{
	printf ( "Start \n" );

//	_set_new_handler ( _set_new_handler_callback );
	_set_invalid_parameter_handler ( _set_invalid_parameter_handler_callback );

	SetUnhandledExceptionFilter( MyCustomFilter );

//	FuncDynamicNew();

	FuncInvalid();

//	FuncThrow();

//	FuncVirtual();

//	Func();

	printf ( "End \n" );

	return 0;
}

