import random
import time

print("자 오늘은 무엇을 먹어볼까나?? 피... 피카츄!!")
boblst=['서문 아만도','서문 브리또','서문 쌀국수','한울샘','솟을샘 브리또', \
        '솟을샘 만두','솟을샘 김밥','솟을샘 샌드위치','공순이','학관 아마뜨리치아나',\
        '꼬숑','싸움의 고수','타코벨','홍콩반점','맥날','순대국','버거킹','신촌수제비','달려라팬']
a = random.randint(0,len(boblst))
for i in range(4):
    print("두구두구  "+"%d"%(4-i))
    time.sleep(1)
print ("맛있는 ["+format(boblst[a])+"] 이로구나!!")
