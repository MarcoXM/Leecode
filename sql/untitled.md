# SELECT within SUM and COUNT



#### World Country Profile: Aggregate functions

This tutorial is about aggregate functions such as COUNT, SUM and AVG. An aggregate function takes many values and delivers just one value. For example the function SUM would aggregate the values 2, 4 and 5 to deliver the single value 11.

| name | continent | area | population | gdp |
| :--- | :--- | :--- | :--- | :--- |
| Afghanistan | Asia | 652230 | 25500100 | 20343000000 |
| Albania | Europe | 28748 | 2831741 | 12960000000 |
| Algeria | Africa | 2381741 | 37100000 | 188681000000 |
| Andorra | Europe | 468 | 78115 | 3712000000 |
| Angola | Africa | 1246700 | 20609294 | 100990000000 |
| ... |  |  |  |  |

### You might want to look at these examples first

[Using SUM, Count, MAX, DISTINCT and ORDER BY](https://sqlzoo.net/wiki/Using_SUM,_Count,_MAX,_DISTINCT_and_ORDER_BY).

1. Show the total **population** of the world.

```sql
SELECT SUM(population)
FROM world
```

  
2.List all the continents - just once each.

```sql
SELECT DISTINCT continent
FROM world
```

3. Give the total GDP of Africa

```sql
SELECT SUM(gdp)
FROM world
WHERE continent = 'Africa';
```

4.How many countries have an **area** of at least 1000000

```sql
SELECT COUNT(name)
FROM world
WHERE area >= 1000000;
```

  
5.What is the total **population** of \('Estonia', 'Latvia', 'Lithuania'\)

```sql
SELECT SUM(population)
FROM world
WHERE name in  ('Estonia', 'Latvia', 'Lithuania');
```

  
6.For each **continent** show the **continent** and number of countries.

```sql
SELECT continent ,COUNT(name)
FROM world
GROUP BY continent;
```

  
7.For each **continent** show the **continent** and number of countries with populations of at least 10 million.

```sql
SELECT continent ,COUNT(name)
FROM world
WHERE population >= 10000000
GROUP BY continent;
```

  
8.List the continents that **have** a total population of at least 100 million.

```sql
SELECT continent 
FROM world
GROUP BY continent
HAVING sum(population) >= 100000000
```











