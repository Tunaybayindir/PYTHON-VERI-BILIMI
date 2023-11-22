phone=input(">Phone Number: ")
numbers={
    "0":"sıfır",
    "1":"bir",
    "2":"iki",
    "3":"üç",
    "4":"dört",
    "5":"beş",
    "6":"altı",
    "7":"yedi",
    "8":"sekiz",
    "9":"dokuz",
}
output=""
for ch in phone:
  output+=numbers.get(ch,"!")+" "
print(output)
