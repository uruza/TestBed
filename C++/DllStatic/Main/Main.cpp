// Main.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

//#include "Engine.h"
//#include "Effect.h"

#include "MyMenu.h"


int _tmain(int argc, _TCHAR* argv[])
{
	//Engine engine;
	//engine.Init();
	//GUI::gui = engine.GetGUI();
	//GUI::gui->SetCnt( 1 );
	//void* pGui = GUI::gui;
	//void* effect = Effect::effect;

	MyMenu menu;
	menu.File();

	return 0;
}

