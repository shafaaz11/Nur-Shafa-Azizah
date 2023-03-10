def linearSearch(mylist, char): 
    for sub_list in mylist: 
        if char in sub_list:
            idx = mylist.index(sub_list)
            sub_idx = sub_list.index(char)
            return(print('Item', item, 'berada di Index ke', idx, 'dan Kolom ke', sub_idx))

    raise ValueError("'{char}' is not in list".format(char = char))


var = ['Arsel','Avivah','Daiva', ['Wahyu','Wibi']]
item = str(input('Masukkan item yang ingin dicari: '))
find_item = linearSearch(var, item)


print(find_item)

