-------------------------------------------------------------
                                                   -- DOGS --
-------------------------------------------------------------

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
    -- PLEASE DO NOT CHANGE ANY DOG TABLES ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select s.size, d.name from sizes as s, dogs as d where d.height > s.min and d.height <= s.max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  with the_table as (select parent, height from parents as p, dogs as d where p.parent = d.name)
  select name from dogs as d, parents as p, the_table as t where d.name = p.child group by name order by t.height;

-- Sentences about siblings that are the same size

-- create table sentences as
create table sentences as
  with the_table as (select p1.child as child1, p2.child as child2 from parents as p1, parents as p2 where p1.parent = p2.parent and p1.child < p2.child)
  select child1 || ' and ' || child2 || ' are ' || s1.size || ' siblings' from the_table as t, size_of_dogs as s1, size_of_dogs as s2
    where s1.size = s2.size and s1.name = child1 and s2.name = child2;


-- Heights and names of dogs that are above average in height among
-- dogs whose height has the same first digit.
create table above_average as
  with the_table as (select dogs.height/10 as num, avg(dogs.height) as avgnum from dogs group by dogs.height/10 having count(*) > 1)
  select d.height, d.name from dogs as d, the_table as t where d.height/10 = t.num and d.height > t.avgnum;

-------------------------------------------------------------
                                     -- EUCLID CAFE TYCOON --
-------------------------------------------------------------

-- Locations of each cafe
create table cafes as
  select "nefeli" as name, 2 as location union
  select "brewed"        , 8             union
  select "hummingbird"   , 6;

-- Menu items at each cafe
create table menus as
  select "nefeli" as cafe, "espresso" as item union
  select "nefeli"        , "bagels"           union
  select "brewed"        , "coffee"           union
  select "brewed"        , "bagels"           union
  select "brewed"        , "muffins"          union
  select "hummingbird"   , "muffins"          union
  select "hummingbird"   , "eggs";

-- All locations on the block
create table locations as
  select 1 as n union
  select 2      union
  select 3      union
  select 4      union
  select 5      union
  select 6      union
  select 7      union
  select 8      union
  select 9      union
  select 10;

-------------------------------------------------------------
   -- PLEASE DO NOT CHANGE ANY CAFE TABLES ABOVE THIS LINE --
-------------------------------------------------------------

-- Locations without a cafe
create table open_locations as
  select n from locations, cafes group by n having min(abs(n-location)) != 0;

-- Items that could be placed on a menu at an open location
create table allowed as
  with item_locations(item, location) as (
    select item, location from cafes, menus where name = cafe
  )
  select n, item from item_locations, locations group by n, item having min(abs(n-location)) > 2;
