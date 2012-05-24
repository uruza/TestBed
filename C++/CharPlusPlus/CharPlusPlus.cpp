// CharPlusPlus.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

namespace TRANSFORM
{
	typedef unsigned char TYPE;

	const TYPE NONE			= 0;
	const TYPE LAYPERSON		= 1;// 일반인 상태
	const TYPE RANGER		= 3;// 1차 변신 상태
	const TYPE MAX			= 4;
}

int _tmain(int argc, _TCHAR* argv[])
{
	TRANSFORM::TYPE type = TRANSFORM::LAYPERSON;

	type++;

	return 0;
}

