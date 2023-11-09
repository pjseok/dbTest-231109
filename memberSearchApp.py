import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import pymysql

form_class = uic.loadUiType("ui/memberui.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원조회 프로그램")

        self.search_btn.clicked.connect(self.de_search) # 조회 버튼 클릭시 db_search 함수 호출
        self.modify_btn.clicked.connect(self.db_modify) # 조회 버튼 클릭시 db_modify 함수 호출
        self.reset_btn.clicked.connect(self.reset) # 조회 버튼 클릭시 reset 함수 호출
    def de_search(self):
        memberid = self.memberid_edit.text() # 회원아이디로 입력된 텍스트 가져오기

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM member WHERE memberid = '{memberid}'"

        cur = conn.cursor() # 커서 생성
        cur.execute(sql) # SQL문 실행

        result = cur.fetchone()

        cur.close()
        conn.close()

        # print(result)
        # memberInfo1 = result[1]
        # memberInfo2 = result[2]
        # memberInfo3 = result[3]
        # memberInfo4 = result[4]
        # memberInfo5 = result[5]
        if result != None:
            self.password_edit.setText(result[1])
            self.name_edit.setText(result[2])
            self.phone_edit.setText(result[3])
            self.adress_edit.setText(result[4])
            self.age_edit.setText(str(result[5]))
            # age(result[5])가 정수이므로 문자열로 변환
        else:
            self.password_edit.setText('회원정보없음')
            self.name_edit.setText('회원정보없음')
            self.phone_edit.setText('회원정보없음')
            self.adress_edit.setText('회원정보없음')
            self.age_edit.setText('회원정보없음')


    def db_modify(self):
        memberid = self.memberid_edit.text()  # 회원아이디로 입력된 텍스트 가져오기
        memberpw = self.password_edit.text()   # 회원비밀번호 입력된 텍스트 가져오기
        name = self.name_edit.text()  # 회원이름 텍스트 가져오기
        phone = self.phone_edit.text() # 회원전화번호 입력된 텍스트 가져오기
        adress = self.adress_edit.text() # 회원주소 텍스트 가져오기
        age = self.age_edit.text() # 회원나이 텍스트 가져오기

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"UPDATE member SET memberpw = '{memberpw}', name='{name}', phone='{phone}', address ='{adress}', age='{age}' WHERE memberid = '{memberid}'"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        cur.close()
        conn.commit()
        conn.close()

        self.de_search() # 다시 데이터 갱신

    def reset(self):
        self.memberid_edit.clear()
        self.password_edit.clear()
        self.name_edit.clear()
        self.phone_edit.clear()
        self.adress_edit.clear()
        self.age_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())