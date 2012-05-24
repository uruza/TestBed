
#pragma once

#include "Base.h"

class LibMain00
{
public:
	LibMain00(void);
	~LibMain00(void);
};

//---------------------------------------------------------------------------------------
class Object : public Base
{
public:
	Object();
	~Object();

	virtual void Init( int n );

	int aa;
};
