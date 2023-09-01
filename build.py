from database import Database
import requests
from bs4 import BeautifulSoup

# init database
db = Database()
db.setName("name.db")
db.open()

# 中文 姓
if 1:
    bai_jia_xing = [
        "赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈",
        "褚", "卫", "蒋", "沈", "韩", "杨", "朱", "秦", "尤", "许",
        "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏",
        "陶", "姜", "戚", "谢", "邹", "喻", "柏", "水", "窦", "章",
        "云", "苏", "潘", "葛", "奚", "范", "彭", "郎", "鲁", "韦",
        "昌", "马", "苗", "凤", "花", "方", "俞", "任", "袁", "柳",
        "酆", "鲍", "史", "唐", "费", "廉", "岑", "薛", "雷", "贺",
        "倪", "汤", "滕", "殷", "罗", "毕", "郝", "邬", "安", "常",
        "乐", "于", "时", "傅", "皮", "卞", "齐", "康", "伍", "余",
        "元", "卜", "顾", "孟", "平", "黄", "和", "穆", "萧", "尹",
        "姚", "邵", "湛", "汪", "祁", "毛", "禹", "狄", "米", "贝",
        "明", "臧", "计", "伏", "成", "戴", "谈", "宋", "茅", "庞",
        "熊", "纪", "舒", "屈", "项", "祝", "董", "梁", "杜", "阮",
        "蓝", "闵", "席", "季", "麻", "强", "贾", "路", "娄", "危",
        "江", "童", "颜", "郭", "梅", "盛", "林", "刁", "钟", "徐",
        "邱", "骆", "高", "夏", "蔡", "田", "樊", "胡", "凌", "霍",
        "虞", "万", "支", "柯", "昝", "管", "卢", "莫", "白", "房",
        "裘", "缪", "干", "解", "应", "宗", "丁", "宣", "贲", "邓",
        "郁", "单", "杭", "洪", "包", "诸", "左", "石", "崔", "吉",
        "钮", "龚", "程", "嵇", "邢", "滑", "裴", "陆", "荣", "翁",
        "荀", "羊", "于", "惠", "甄", "曲", "家", "封", "芮", "羿",
        "储", "靳", "汲", "邴", "糜", "松", "井", "段", "富", "巫",
        "乌", "焦", "巴", "弓", "牧", "隗", "山", "谷", "车", "侯",
        "宓", "蓬", "全", "郗", "班", "仰", "秋", "仲", "伊", "宫",
        "宁", "仇", "栾", "暴", "甘", "钭", "历", "戎", "祖", "武",
        "符", "刘", "景", "詹", "束", "龙", "叶", "幸", "司", "韶",
        "郜", "黎", "蓟", "溥", "印", "宿", "白", "怀", "蒲", "邰",
        "从", "鄂", "索", "咸", "籍", "赖", "卓", "蔺", "屠", "蒙",
        "池", "乔", "阳", "郁", "胥", "能", "苍", "双", "闻", "莘",
        "党", "翟", "谭", "贡", "劳", "逄", "姬", "申", "扶", "堵",
        "冉", "宰", "郦", "雍", "却", "璩", "桑", "桂", "濮", "牛",
        "寿", "通", "边", "扈", "燕", "冀", "姓", "浦", "尚", "农",
        "温", "别", "庄", "晏", "柴", "瞿", "阎", "充", "慕", "连",
        "茹", "习", "宦", "艾", "鱼", "容", "向", "古", "易", "慎",
        "戈", "廖", "庾", "终", "暨", "居", "衡", "步", "都", "耿",
        "满", "弘", "匡", "国", "文", "寇", "广", "禄", "阙", "东",
        "欧", "殳", "沃", "利", "蔚", "越", "夔", "隆", "师", "巩",
        "厍", "聂", "晁", "勾", "敖", "融", "冷", "訾", "辛", "阚",
        "那", "简", "饶", "空", "曾", "毋", "沙", "乜", "养", "鞠",
        "须", "丰", "巢", "关", "蒯", "相", "查", "后", "荆", "红",
        "游", "竺", "权", "逮", "盍", "益", "桓", "公", "万俟",
        "司马", "上官", "欧阳", "夏侯", "诸葛", "闻人", "东方", "赫连",
        "皇甫", "宗政", "濮阳", "淳于", "太叔", "申屠", "公孙",
        "慕容", "仲孙", "钟离", "长孙", "宇文", "司徒", "鲜于",
        "司空", "闾丘", "子车", "亓官", "司寇", "巫马", "公西",
        "颛孙", "壤驷", "公良", "漆雕", "乐正", "宰父", "谷梁",
        "拓跋", "夹谷", "轩辕", "令狐", "段干", "百里", "呼延",
        "东郭", "南门", "羊舌", "微生", "公户", "公玉", "公仪",
        "梁丘", "公仲", "公上", "公门", "公山", "公坚", "左丘",
        "公伯", "西门", "公祖", "第五", "公乘", "贯丘", "公皙",
        "南荣", "东里", "东宫", "仲长", "子书", "子桑", "即墨",
        "达奚", "褚师", "吴铭", "欧阳", "太史", "端木", "上官",
        "司马", "东方", "独孤", "南宫", "万俟", "闻人", "夏侯",
        "诸葛", "尉迟", "公羊", "澹台", "公冶", "宗政", "濮阳",
        "公冶", "太叔", "申屠", "公孙", "慕容", "仲孙", "钟离",
        "长孙", "宇文", "司徒", "鲜于", "司空", "闾丘", "子车",
        "亓官", "司寇", "巫马", "公西", "颛孙", "壤驷", "公良",
        "漆雕", "乐正", "宰父", "谷梁", "拓跋", "夹谷", "轩辕",
        "令狐", "段干", "百里", "呼延", "东郭", "南门", "羊舌",
        "微生", "公户", "公玉", "公仪", "梁丘", "公仲", "公上",
        "公门", "公山", "公坚", "左丘", "公伯", "西门", "公祖",
        "第五", "公乘", "贯丘", "公皙", "南荣", "东里", "东宫",
        "仲长", "子书", "子桑", "即墨", "达奚", "褚师", "吴铭"
    ]

    # create table
    db.create("CREATE TABLE IF NOT EXISTS surname (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, len INTEGER NOT NULL);")
    dbSurName = db.search("SELECT name FROM surname;")
    for name in bai_jia_xing:
        if name not in dbSurName:
            db.insert(f'INSERT INTO surname (name, len) VALUES (\"{name}\", \"{len(name)}\");')

# 中文 名
if 0:
    db.create("CREATE TABLE IF NOT EXISTS firstnamecn (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, sex INTEGER NOT NULL, len INTEGER NOT NULL);")
    url_firstname_cn = "https://www.qqxiuzi.cn/zh/xingming/show.php"
    header = {
        "Cookie": "",
        "Host": "www.qqxiuzi.cn",
        "Origin": "https://www.qqxiuzi.cn",
        "Referer": "https://www.qqxiuzi.cn/zh/xingming/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    data = {
        "fenlei": "buxian",  # buxian, changjian, xiyou 姓的稀有程度
        "xing": "1",  # 1, 2 姓长度，不重要
        "text": "赵 钱 欧阳 芈 夏",  # 固定参数
        "xb": "",  # nan, nv 性别
        "ming": "",  # 1, 2 名字长度
        "num": "",  # 数量 MAX: 2000
        "token": ""  # token
    }

    def setRequestParam(cookie: str, token: str):
        header["Cookie"] = "PHPSESSID=" + cookie
        data["token"] = token

    def setData(xb: str, ming: str, num: int = 2000) -> dict:
        data["xb"] = xb
        data["ming"] = ming
        data["num"] = str(num)
        return data

    setRequestParam("75ro9ipi1t0vif4365tsko3o46", "a451649c242b308b01ea7e1bd0a2dc41")
    r = requests.post(url=url_firstname_cn, headers=header, data=setData("nv", "2"))
    # 分别用:   "nan", "1"
    #           "nv", "1"
    #           "nan", "2"
    #           "nv", "2"
    # 作为参数

    b = BeautifulSoup(r.content, "lxml")
    # print(b)
    names = b.find_all("div")
    sex = 1 if data["xb"] == "nan" else 0
    name_list = db.search("SELECT name FROM firstnamecn;")
    for name in names:
        name = name.text[1:]
        if name not in name_list:
            name_list.append(name)
            db.insert(f"INSERT INTO firstnamecn (name, sex, len) VALUES (\"{name}\", \"{sex}\", \"{data['ming']}\");")

# 英文 姓
if 0:
    db.create("CREATE TABLE IF NOT EXISTS lastname (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);")

# 英文 名
if 0:
    db.create("CREATE TABLE IF NOT EXISTS firstnameen (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, sex INTEGER NOT NULL);")

