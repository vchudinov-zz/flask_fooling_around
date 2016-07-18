drop table if exists announcements;
create table announcements (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null,
  publication_date datetime not null
);
