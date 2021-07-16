DROP TABLE IF EXISTS country;
CREATE TABLE country(
name varchar(255),
alpha2_code varchar(10),
alpha3_code varchar(10),
numeric_code integer,
location point
);

-- DROP TABLE IF EXISTS main_meta_table;

INSERT INTO country VALUES('Afghanistan', 'AF', 'AFG', 4, '(33, 65)');
INSERT INTO country VALUES('Albania', 'AL', 'ALB', 8, '(41, 20)');
INSERT INTO country VALUES('Algeria', 'DZ', 'DZA', 12, '(28, 3)');
INSERT INTO country VALUES('American Samoa', 'AS', 'ASM', 16, '(-14.3333, -170)');
INSERT INTO country VALUES('Andorra', 'AD', 'AND', 20, '(42.5, 1.6)');
INSERT INTO country VALUES('Angola', 'AO', 'AGO', 24, '(-12.5, 18.5)');
INSERT INTO country VALUES('Anguilla', 'AI', 'AIA', 660, '(18.25, -63.1667)');
INSERT INTO country VALUES('Antarctica', 'AQ', 'ATA', 10, '(-90, 0)');
INSERT INTO country VALUES('Antigua and Barbuda', 'AG', 'ATG', 28, '(17.05, -61.8)');
INSERT INTO country VALUES('Argentina', 'AR', 'ARG', 32, '(-34, -64)');
INSERT INTO country VALUES('Armenia', 'AM', 'ARM', 51, '(40, 45)');
INSERT INTO country VALUES('Aruba', 'AW', 'ABW', 533, '(12.5, -69.9667)');
INSERT INTO country VALUES('Australia', 'AU', 'AUS', 36, '(-27, 133)');
INSERT INTO country VALUES('Austria', 'AT', 'AUT', 40, '(47.3333, 13.3333)');
INSERT INTO country VALUES('Azerbaijan', 'AZ', 'AZE', 31, '(40.5, 47.5)');
INSERT INTO country VALUES('Bahamas', 'BS', 'BHS', 44, '(24.25, -76)');
INSERT INTO country VALUES('Bahrain', 'BH', 'BHR', 48, '(26, 50.55)');
INSERT INTO country VALUES('Bangladesh', 'BD', 'BGD', 50, '(24, 90)');
INSERT INTO country VALUES('Barbados', 'BB', 'BRB', 52, '(13.1667, -59.5333)');
INSERT INTO country VALUES('Belarus', 'BY', 'BLR', 112, '(53, 28)');
INSERT INTO country VALUES('Belgium', 'BE', 'BEL', 56, '(50.8333, 4)');
INSERT INTO country VALUES('Belize', 'BZ', 'BLZ', 84, '(17.25, -88.75)');
INSERT INTO country VALUES('Benin', 'BJ', 'BEN', 204, '(9.5, 2.25)');
INSERT INTO country VALUES('Bermuda', 'BM', 'BMU', 60, '(32.3333, -64.75)');
INSERT INTO country VALUES('Bhutan', 'BT', 'BTN', 64, '(27.5, 90.5)');