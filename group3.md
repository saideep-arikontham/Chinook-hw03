
# Group 3: Filtering

## Q1

List the first 5 tracks with 'rock' in their titles, ordered by (non-null) Composer.

```
select * from Track where Name like '%rock%' and Composer!='NULL' order by Composer limit 5
```

## Q2

How many composers have 'Jimmy' in their name?

```
select count(*) as composer_count_with_jimmy_name from Track where Composer like '%Jimmy%'
```
