
#pragma once

#ifdef DLL_MODULE_00_EXPORT
	#define DLL_MODULE_00_ENTRY __declspec(dllexport)
#else
	#ifdef DLL_MODULE_00_IMPORT
		#define DLL_MODULE_00_ENTRY __declspec(dllimport)
	#else
		#define DLL_MODULE_00_ENTRY
	#endif
#endif