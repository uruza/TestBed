// StringReturn.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

char* GetString_1()
{
	return "1";
}

char* GetString_2()
{
	return "2";
}


int _tmain(int argc, _TCHAR* argv[])
{
	char* szString = NULL;

	szString = "0";

	szString = GetString_1();

	szString = GetString_2();

	return 0;
}



