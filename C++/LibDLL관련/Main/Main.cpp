// Main.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include "LibMain00.h"
#include "Node.h"
//#include "NiFilename.h"
#include "NiFloat16.h"

int _tmain(int argc, _TCHAR* argv[])
{
	Object obj;
	obj.Init( 1 );

	Node node;
	node.Init( 2 );

	NiFloat16 f16;

	return 0;
}

