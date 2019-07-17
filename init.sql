COPY app_sales(region,country,ptype,channel,date,quantity,price,cost,revenue,profit)
FROM '/var/lib/postgresql/data/pgdata/2000_Sales_Records.csv' DELIMITER ';' CSV HEADER;