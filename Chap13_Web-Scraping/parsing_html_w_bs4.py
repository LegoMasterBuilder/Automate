import requests, bs4

res = requests.get('https://autbor.com/example3.html')
res.raise_for_status()
example_soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(example_soup))

with open('example3.html') as example_file:
    example_soup = bs4.BeautifulSoup(example_file, 'html.parser')

print(type(example_soup))

soup = bs4.BeautifulSoup(open('example3.html'), 'html.parser')
span_elem = soup.select('span')[0]
print(str(span_elem))
print(span_elem.get('id'))
print(span_elem.get('some_nonexistent_addr') == None)
print(span_elem.attrs)
