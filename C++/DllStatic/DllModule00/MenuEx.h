#pragma once

#include "DllModule00LibType.h"
#include "Menu.h"

class DLL_MODULE_00_ENTRY MenuEx : public Menu
{
public:
	MenuEx(void);
	~MenuEx(void);

	virtual void File();
};
