#encoding=utf-8
import sys
sys.path.append('../')
import jieba
import jieba.analyse
import chardet
jieba.load_userdict("C:\Users\dell\Desktop\\1212.txt")
import MySQLdb


def fun1():
    f = open("1234.txt")
    line = f.readline()
    d = {'a': 1}
    while line:
        s = line.split(' ')
        d[s[0]] = s[1][:-1]
        line = f.readline()
    f.close()

    f = open("123.txt")
    line = f.readline()
    line=line.decode('utf8')
    color=''
    name=''
    style=''
    season=''
    use=''
    u= open('use.txt', 'r').read().split(' ')
    s= open('style.txt', 'r').read().split(' ')
    n= open('name.txt', 'r').read().split(' ')
    c= open('color.txt', 'r').read().split(' ')
    se= open('season.txt', 'r').read().split(' ')
    while line:
        seg_list = jieba.cut(line, cut_all=False)

        for word in seg_list:
            if word.encode('utf8') in u:
                use=use+d[word.encode('utf8')]
                print d[word.encode('utf8')]
            if word.encode('utf8') in s:
                style=style+d[word.encode('utf8')]
                print d[word.encode('utf8')]
        line = f.readline()

    f.close()
    print "end"
    print use
    print style
def fun2(c):
    conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', port=3306,db='imix',charset="utf8")
    cur = conn.cursor()
    print cur
    c=c.decode('utf8')
    seg_list = jieba.cut(c, cut_all=False)

    u = open('use.txt', 'r').read().split(' ')
    s = open('style.txt', 'r').read().split(' ')
    n = open('name.txt', 'r').read().split(' ')
    c = open('color.txt', 'r').read().split(' ')
    se = open('season.txt', 'r').read().split(' ')
    color = ''
    name = ''
    style = ''
    season = ''
    use = ''

    seg=list(seg_list)

    for word in seg:#word is unicode

        if word.encode('utf8') in u:

            use = use + word.encode('utf8')
        if word.encode('utf8') in s:
            style = style + word.encode('utf8')
        if word.encode('utf8') in n:
            name += word.encode('utf8')
        if word.encode('utf8') in c:
            color+=word.encode('utf8')
        if word.encode('utf8') in se:
            season+=word.encode('utf8')
    
    cur.execute("INSERT INTO item(color,name,season,uuse,style) values(%s,%s,%s,%s,%s)",([color], [name], [season], [use], [style]))

    #[color], [name], [season], [use], [style]
    conn.commit()
    cur.close()
    conn.close()