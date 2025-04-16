-- Rename columns and filter NULLs
SELECT
    employeenumber,
    age,
    attrition,
	JobRole,
    department,
    educationfield,
    gender,
    overtime,
    jobsatisfaction,
    worklifebalance,
    monthlyincome,
    totalworkingyears,
    yearsatcompany
FROM hr_employee_attrition
WHERE employeenumber IS NOT NULL
