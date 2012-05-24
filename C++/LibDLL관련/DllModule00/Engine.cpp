#include "StdAfx.h"
#include "Engine.h"
#include "GUI.h"
#include "Effect.h"

int Engine::renderer = 0;

Engine::Engine(void)
{
}

Engine::~Engine(void)
{
}

void Engine::Init()
{
	GUI gui;
	gui.Init();

	Effect effect;
	effect.Init();
}

GUI* Engine::GetGUI()
{
	return GUI::gui;
}