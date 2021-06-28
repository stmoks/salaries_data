import pandas as pd

raw_data = pd.read_csv('salaries_by_college_major.csv')


# data exploration
# print(f'\nHead:\n {raw_data.head()}')
# print(f'\nShape:\n {raw_data.shape}')

# print(f'\nColumns:\n {raw_data.columns}')

clean_data = raw_data.dropna()

# print(f'\nTail:\n {clean_data.tail()}')


# # Highest starting median salary

# max_salary = clean_data['Starting Median Salary'].max()
# print(clean_data[clean_data['Starting Median Salary'] == max_salary])

# # or...
# id_max = clean_data['Starting Median Salary'].idxmax()
# print(clean_data.loc[id_max])



# # Highest mid-career salary
# max_salary = clean_data['Mid-Career Median Salary'].max()
# print(clean_data[clean_data['Mid-Career Median Salary'] == max_salary])

# # Lowest starting salary
# min_salary = clean_data['Starting Median Salary'].min()
# print(clean_data[clean_data['Starting Median Salary'] == min_salary])


# Low risk majors
salary_spread = clean_data['Mid-Career 90th Percentile Salary'] - clean_data['Mid-Career 10th Percentile Salary']
clean_data.insert(1,'Salary spread',salary_spread)
low_risk = clean_data['Salary spread'].min()
print(clean_data[clean_data['Salary spread'] == low_risk])

#or...
print(clean_data.sort_values('Salary spread').head())



# Number of majors per group
print(clean_data.groupby('Group').count())

# Average salary per group
pd.options.display.float_format = '{:,.2f}'.format 
print(clean_data.groupby('Group').mean().sort_values(['Starting Median Salary'],ascending=False))






