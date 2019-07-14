## Description

> Sales Records API endpoint with Django Rest Framework and Django Filters

## System Requirements

- Python 3.6+
- pip3
- virtualenv

## Dependencies

<!-- > See [requirements.txt](https://github.com/talented/djangoAPI_task/blob/master/requirements.txt) for more information. -->

## Build Instructions

1. Create a virtual environment

```
(OSX)
python3 -m venv .env

(Linux)
virtualenv .env
```

2. Activate virtual environment

```
. .venv/bin/Activate
```

3. Install modules by running 'requirements.txt'

```
pip3 install -r requirements.txt
```

4. Configure settings for postgresql database

## API filters

> GET {website}/api/sales display a DRF List API view. Avaliable filter types are listed below:

### Filter by Field name

- for filtering by field names like `country=Germany`, `region=Europe` or same values for sale price like `price=500`

### Filter by date

- for exact date filtering like `date=01.06.2017`
- `date_to` - # filter by date as "is_less_than_or_equal_to" in format "%d.%m.%Y"
- `date_from` - # filter by date as "is_greater_than_or_equal_to" in format "%d.%m.%Y"

### Filter by 'LESS THAN OR EQUAL TO' & 'GREATER THAN OR EQUAL TO'

- Defining minimum and maximum value filters in a row for numeric fields ('quantity', 'price', 'cost', 'revenue', 'profit', 'profit_percentage') to be used in filtering as "is_less_than_or_equal_to" and "is_greater_than_or_equal_to"
- Usage is as `min_revenue=10000` or `max_price`

### Ordering Filter

- `ordering` - to order queryset in ascending or descending as `ordering=quantity` ASC or `ordering=-quantity` DESC

### Grouping Filter

- `groupby` - to group by one or more columns: date, region, country, ptype, channel (not numeric columns) with a result of total values of quantity, price, cost, revenue, profit and calculated profit_percentage of total revenue and total profit

### Search Filter

- `search` - to make a case insensitive search in values for all items in a queryset
- Usage is as `search=Meat` or even `search=Me`. First search will return items with ptype=Meat, second one will also return items like region=North America

## USE-CASE TESTS

1. Show the number of quantity and total cost of sales before 1st of June 2015, broken down by channel and country, sorted by profit_percentage in descending order.

> GET {website}/api/sales?groupby=country&groupby=channel&date_to=01.06.2015&ordering=-profit_percentage

2. Show the total cost of products in May of 2017 on ptype, broken down by date, sorted by date in ascending order.

> GET {website}/api/sales?groupby=ptype&groupby=date&date_from=01.03.2010&date_to=31.03.2010&ordering=date

3. Show revenue, earned in 2015 in Europe region, broken down by country and sorted by revenue in descending order.

> GET {website}/api/sales?region=Europe&groupby=country&date_from=01.01.2015&date_to=31.12.2015&ordering=-revenue

4. Show profit percentage for Turkey broken down by channel ordered by profit percentage in descending order.

> GET {website}/api/sales?country=Turkey&groupby=channel&ordering=-profit_percentage
