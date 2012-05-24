#pragma once

class GUI
{
public:
	GUI(void);
	~GUI(void);

	void Init();

	static GUI* gui;

	static GUI* GetGUI();

	void SetCnt( int i );

private:
	int cnt;
};
