
x = 3.145

str_x = str(x)
dp = str_x.find('.')
num_before_dp = str_x[0:dp]
num_after_dp = str_x[dp + 1]

if int(num_after_dp) >= 5:
    rounded_number = int(num_before_dp) + 1
    print rounded_number
else:
    print int(num_before_dp)