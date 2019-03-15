#coding=utf-8

def main():

        choose = input("请输入您的选择:")
        if choose == '1' :
            file_url1 = input('请输入第一个需要去重文件名:')
            file_url2 = input('请输入第二个需要去重文件名:')
            file_url3 = input('请输入去重过后的文件名:')

            file = open(file_url1+'.txt',"r",encoding="utf-8",errors="ignore")
            t1 = set()

            while True:
                mystr = file.readline()  # 表示一次读取一行
                mystr = mystr.strip('\n')

                if not mystr:
                #读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
                    break

                t1.add(mystr)
            file.close()

            file1 = open(file_url2+'.txt',"r",encoding="utf-8",errors="ignore")
            while True:

                yourstr = file1.readline()  # 表示一次读取一行
                yourstr = yourstr.strip('\n')

                if not yourstr:
                #读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
                    break
                t1.add(yourstr)
            # print(t1)
            file1.close()

            file2 = open(file_url3+'.txt',"a+",encoding="utf-8",errors="ignore")
            # global list
            list1 = list(t1)            #集合转列表，对列表的值递归写入
            for i in range(len(list1)):
                print(list1[i])
                file2.write(list1[i]+'\n')
            file2.close()

        elif choose == '2' :
            file_url4 = input('请输入第一个文件名(已经用sqlmap跑过的):')
            file_url5 = input('请输入第二个需要文件名(需要减去的):')
            file_url6 = input('请输入减去过后的文件名:')

            file = open(file_url4+'.txt', "r", encoding="utf-8-sig", errors="ignore")
            t1 = set()
            t2 = set()

            while True:
                mystr = file.readline()  # 表示一次读取一行
                mystr = mystr.strip('\n')

                if not mystr:
                    # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
                    break

                t1.add(mystr)
            print(t1)
            file.close()

            file1 = open(file_url5+'.txt', "r", encoding="utf-8-sig", errors="ignore")
            while True:

                yourstr = file1.readline()  # 表示一次读取一行
                yourstr = yourstr.strip('\n')

                if not yourstr:
                    # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
                    break
                t2.add(yourstr)
            print(t2)
            file1.close()

            file2 = open(file_url6+'.txt', "a+", encoding="utf-8-sig", errors="ignore")

            t3 = t2 - t1
            list1 = list(t3)  # 集合转列表，对列表的值递归写入
            for i in range(len(list1)):
                file2.write(list1[i] + '\n')
            file2.close()

        elif choose == '3' :
            file_url7 = input("请输入需要排序的文件名:")
            file_url8 = input("请输入排序过后的文件名:")
            list1 = []
            with open(file_url7+'.txt', 'r') as f:
                for line in f:
                    list1.append(line.strip())

            with open(file_url8+'.txt', "w") as f:
                for item in sorted(list1):
                    f.writelines(item)
                    f.writelines('\n')

        elif choose == '4' :
            file_urlz = input('请输入需要删除同变量的url文件名:')
            file_urld = input('请输入处理后的文件名:')

            file = open(file_urlz+'.txt', "r", encoding="utf-8", errors="ignore")
            my_strb = ''

            while True:
                if my_strb == '':
                    my_stra = file.readline()  # 表示一次读取一行
                    my_stra = my_stra.strip('\n')
                else:
                    my_stra = my_strb

                my_strb = file.readline()
                my_strb = my_strb.strip('\n')

                while True:
                    a = my_stra.split('=')
                    b = my_strb.split('=')

                    if len(a) >= 2:
                        x = 0
                        for x in range(1, len(a) - 1):
                            a[x] = a[x - 1] + '=' + a[x]
                        a = a[x]

                    if len(b) >= 2:
                        y = 0
                        for y in range(1, len(b) - 1):
                            b[y] = b[y - 1] + '=' + b[y]
                        b = b[y]

                    if type(a) is list:
                        print('aok')
                    else:
                        a = a.split()

                    if type(b) is list:
                        print('bok')
                    else:
                        b = b.split()

                    if a == b:
                        my_strb = file.readline()
                        my_strb = my_strb.strip('\n')
                        continue
                    else:
                        break

                with open(file_urld+'.txt', "a+", encoding="utf-8") as f:
                    f.write(my_stra + '\n')
                    f.close()

                if not my_strb:
                    # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
                    break

            file.close()

        elif choose == '5' :
            variable = input('请输入要删除的字段：')
            file_urla = input('请输入需要删除某字段url的文件名:')
            file_urlb = input('请输入处理后的文件名:')

            file = open(file_urla+'.txt' , "r", encoding="utf-8", errors="ignore")
            while True:
                mystr = file.readline()  # 表示一次读取一行
                mystr = mystr.strip('\n')

                if not mystr:
                    # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
                    break

                if variable in mystr:
                    print("有variable")
                    continue
                else:
                    file2 = open(file_urlb+'.txt' , "a+", encoding="utf-8", errors="ignore")
                    file2.write(mystr + '\n')
                    file2.close()
            file.close()

        elif choose == '6':
            file_urlx = input('请输入需要保留主域名的文件:')
            file_urly = input('请输入处理后的文件名:')

            file = open(file_urlx+'.txt' , "r", encoding="utf-8", errors="ignore")
            while True:
                mystr = file.readline()  # 表示一次读取一行
                mystr = mystr.strip('\n')

                if not mystr:
                    # 读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
                    break

                url_index_tmp = mystr.split('/')
                url_index = url_index_tmp[0] + '//' + url_index_tmp[2]
                print(url_index)
                file2 = open(file_urly+'.txt', "a+", encoding="utf-8", errors="ignore")
                file2.write(url_index + '\n')
                file2.close()
            file.close()

        elif choose == '7':
            exit()

if __name__ == '__main__':

    while True:
        print('1、合并A、B两个文件并删除重复项\n2、从B中删除A存在的URL\n3、对单个文件URL进行排序\n4、删除单个文件变量赋值=前相同'
              '字段的url(需要进行排序操作)\n5、删除存在某个字段的url(譬如gov)\n6、URL只保留主域名\n7、exit(生成文件需要进行exit)')
        main()