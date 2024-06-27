# #Excel with data firstname lastname username password 50 rows
#
# #We have to login with all the username and password and verify that login is successful and store timestamp of login
# # in excel is respective row. verify correct username is displayed. verify with Excel data
#
# login
# successful
#
# driver = webdriver.chrome()
# driver.get("https://google.com")
#
# wb = openpyxl.open("file location")
# sheet = wb.worksheet["data"]
# row_ = sheet[row]
# for i in range(row_):
#     username_field = driver.find_element(By.Id, "#username")
# username_field.send_keys(sheet[])
#
str1 = 'user1&frst+Last+datetime'
#split above string and store in list one by one
datas = []
char = ""
for ele in str1:
    if (ord(ele) <= ord('z') and ord(ele) >= ord('a')) or (ord(ele) <= ord('Z') and ord(ele) >= ord('A')) or (
            ord(ele) >= ord('0') and ord(ele) <= ord('9')):
        char += ele
    else:
        datas.append(char)
        char = ""
print(datas)
#regex
import re
pattern = r'[\&\+\s]+'
list1 = re.split(pattern, str1)
print(list1)

# #table -> dynamic rows -> in one cell dropdown is there -> find count of options in dropdown

