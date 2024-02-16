DROP TABLE IF EXISTS transaction;

CREATE TABLE transaction(
    transaction_id integer,
	product_id integer,
	customer_id integer,
	transaction_date timestamp,
	online_order bool,
	order_status varchar,
	brand varchar,
	product_line varchar,
	product_class varchar,
	product_size varchar,
	list_price float8,
	standard_cost float8
);


/*Raw customers. Drop temp table befor importing data and then create new one*/
DROP TABLE IF EXISTS customer;

CREATE TABLE customer(
    customer_id integer,
	first_name varchar,
	last_name varchar,
	gender varchar,
	DOB date,
	job_title varchar,
	job_industry_category varchar,
	wealth_segment varchar,
	deceased_indicator varchar,
	owns_car varchar,
	address varchar,
	postcode varchar,
	state varchar,
	country varchar,
	property_valuation varchar
);
/*1.Вывести все уникальные бренды,у которых стандартная стоимость выше 1500 долларов*/
 
 
SELECT DISTINCT brand 
FROM "transaction" WHERE standard_cost > 1500;


/*2.Вывести все подтвержденные транзакции
 * за период '2017-04-01' по '2017-04-09' включительно.*/

SELECT transaction_id , order_status , transaction_date  
FROM "transaction" WHERE order_status  = 'Approved' AND transaction_date::date  BETWEEN '2017-04-01' AND '2017-04-09';

/*3.Вывести все профессии у клиентов из сферы IT или Financial Services, 
 * которые начинаются с фразы 'Senior'.*/

SELECT job_title 
FROM customer WHERE (job_industry_category = 'IT' 
OR job_industry_category ='Financial Services') AND job_title::varchar LIKE 'Senior%';

/*4.Вывести все бренды, которые закупают клиенты, работающие в сфере Financial Services*/

SELECT brand, job_industry_category
FROM "transaction"  AS t
JOIN customer AS c ON t.customer_id = c.customer_id 
WHERE job_industry_category = 'Financial Services' ;
DELETE FROM "transaction" WHERE brand = '' OR brand IS NULL
  
/*5.Вывести 10 клиентов, которые оформили онлайн-заказ продукции 
из брендов 'Giant Bicycles', 'Norco Bicycles', 'Trek Bicycles'.*/


SELECT first_name, last_name, online_order, brand 
FROM "transaction" AS t
JOIN customer AS c ON t.customer_id = c.customer_id 
WHERE (brand = 'Giant Bicycles' OR  brand = 'Norco Bicycles' OR brand = 'Trek Bicycles')AND online_order = 'True'
LIMIT 10;

/* 6.Вывести всех клиентов, у которых нет транзакций.*/

SELECT  cs.customer_id
FROM customer cs
LEFT JOIN transaction tr
ON tr.customer_id = cs.customer_id
WHERE  tr.transaction_id is NULL
ORDER BY cs.customer_id;


/*7 Вывести всех клиентов из IT, у которых транзакции с максимальной стандартной стоимостью. */


SELECT first_name,last_name, transaction_id, job_industry_category, standard_cost 
FROM "transaction" AS t
JOIN customer AS c ON t.customer_id = c.customer_id 
WHERE( standard_cost = (
SELECT MAX(standard_cost) FROM "transaction" ))
AND job_industry_category = 'IT';

/*8 Вывести всех клиентов из сферы IT и Health, у которых есть подтвержденные 
транзакции за период '2017-07-07' по '2017-07-17'*/


SELECT transaction_id, job_industry_category, transaction_date, order_status
FROM "transaction" AS t
JOIN customer AS c ON t.customer_id = c.customer_id 
WHERE (transaction_date BETWEEN '2017-07-07' AND '2017-07-17') 
AND( job_industry_category = 'IT' or job_industry_category = 'Health') 
AND order_status = 'Approved';






