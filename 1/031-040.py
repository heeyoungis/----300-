#031
a = "3"
b = "4"
print(a + b)

#032
print("Hi" * 3)

#033
print("-" * 80)

#034
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

#035
name1 = '김민수'
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d\n이름: %s 나이: %d" % (name1, age1, name2, age2))

#036
s1 = '이름: {name1} age: {age1}'.format(name1='김민수', age1=10)
s2 = '이름: {name2} age: {age2}'.format(name2='이철희', age2=13)
print(s1)
print(s2)

#037
name1 = '김민수'
age1 = 10
name2 = "이철희"
age2 = 13
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

#038
상장주식수 = '5,969,782,550'
new = int(상장주식수.replace(",",""))
print(new, type(new))

#039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#040
data = "   삼성전자    "
data1 = data.strip()
print(data1)