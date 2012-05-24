
#pragma once

#include "DllModule00LibType.h"
#include "GUI.h"

class DLL_MODULE_00_ENTRY Engine
{
public:
	Engine(void);
	~Engine(void);

	void Init();

	static int renderer;
	
	static int GetRenderer()
	{
		return renderer;
	}

	static GUI* GetGUI();
};