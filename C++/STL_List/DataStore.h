#pragma once

class DataStore
{
	class Data
	{
	public:
		int name;
		int number;
	};

	typedef list<Data*>			stl_list;
	typedef stl_list::iterator	stl_it;

public:
	DataStore(void);
	~DataStore(void);

	void PushData();
	void RemoveAllData();

	stl_list que;
};
