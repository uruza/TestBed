#include "StdAfx.h"
#include "LibMain00.h"
#include "NiFloat16.h"

LibMain00::LibMain00(void)
{
}

LibMain00::~LibMain00(void)
{
}

//---------------------------------------------------------------------------------------
Object::Object()
{
}

Object::~Object()
{
}

void Object::Init( int n )
{
	aa = n;

	Base::Init( n );

	Base::Core();

	NiFloat16 f16;
}