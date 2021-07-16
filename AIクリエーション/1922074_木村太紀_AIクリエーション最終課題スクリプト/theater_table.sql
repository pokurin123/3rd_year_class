CREATE TABLE theater_table(
   id           INTEGER  NOT NULL PRIMARY KEY 
  ,name_theater VARCHAR(9) NOT NULL
  ,theater_id   INTEGER  NOT NULL
  ,theater_spot VARCHAR(8) NOT NULL
);
INSERT INTO theater_table(id,name_theater,theater_id,theater_spot) VALUES (1,'theater_A',1,'Yokohama');
INSERT INTO theater_table(id,name_theater,theater_id,theater_spot) VALUES (2,'theater_B',2,'Kouenji');
INSERT INTO theater_table(id,name_theater,theater_id,theater_spot) VALUES (3,'theater_C',3,'Kanda');
INSERT INTO theater_table(id,name_theater,theater_id,theater_spot) VALUES (4,'theater_D',4,'Itabashi');
INSERT INTO theater_table(id,name_theater,theater_id,theater_spot) VALUES (5,'theater_E',5,'Nakano');
INSERT INTO theater_table(id,name_theater,theater_id,theater_spot) VALUES (6,'theater_F',6,'Ogikubo');