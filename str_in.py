ng = 'free'
str = 'adamfreelance'
if ng in str:
    print('含まれています')
else:
    print('含まれていません')

print('含まれています' if ng in str else '含まれていません')

