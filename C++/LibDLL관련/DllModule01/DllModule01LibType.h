
#pragma once

#ifdef DLL_MODULE_01_EXPORT
	#define DLL_MODULE_01_ENTRY __declspec(dllexport)
#else
	#ifdef DLL_MODULE_01_IMPORT
		#define DLL_MODULE_01_ENTRY __declspec(dllimport)
	#else
		#define DLL_MODULE_01_ENTRY
	#endif
#endif