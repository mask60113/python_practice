import os #operating system


def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價錢' in line:
				continue
			name, price = line.strip().split(',') #先去\n，再用逗號分割
			products.append([name,price])
	return products
#讓使用者輸入
def user_info(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append([name, price])
	print(products)
	return products


#印出所有購買紀錄
def print_products(products):
	for product in products:
		print(product[0], '的價格為 ', product[1])

#寫入檔案
def write_file(filename, products):
	with open(filename,'w',encoding='utf-8') as f:
		f.write('商品,價錢\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

# Excel讀取標頭會亂碼，必須使用utf-8寫入
# 但讀取時也要用utf-8，excel 要從Data 匯入，選擇utf-8並使用逗號做分割


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢察檔案在不在
		print('找到檔案了')
		products = read_file(filename)
	else:
		print('找不到檔案...')

	products = user_info(products)
	print_products(products)
	write_file('products.csv',products)

main()








