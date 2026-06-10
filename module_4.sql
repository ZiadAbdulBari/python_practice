create database movie_db;
use movie_db;
create table Movies(
MovieId int primary key,
Title varchar(100),
Genre varchar(100),
ReleaseYear year,
Rating decimal(10,1),
BoxOfficeRevenue bigint,
Director varchar(100)
);
insert into movies
values
(1, 'Inception', 'Sci-Fi', 2010, 8.8, 830000000, 'Christopher Nolan'),
(2, 'Titanic', 'Romance', 1997, 7.8, 2200000000, 'James Cameron'),
(3, 'The Godfather', 'Crime', 1972, 9.2, 134000000, 'Francis Ford Coppola'),
(4, 'Avatar', 'Sci-Fi', 2009, 7.9, 2840000000, 'James Cameron'),
(5, 'Interstellar', 'Sci-Fi', 2014, 8.6, 677000000, 'Christopher Nolan'),
(6, 'Parasite', 'Thriller', 2019, 8.6, 264000000, 'Bong Joon Ho'),
(7, 'The Dark Knight', 'Action', 2008, 9.0, 1000000000, 'Christopher Nolan'),
(8, 'Schindler''s List', 'Drama', 1993, 9.0, 322000000, 'Steven Spielberg'),
(9, 'The Shawshank Redemption', 'Drama', 1994, 9.3, 28300000, 'Frank Darabont'),
(10, 'Pulp Fiction', 'Crime', 1994, 8.9, 213000000, 'Quentin Tarantino');
select * from movies where Director="Christopher Nolan";
select distinct Genre from movies;
select Title from movies order by Rating desc limit 5;
select Title from movies where ReleaseYear<2000;
select Genre,count(Title) as number_Of_movies from movies group by Genre;
select sum(BoxOfficeRevenue) as total_revenue from movies where Genre="Sci-Fi";
select Title from movies where Rating>8.5 And Rating<9.0;
select Title from movies where Title like "%The%";
select Title,BoxOfficeRevenue from movies where BoxOfficeRevenue=(select max(BoxOfficeRevenue) from movies);
select avg(Rating) as avg_rating from movies where ReleaseYear>2000;