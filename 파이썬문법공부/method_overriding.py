#메소드 오버라이딩

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class MailSender:
    def send(self):
        print('메일 발송')

class TravelBlackBox(BlackBox, VideoMaker, MailSender): #다중상속
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd

    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')

#자식 클래스에서 같은 메소드를 새로 정의하지 않으면? 부모 클래스의 메소드를,
#자식 클래스에서 같은 메소드를 새로 정의하면? 자식 클래스의 메소드를 쓰게 됩니다!
        
class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')
        self.make()
        self.send()

    def use_pass(self):
        pass # use_pass 메소드를 호출해도 에러 발생 X

b1 = TravelBlackBox('하양이', 100000, 64)
b1.set_travel_mode(20)
# 실행결과 : 20분 동안 여행 모드 ON

b2 = AdvancedTravelBlackBox('초록이', 120000, 64)
b2.set_travel_mode(15)
# 실행결과 : 
# 15분 동안 여행 모드 ON
# 추억용 여행 영상 제작
# 메일 발송
