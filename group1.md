# Group 1 -- Subqueries

Investigating the most expensive invoice using subqueries and joins. Execute all the files to get the required results using the following make command.

```
make group1
```

## Q1 

What's the most expensive invoice (id and price)?

- SQL query to get the most expensive invoice price and its id is:

```
select InvoiceId, total from Invoice where total = (select max(total) from Invoice)
```

## Q2 

List the tracks (id and price) on the most expensive invoice. 
Don't hard code the desired invoice ID.
Try using a [subquery](https://www.w3schools.com/sql/sql_any_all.asp) instead.

- SQL query to list the tracks with most expensive invoice (Python's string concatenation is used in the python file):

```
select t.TrackId, t.UnitPrice from InvoiceLine il inner join Track t on t.TrackId = il.TrackId where il.InvoiceId=(select InvoiceId from Invoice where total = (select max(total) from Invoice))
```

## Q3

List the song titles from the most expensive invoice in alphabetical order.

- SQL query to list the song titles from the most expensive invoice in alphabetical order (Python's f-strings are used in the python file):

```
select t.Name from InvoiceLine il inner join Track t on t.TrackId = il.TrackId 
where il.InvoiceId=(select InvoiceId from Invoice where total = (select max(total) from Invoice)) order by t.Name
```
