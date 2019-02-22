products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

for product in products:
	print(product[0], '的價格為 ', product[1])

with open('products.csv','w',encoding='utf-8') as f:
	f.write('商品名稱,價錢\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

# Excel讀取標頭會亂碼，必須使用utf-8寫入
# 但讀取時也要用utf-8，excel 要從Data 匯入，選擇utf-8並使用逗號做分割