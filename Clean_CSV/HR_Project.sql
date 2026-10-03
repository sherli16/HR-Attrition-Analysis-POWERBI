Use [HR Project];

select Top 10 * from HR_Employee_Attrition;

--Total Employees by Attrition

select Attrition,count(*) as Employee_Count
from HR_Employee_Attrition
group by Attrition;

--Deptwise Attrition
select Department,count(*) as Attrition_count
from HR_Employee_Attrition where Attrition=1
group by Department order by Attrition_count desc;


--OverTimewise Attrition
select OverTime,count(*) as count
from HR_Employee_Attrition where Attrition=1
group by OverTime;

--Age group wise 
select 
case 
 when Age between 18 and 30 then '18-30'
 when Age between 31 and 40 then '31-40'
 else '41+'
end as age_group,
count(*) as attrition_count
from HR_Employee_Attrition
where Attrition=1
group by
 case
 when Age between 18 and 30 then '18-30'
 when Age between 31 and 40 then '31-40'
 else '41+'
end;

--Salarywise Attrition
select JobRole,Avg(MonthlyIncome) as avg_sal
from HR_Employee_Attrition
group by JobRole,Attrition
order by Attrition;