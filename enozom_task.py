import hashlib # for MD5 Hashing
file = open('annual-enterprise-survey-2020-financial-year-provisional-csv.csv')
result = ''
x=0
for line in file:
    if x % 2 == 1: # check for odd rows
        column = line.split(',')[2]
        result += column
    x+=1
# hashing the result
result_md5 = hashlib.md5(result.encode()) 
final_hash = result_md5.hexdigest().upper()
print('Result : {}'.format(result))
print('MD5 hashed string:{}'.format(final_hash))