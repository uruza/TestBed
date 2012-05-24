// Hash_Map_Test.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

class Node : public stdext::hash_map< size_t, Node* >
{
	Node()
};


int _tmain(int argc, _TCHAR* argv[])
{


	return 0;
}

