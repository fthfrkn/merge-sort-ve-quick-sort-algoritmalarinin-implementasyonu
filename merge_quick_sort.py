from random import shuffle
class Merge:
    def merge(self, a, lo, mid, hi):

        i = lo
        j = mid + 1
        aux = list()            # birleştirme işlemi için ara liste.
        aux.extend(a)     # ara listeyi ilk değerlerle  doldur
        # a[lo..hi] 'yı aux[lo..hi]'ya kopyala
        for k in range(lo, hi + 1, 1):
            aux[k] = a[k]
        # a[lo..hi] üzerinde birleştir.
        for k in range(lo, hi + 1, 1):
            if i > mid:
                a[k] = aux[j]
                j = j + 1
            elif j > hi:
                a[k] = aux[i]
                i = i + 1
            elif aux[j] < aux[i]:
                a[k] = aux[j]
                j = j + 1
            else:
                a[k] = aux[i]
                i = i + 1

    def merge_sort (self, a):
        # Gelen listeyi karıştır
        shuffle(a)
        self.sort (a, 0, len(a)-1)

    # a[lo..hi]'ı sırala
    def sort(self, a, lo, hi):
        if hi <= lo :                      # base case
            return
        mid = lo + (hi - lo) //2
        self.sort(a, lo,  mid)             # sol yarıyı sırala
        self.sort(a, mid+1, hi)            # sağ yarıyı sırala
        self.merge(a, lo, mid, hi)         # sonuçları birleştir.

import  random
# Hızlı sıralama yapan sınıf

class Quick:
    # Diziyi a[lo..j-1], a[j], a[j+1..hi] olmak üzere iki parçaya böler
    def partition(self, a, lo, hi):
        i, j = lo, hi + 1  # sol ve sağ tarama indisleri
        pivot = a[lo]  # parçalama elemanı
        while (True):
            i = i + 1
            j = j - 1
            while a[i] < pivot:  # soldan sağa doğru pivottan daha büyük buluncaya kadar tara
                if i == hi:
                    break
                i = i + 1
            while pivot < a[j]:  # sağdan sola doğru pivottan daha küçük buluncaya kadar tara
                if j == lo:
                    break
                j = j - 1
            if i >= j:               # Eğer sol ve sağ işaretçiler çakıştıysa bitir.
                break

            a[i], a[j] = a[j], a[i]  # Durduğun gözlerdeki elemanları yer değiştir.

        a[lo], a[j] = a[j], a[lo]    # a[lo] ile a[j]'yi yer değiştir.
        return j                     # j'yi geri döndür.


    def quick_sort (self, a):
        random.shuffle(a)               # listeyi karıştırma adımı önemli
        self.sort (a, 0, len(a)-1)

    def sort(self, a, lo, hi):
        if hi <= lo :                           # base case
            return
        j = self.partition (a, lo, hi)        # dizi iki parçaya ayrılır.
        self.sort(a, lo,  j-1)                     # sol yarıyı sırala
        self.sort(a, j+1, hi)                     # sağ yarıyı sırala



my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
my_obj = Merge()
my_obj.merge_sort(my_list)
print(my_list)

my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
my_obj = Quick()
my_obj.quick_sort(my_list)
print(my_list)
