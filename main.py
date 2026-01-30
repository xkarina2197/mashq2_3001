# 1.3-misol

scores = [85, 90, 78, 92, 88]
print(scores)


# 1
summa = sum(scores)
print(f"Ro'yhatdagi barcha sonlar yigindisi: {summa} ga teng")

# 2
ort = summa / len(scores)
print(f"Ro'yhatning o'rtacha qiymati {ort} ga teng ")

# 4
scores.reverse()
print(scores)

# 5
print(f"Yakuniy natija: {scores} ga teng")


1.4-misol
items =[1,2,2,3,3,3,4,1]
print(items)

# 1
a = list(set(items))
print(a)

# 2
items.sort()
print(items)
# 3
first = items[0]
last = items[-1]
print(f"Birinchi element: {first} ")
print(f"oxirgi  elelment: {last}")
# 4
x = len(items)
print(f"Ro'yhat uzunligi {x} ga teng  ")
# 5
print(f"Yakuniy natija: {items} ")
