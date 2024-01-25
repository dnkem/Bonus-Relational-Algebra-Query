# https://www.w3schools.com/python/pandas/ref_df_query.asp
# https://note.nkmk.me/en/python-pandas-query/
# https://mode.com/blog/set-operations-python-sql
# https://www.kdnuggets.com/2019/11/set-operations-applied-pandas-dataframes.html#:~:text=Set%20Operations%20in%20Pandas,Difference%3A%20isin()%20%2B%20Boolean%20indexing
# https://www.w3schools.com/python/pandas/ref_df_drop_duplicates.asp#:~:text=The%20drop_duplicates()%20method%20removes,considered%20when%20looking%20for%20duplicates.
# https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/
# https://note.nkmk.me/en/python-pandas-str-contains-match/
# https://github.com/dnkem/Bonus-Relational-Algebra-Query
# importing pandas package
import pandas as pd # installed pip3 and pandas

def add_to_df(data, key, value):
data[key].append(value)

def add_employee_tuple(data):
print("\nPlease enter your employee info: ")
data_id = int(input("Employee id: "))
data_name = input("Employee name: ")
data_age = int(input("Employee age: "))
data_dep = input("Employee department: ")
print("-----------------------------------------")
data["id"].append(data_id)
data["name"].append(data_name)
data["age"].append(data_age)
data["department"].append(data_dep)

def add_grad_student(grad_student):
print("\nPlease enter your grad student info: ")
stu_id = int(input("Grad student id: "))
stu_name = input("Grad student name: ")
stu_age = int(input("Grad student age: "))
stu_email = input("Grad student email: ")
print("-----------------------------------------")
grad_student["id"].append(stu_id)
grad_student["name"].append(stu_name)
grad_student["age"].append(stu_age)
grad_student["email"].append(stu_email)

def add_department(department):
print("\nPlease enter your department info: ")
dep_name = input("Department name: ")
dep_budget = int(input("Department budget: "))
print("-----------------------------------------")
department["name"].append(dep_name)
department["budget"].append(dep_budget)


def query_selection(dataFrame):
print("\nSELECTION--------------------------------")
y = input("Enter '1' if you're querying a number attribute, or '2' if a string attribute: ")
if y == '1':
    attribute = input("Input attribute: ")
    operator = input("Input operator: ")
    query_value = input("Input value: ")
    print(dataFrame.query(attribute + operator + query_value))
elif y == '2':
    attribute2 = input("Input attribute: ")
    query_value2 = input("Input word you are searching for: ")
    # print(df[attribute2].isin([query_value2]))
    print(dataFrame.query(attribute2 + '==' + query_value2))
    # print(df.query(attribute2.str.contains(query_value2)))
else:
    print("Please try again")

def query_projection(df):
print("\nPROJECTION------------------------------------")
z = input("'1' for single column, '2' for more than 1 column: ")
attribute = input("Input attribute(s) (separate by space if needed): ")
if z == '1':
    print(df[attribute])
elif z == '2':
    attrs = attribute.split()
    projection_df = df.get(attrs)
    print(projection_df) 
else:
    print("Please try again")

def main():

x = 10
employee = {
    "id" : [],
    "name" : [],
    "age" : [],
    "department" : []
}

grad_student = {
    "id" : [],
    "name" : [],
    "age" : [],
    "email" : []
}

department = {
    "name" : [],
    "budget": []
}

df = pd.DataFrame(employee)
df2 = pd.DataFrame(grad_student)
df3 = pd.DataFrame(department)

while x != 0: 
    print("")
    print("Options: ")
    print("1. Add employee")
    print("2. Add grad student")
    print("3. Add department")
    print("4. Print a relation")
    print("5. Query selection")
    print("6. Query projection")
    print("7. Query join")
    print("8. Query set")
    print("9. Make your own query selection")
    print("0. Quit")
    x = int(input("Input Your choice: "))

    if x == 1:
        add_employee_tuple(employee)
    elif x == 2:
        add_grad_student(grad_student)
    elif x == 3:
        add_department(department)
    elif x == 4:
        p = input("Enter: \n'1' for print of employee relation \n'2' for print of grad student relation \n'3' for print of department relation: ") 
        if p == '1':
            print(df)
        elif p =='2':
            print(df2)
        elif p == '3':
            print(df3)
    elif x == 5:
        k = input("Enter: \n'1' for query selection of employee \n'2' for query selection of grad student \n'3' for query selection of department: ")
        if k == '1':
            query_selection(df)
        elif k =='2':
            query_selection(df2)
        elif k == '3':
            query_selection(df3)
        else:
            print("Please try again")

    elif x == 6:
        pr = input("Enter: \n'1' for query projection of employee \n'2' for query projection of grad student \n'3' for query projection of department: ")
        if pr == '1':
            query_projection(df)
        elif pr =='2':
            query_projection(df2)
        elif pr == '3':
            query_projection(df3)
        else:
            print("Please try again")


    elif x == 7:
        print("\nJOIN OPERATIONS---------------------------")
        print("Query join is available for employee and department")
        d = input("Enter: \n'1' for Inner join, \n'2' for outer join, \n'3' for left join \n'4' for right join \n'5' natural join: ")
        if d == '1':
            inner_joined = pd.concat([df, df3], axis=1, join="inner", )
            print(inner_joined)
        elif d == '2':
            outer_joined = pd.concat([df, df3], axis=1)
            print(outer_joined)
        elif d == '3':
            left_join = pd.merge(df,df3,on="name",how='left')
            print(left_join)
        elif d == '4':
            left_join = pd.merge(df,df3,on="name",how='right')
            print(left_join)
        elif d == '5':
            natural_join = df
            for i in range(len(department["budget"])):
                natural_join = natural_join.assign(budget=department["budget"][i])
            print(natural_join)


    elif x == 8:
        print("\nSET OPERATIONS ------------------------------")
        print("Query set is available for employee and grad student")
        b = input("To intersect the 2 relations enter '1',\nTo union the 2 relations enter '2', \nTo minus a relation enter '3': ")
        if b == '1':
            employee_and_gradstu = df.merge(df2)
            print(employee_and_gradstu) #inner merge

        elif b == '2':
            all = pd.concat([df,df2], ignore_index=True)
            all = all.drop_duplicates(subset="name")
            print(all)

        elif b == '3':
            c = input("Enter '1' to exclude the Employees, or '2' to exclude the Grad Students: ")
            if c == '1':
                emp_not_stu = df[df.id.isin(df2.id) == False]
                print(emp_not_stu)
            elif c == '2':
                stu_not_emp = df2[df2.id.isin(df.id) == False]
                print(stu_not_emp)

    elif x == 9:
        q = input("Enter: \n'1' for query projection of employee \n'2' for query projection of grad student \n'3' for query projection of department: ")
        diy = input("Enter your **own** query selection: ")
        if q == '1':
            print(df.query(diy))
        elif q =='2':
            print(df2.query(diy))
        elif q == '3':
            print(df3.query(diy))
        else:
            print("Please try again")
        
    
    elif x != 0:
        print("Please try another value")


    # updates after each loop
    df = pd.DataFrame(employee)
    df2 = pd.DataFrame(grad_student)
    df3 = pd.DataFrame(department)

main()

#print(df.query('age > 35'))
