basic_salary=float(input('enter the basic salary:'))
hra=basic_salary*0.8
da=basic_salary*0.1
ta=basic_salary*0.05

Total_salary=basic_salary+hra+da+ta
print('the Total salary is:',Total_salary)

professional_tax=Total_salary*0.02
salary_payable=Total_salary-professional_tax
print('final salary of employee after the tax deduction:',salary_payable)