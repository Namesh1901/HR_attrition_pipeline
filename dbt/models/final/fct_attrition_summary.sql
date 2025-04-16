-- Final table for dashboard
SELECT
    attrition,
    gender,
    department,
    COUNT(*) AS employee_count,
    AVG(monthlyincome) AS avg_income
FROM {{ ref('int_hr_attrition_features') }}
GROUP BY attrition, gender, department
