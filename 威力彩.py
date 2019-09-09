from 爬蟲_威力 import winner_number

n = winner_number()
global zone1
global zone2

zone1 = n[:6]
zone2 = n[6:]

print(f'第一區號碼{zone1},第二區號碼{zone2}')


def weli():
	winzone1 = []
	i = 0
	while i < 6:
		z1 = input('請輸入第一區號碼: ')
		if z1 == 'n':
			return None
			break
		elif not z1.isdigit() or 39<int(z1) or int(z1)<1:     #x.isdigit() 檢查輸入的是否為數字
			print('輸入錯誤')
			continue
		if z1 in zone1:
			winzone1.append(z1)
		i += 1
	return len(winzone1)
	
def weli_z2():
	while True:
		z2 = input('請輸入第二區號碼: ')
		if z2 == 'n':
			return None
			break
		elif not z2.isdigit() or 9<int(z2) or int(z2)<1 :     #x.isdigit() 檢查輸入的是否為數字
			print('輸入錯誤')
		else:
			break
	if z2 in zone2:
		return 1
	else:
		return 0

def reward():
	win1 = weli()
	if win1 == None:
		return 0
	win2 = weli_z2()

	x = [win1,win2]

	if x == [1,1]:
		print('你中了普獎')
	elif x == [3,0]:
		print('你中了9獎')
	elif x == [2,1]:
		print('你中了8獎')
	elif x == [3,1]:
		print('你中了7獎')
	elif x == [4,0]:
		print('你中了6獎')
	elif x == [4,1]:
		print('你中了5獎')
	elif x == [5,0]:
		print('你中了4獎')
	elif x == [5,1]:
		print('你中了3獎')
	elif x == [6,0]:
		print('你中了2獎')
	elif x == [6,1]:
		print('你中了頭獎')
	else:
		print('你沒中獎')


def main():
	while True:
		if reward() == 0:
			break
		else:
			x = input('繼續對嗎?Y OR N: ' )
			if x == 'N'or x == 'n':
				break
main()
	

