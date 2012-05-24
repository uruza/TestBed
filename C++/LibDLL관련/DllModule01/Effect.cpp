#include "StdAfx.h"
#include "Effect.h"
//#include "Engine.h"

void* Effect::effect = 0;

Effect::Effect(void)
{
}

Effect::~Effect(void)
{
}

void Effect::Init()
{
	//Engine::renderer;

	//Engine::GetRenderer();

	effect = this;
}
