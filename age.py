driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有喔')
	raise SystemExit	

age = input('請輸入你的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('很棒喔，你會開車了')
	else:
		print('你還不行開車喔!')
elif driving == '沒有':
	if age >= 18:
		print('可以去考駕照囉!')
	else:
		print('再過幾年就可以考駕照了')
