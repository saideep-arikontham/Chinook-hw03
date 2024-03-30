
# Group 2 -- Popular genres

## Q1

Which country purchased the most music and how much did it spend? (f-strings used)

```
select BillingCountry, Total_spent from (select BillingCountry, sum(Total) as Total_spent from Invoice group by BillingCountry) where Total_spent = (select max(Total_spent) from (select BillingCountry, sum(Total) as Total_spent from Invoice group by BillingCountry))
```
## Q2

What was the most popular genre and how much did it generate in sales? (f-strings used, python query strings included inorder to avoid confusion)

```
s1 = '''select t.GenreId, il.UnitPrice from Track t inner join InvoiceLine il on t.TrackId=il.TrackId'''
s2 = f'''select g.Name, sum(s1.UnitPrice) sales from Genre g inner join ({s1}) s1 on s1.GenreId = g.GenreId group by g.Name'''
s3 = f'''select Name,sales from ({s2}) where sales = (select max(sales) from ({s2}))'''
```

## Q3

What was the most popular genre in the U.S. and how much did it generate in sales? (f-strings used, python query strings included inorder to avoid confusion)

```
s = '''select il.TrackId, il.UnitPrice from InvoiceLine il inner join Invoice i on il.InvoiceId = i.InvoiceId
        where i.BillingCountry = 'USA' '''
s1 = f'''select t.GenreId, s.UnitPrice from Track t inner join ({s}) s on t.TrackId=s.TrackId'''
s2 = f'''select g.Name, sum(s1.UnitPrice) sales from Genre g inner join ({s1}) s1 on s1.GenreId = g.GenreId 
    group by g.Name'''
s3 = f'''select Name,sales from ({s2}) where sales = (select max(sales) from ({s2}))'''
```
