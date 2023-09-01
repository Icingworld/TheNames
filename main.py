from database import Database

db = Database()
db.setName("name.db")
db.open()

# 获取 中文 姓
def getSurname(length: int = 1, num: int = 1) -> list:
    return db.search(f"SELECT name FROM surname WHERE len = \"{length}\" ORDER BY RANDOM() LIMIT \"{num}\";")

# 获取 中文 名
def getFirstNameCn(sex: int, length: int, num: int = 10) -> list:
    return db.search(f"SELECT name FROM firstnamecn WHERE sex = \"{sex}\" AND len = \"{length}\" ORDER BY RANDOM() LIMIT \"{num}\";")

# 获取 中文 全名
def getNameCn(sex: int, xing_length: int = 1, ming_length: int = 2, num: int = 10) -> list:
    nameList = []
    xingList = getSurname(xing_length, num)
    mingList = getFirstNameCn(sex, ming_length, num)
    for i in range(num):
        nameList.append(xingList[i] + mingList[i])
    return nameList

# print(getFirstNameCn(0, 2, 100))

# print(getSurname(num=10))

print(getNameCn(1, 1, 2, 100))