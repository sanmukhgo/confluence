from parser import soup
import link
import htag


def parse_list(tag):
    if tag.name == 'ul':
        return [parse_list(item)
                for item in tag.find_all('li', recursive=False)]
    elif tag.name == 'li':
        if tag.ul is None:
            return tag.text
        else:
            return [tag.contents[0].string.strip(), parse_list(tag.ul)]

data=[]
m = soup.find('div', {'id': 'main-content'})

try:
    for i in m.children:
        if i.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            data.append({'tag': i.name,
                         'text': i.text.strip(),
                         'ul': [],
                         'table': [],
                         'subheads': []})

        if i.name == 'ul':
            temp = parse_list(i)
            data[-1]['ul'].append(temp)

        try:
            lst = i.get_attribute_list('class')
            if 'table-wrap' in lst:
                tbl = []
                row = []
                for j in i.find_all('th'):
                    txt = j.text.strip()
                    row.append(txt)
                if row!=[]:
                    tbl.append(row)

                for k in i.find_all('tr'):
                    row=[]
                    for l in k.find_all('td'):
                        '''txt = parse_list(l.ul)
                        if txt == None:'''
                        txt=l.text.strip()
                        row.append(txt)
                    if row!=[]:
                        tbl.append(row)
                if(tbl != []):
                    data[-1]['table'].append(tbl)
        except:
            pass
except:
    pass

for i in data:
    for j, k in i.items():
        print(j, " : ", k)
    print()
