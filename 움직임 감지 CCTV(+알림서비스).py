#
#   opencv python 코딩
#   움직임이 있을때만 영상을 캡쳐(1초)
#   움직임이 있을시 영상녹화(5초)
#

import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os
from tkinter import *

def get_diff_img(frame_a, frame_b, frame_c, threshold):         # 쉽게 말해서 프레임이 바뀌면 차이가 있구나 그리고 얼마정도 차이가 있구나를
    # 3 프레임의 영상을 모두 흑백으로 전환 -- 흑백은 처리시간이 3분의1이므로 흑백으로 바꾼것(RGB색)         # 출력해주는 거임
    frame_a_gray = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    frame_b_gray = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    frame_c_gray = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

    # 1,2 프레임, 2,3 프레임 영상들의 차를 구함
    diff_ab = cv2.absdiff(frame_a_gray, frame_b_gray)
    diff_bc = cv2.absdiff(frame_b_gray, frame_c_gray)

    # 영상들의 차가 threshold 이상이면 값을 255(백색)으로 만들어줌
    ret, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)
    ret, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)

    # 두 영상 차의 공통된 부분을 1로 만들어줌
    diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)
    # 영상에서 1이 된 부분을 적당히 확장해줌(morpholgy)
    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

    # 영상에서 1인 부분의 갯수를 셈
    diff_cnt = cv2.countNonZero(diff)
    return diff, diff_cnt
    

# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')    # 영상을 기록할 코덱 설정
font = ImageFont.truetype('fonts/SCDream6.otf', 20) # 글꼴파일을 불러옴
is_record = False                           # 녹화상태는 처음엔 거짓으로 설정
on_record = False

threshold = 40      # 영상 차이에 사용할 threshold 설정
diff_max = 10       # 영상 차이 픽셀의 개수(이것 이상이면 움직임이 있다고 결정)
cnt_record = 0      # 영상 녹화 시간 관련 변수
max_cnt_record = 5  # 최소 촬영시간

# 초기 프레임으로 사용할 프레임들을 저장
ret, frame_a = capture.read()
ret, frame_b = capture.read()
# 무한루프
while True:
    # 현재시각을 불러와 문자열로저장
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    nowDatetime_path = now.strftime('%Y-%m-%d %H_%M_%S') # 파일이름으로는 :를 못쓰기 때문에 따로 만들어줌

    # 현재 영상을 입력받아 움직임 감지
    ret, frame_c = capture.read()
    diff, diff_cnt = get_diff_img(frame_a=frame_a, frame_b=frame_b, frame_c=frame_c, threshold=threshold)
    
    # 움직임이 일정 이상일시
from pyfcm import FCMNotification


APIKEY = AIzaSyCXFGa4f_FQqDdbFcf8-Z55Vo26PEIiu0Y
TOKEN = "YOUR_TOKEN"

# 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 준다
push_service = FCMNotification(APIKEY)

def sendMessage(body, title) :
    # 토큰값을 이용해 1명에게 푸시알림을 전송함
    result = push_service.notify_single_device(registration_id = TOKEN, message_title = title, message_body = body, data_message = data_message)

    # 전송 결과 출력
    print(result)

    if diff_cnt > diff_max:
        sendMessage("CCTV", "움직임이 감지되었습니다")
    
    # 움직임이 일정 이상이면(화면 캡쳐)
        cv2.imwrite("capture/capture" + nowDatetime_path + ".png", frame)  # 파일이름(한글안됨), 이미지

    # 움직임이 일정 이상이면(영상 녹화)
        is_record = True    # 녹화 준비
        if on_record == False:
            video = cv2.VideoWriter("움직임이 감지됨 " + nowDatetime_path + ".avi", fourcc, 1, (frame_c.shape[1], frame_c.shape[0]))
        cnt_record = max_cnt_record
    if is_record == True:   # 녹화중이면
        print('녹화 중')
        video.write(frame_c)    # 현재 프레임 저장
        cnt_record -= 1     # 녹화시간 1 감소
        on_record = True    # 녹화중 여부를 참으로
    if cnt_record == 0:     # 녹화시간이 다 되면
        is_record = False   # 녹화관련 변수들을 거짓으로
        on_record = False

    # 영상 차이를 출력(실제 사용시는 꺼도 됨)
    cv2.imshow("diff", diff)
    frame = np.array(frame_c)

    # 글자가 잘보이도록 배경을 넣어줌
    # img는 사각형을 넣을 이미지, pt1, pt2는 사각형의 시작점과 끝점, color는 색상(파랑,초록,빨강), tickness는 선굵기(-1은 내부를 채우는 것)
    cv2.rectangle(img=frame, pt1=(10, 15), pt2=(340, 35), color=(0,0,0), thickness=-1)     
    
    # 아래의 4줄은 글자를 영상에 더해주는 역할을 함    
    frame = Image.fromarray(frame)    
    draw = ImageDraw.Draw(frame)    
    # xy는 텍스트 시작위치, text는 출력할 문자열, font는 글꼴, fill은 글자색(파랑,초록,빨강)   
    draw.text(xy=(10, 15),  text="현재시간 : "+nowDatetime, font=font, fill=(255, 255, 255))
    frame = np.array(frame)
    frame_a = np.array(frame_b)
    frame_b = np.array(frame_c)

    key = cv2.waitKey(1000)   # 30ms 동안 키입력 대기    (CCTV이므로 초당 한번씩 인식)
    if key == ord('q'):  # 키보드의 q 를 누르면 무한루프가 멈춤
            break
    cv2.imshow("original", frame)   # 현재 시간을 표시하는 글자를 써준 영상 출력
    
capture.release()                   # 캡처 객체를 없애줌
cv2.destroyAllWindows()             # 모든 영상 창을 닫아줌
