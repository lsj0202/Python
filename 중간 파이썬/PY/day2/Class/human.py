class human:
    def __init__(self , height, age):
        self.height = height #멤버 변수
        self.age = age

    def how_old(self):
        print(self.age, "살입니다.")

    def how_tall(self):
        print(self.height,"cm 입니다.")

sunah = human(166, 29) #인스턴스 생성
eunwoo =human(185, 29) #인스턴스 생성

sunah.how_old()
# human.how_old(sunah)
