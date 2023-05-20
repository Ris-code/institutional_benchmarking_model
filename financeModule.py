'''
R_inst => Institute generated revenue in a year
Ratios => N_fac : N_staff : N_stu = Faculty : Staff : Student
S_fac => Salary of faculty
S_staff => Salary of staff
N => Total number of students
C => Institute's expenditure / costs
y % of C => Fixed cost
 
'''

# Institute's revenue after deducting fixed costs
def R_net(R_inst, C, y):
    return R_inst - (y/100 * C)

# Average net revenue
def R_avg(R_inst, C, y, N):
    return R_net(R_inst, C, y) / N

# Per-student cost of staff and faculty salaries
def C_salary(N_staff, N_fac, N_stu, S_fac, S_staff):
    return ((N_fac * S_fac) + (N_staff * S_staff)) / N_stu

# Profit margin per student
def profit_margin_per_student(R_inst, C, y, N, N_staff, N_fac, N_stu, S_fac, S_staff):
    return R_avg(R_inst, C, y, N) - C_salary(N_staff, N_fac, N_stu, S_fac, S_staff)