d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
n=input().upper()
for i in n:
    for key,value in d.items():
        if i in value:
            print(key * (value.index(i)+1), end="")