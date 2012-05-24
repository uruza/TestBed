#pragma once

#include "DllModule00LibType.h"

class DLL_MODULE_00_ENTRY Base
{
public:
	Base(void);
	~Base(void);

	virtual void Init( int n )
	{
		i = n;
		i++;
	}

	void Core();

	int i;
	char* dumy;
};

#include "Base.inl"