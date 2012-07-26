#pragma once

#include <Windows.h>
#include <iostream>

class System
{
public:
	System(void);
	~System(void);

	void Run();

	UINT mCnt;
	UINT mThreadCnt;
};
