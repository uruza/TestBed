// HTTPUpload.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

#include <windows.h>
#include <WinInet.h>


int _tmain(int argc, _TCHAR* argv[])
{
	for ( UINT i = 0; i < 9999; i++ )
	{

		HINTERNET hInternet = NULL;
		HINTERNET hURL = NULL;
		//-----------------
		// InternetOpen()
		hInternet = InternetOpen(	L"TEST",
									INTERNET_OPEN_TYPE_DIRECT,
									NULL,
									NULL,
									0 );
		if ( hInternet == NULL )
			return FALSE;

		//---------------------
		// InternetOpenUrl()
		hURL = InternetOpenUrl( hInternet,
								L"http://yblacktest.appspot.com/?os=windows xp&cpu_arch=Intel i7&cpu_num=8&phys_mem_total=4000&res_x=1920&res_y=1200&gpu=6600gt&vram_total=2000",
								NULL,
								0,
								INTERNET_FLAG_RELOAD,
								0 );
	//	if ( hURL == NULL )
	//	{
	////		InternetCloseHandle( hInternet );
	////		return FALSE;
	//	}

		if ( hURL )
		{
			InternetCloseHandle( hURL );
			hURL = NULL;
		}

		if( hInternet )
		{
			InternetCloseHandle( hInternet );
			hInternet = NULL;
		}

	}

	return 0;
}

