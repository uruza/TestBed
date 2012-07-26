#include "StdAfx.h"
#include "DataStore.h"

DataStore::DataStore(void)
{
}

DataStore::~DataStore(void)
{
	if ( 0 != que.size() )
	{
		assert( 0 );
	}
}

void DataStore::PushData()
{
	Data* pData = new Data;
	pData->name = 9;
	pData->number = 8;

	que.push_back( pData );
}

void DataStore::RemoveAllData()
{
	for ( stl_it it = que.begin(); it != que.end();  )
	{
		Data* pData = *it;
		it = que.erase( it );

		delete pData;
		pData = NULL;
	}
}
