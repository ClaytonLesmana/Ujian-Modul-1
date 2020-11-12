list1=[5,3,2,8,1,4]
# print(len(list1))
def fungsi2(x):
    _index_even=[] #2,3,5
    angka_even=[] #2,4,8
    _index_odd=[] #0,1,4
    angka_odd=[] #5,3,1
    for i in range(len(x)): #0,1,2,3,4,5 #looping berdasarkan panjang list input
        if x[i]%2==0: #cek apakah elemen x[i] even numbers
            _index_even.append(i) #kalau elemen x[i] berupa even number, maka index dari elemen tersebut akan masuk ke list ini #2,3,5
            angka_even.append(x[i]) #dan value dari elemen tersebut akan masuk ke list ini. #2,4,8
        else:
            _index_odd.append(i) #if the output is odd then append index
            angka_odd.append(x[i]) #append the number 
    angka_even.sort(reverse=True) #mengurutkan angka di list angka dari besar ke kecil. #8,4,2
    angka_odd.sort() #odd ascending order
    for i in range(len(_index_even)):  #mengubah nilai angka pada list input mesuai urutan yang di mau 
        x[_index_even[i]]=angka_even[i] 
    for i in range(len(_index_odd)):  #mengubah nilai angka pada list input mesuai urutan yang di mau 
        x[_index_odd[i]]=angka_odd[i]
    return x

print(fungsi2(list1))


# odd ascending
# even descending