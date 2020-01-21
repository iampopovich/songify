create table userSongs (
	songID integer primary key autoincrement , 
	chatID integer ,
	songName varchar,
	deadlineBefore datetime,
	textComplete bool default false,
	tabsComplete bool default false)