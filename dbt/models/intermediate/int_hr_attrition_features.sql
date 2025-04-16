-- models/fct_employee_attrition.sql
WITH base AS (
    SELECT * FROM {{ ref('stg_hr_employee_attrition') }}
)

SELECT
    *,
    CASE
        WHEN yearsatcompany < 2 THEN '0-2 Years'
        WHEN yearsatcompany BETWEEN 2 AND 5 THEN '2-5 Years'
        ELSE '5+ Years'
    END AS tenure_bucket
FROM base

