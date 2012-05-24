#include "StdAfx.h"
#include "GUI.h"

GUI* GUI::gui = 0;

GUI::GUI(void) :
	cnt(0)
{
}

GUI::~GUI(void)
{
}

void GUI::Init()
{
	gui = this;
}

GUI* GUI::GetGUI()
{
	return gui;
}

void GUI::SetCnt( int i )
{
	cnt = i;
}
