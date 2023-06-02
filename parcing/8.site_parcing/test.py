url = 'https://roscarservis.ru/catalog/legkovye/17570-r13-82h-viatti-strada-asimmetrico-v-130-tl55717/'
res = url.strip('/').split('-')[5:]
res = '-'.join(res)
 
print(res)
