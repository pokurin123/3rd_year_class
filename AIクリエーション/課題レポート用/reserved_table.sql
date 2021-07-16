CREATE TABLE reserved_table(
   movie_title   VARCHAR(26) NOT NULL PRIMARY KEY
  ,name_theater  VARCHAR(10) NOT NULL
  ,month_playing INTEGER  NOT NULL
  ,theater_spot  VARCHAR(10) NOT NULL
);
INSERT INTO reserved_table(movie_title,name_theater,month_playing,theater_spot) VALUES ('test','test',0,'test');