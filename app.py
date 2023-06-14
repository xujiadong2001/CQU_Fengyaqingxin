import sys,time
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QTimer,QUrl
import PyQt5.QtWebEngineWidgets
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from paddleocr import PaddleOCR, draw_ocr
import cv2
# ocr = PaddleOCR(use_angle_cls=True, lang="ch",cls_model_dir='C:\\Users\\xujiadong/.paddleocr/whl\\cls\\ch_ppocr_sever_v2.0_cls_infer') # need to run only once to download and load model into memory

# 动态载入
class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # PyQt5
        self.ui=uic.loadUi("main.ui")
        self.pagenumber=0
        pic_path="imgs/images_"+str(self.pagenumber)+".png"
        self.detect_result=None
        self.page_num=self.get_pages_num()
        self.set_page_number()
        self.det_db_box_thresh=0.1
        self.det_db_thresh=0.2
        self.ui.horizontalSlider.setValue(self.det_db_box_thresh*100)
        self.ui.horizontalSlider_2.setValue(self.det_db_thresh*100)
        self.ui.label_9.setText(str(self.ui.horizontalSlider.value()/100))
        self.ui.label_10.setText(str(self.ui.horizontalSlider_2.value()/100))
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.pushButton.clicked.connect(self.set0)
        self.ui.pushButton_2.clicked.connect(self.set1)
        self.ui.graphicsView.setStyleSheet("border-image:url("+pic_path+")")
        self.ui.pushButton_3.clicked.connect(self.search)
        self.ui.pushButton_4.clicked.connect(self.page_backward)
        self.ui.pushButton_5.clicked.connect(self.page_forward)
        self.ui.pushButton_6.clicked.connect(self.trans_pages)
        self.ui.horizontalSlider.valueChanged.connect(self.set_det_db_box_thresh)
        self.ui.horizontalSlider_2.valueChanged.connect(self.set_det_db_thresh)
        self.ui.treeWidget.itemClicked.connect(self.show_item)
        self.ui.chart3.load(QUrl.fromLocalFile(os.path.abspath("charts/bar.html")))
        self.ui.chart2.load(QUrl.fromLocalFile(os.path.abspath("charts/pie.html")))
        self.ui.chart1.load(QUrl.fromLocalFile(os.path.abspath("charts/word.html")))
        timer= QTimer(self)
        timer.start()
        timer.timeout.connect(self.show_time)
        self.page_dict={'封面':[0,1],'序幕':[2,5],'第一章':[6,26],'第二章':[27,59],'第三章':[60,86],'第四章':[87,121],'第五章':[122,151],'第六章':[152,184],'第七章':[185,210],'第八章':[211,237],'书后':[238,239]}

        # 这里与静态载入不同，使用 self.ui.show()
        # 如果使用 self.show(),会产生一个空白的 MainWindow
        self.ui.show()

    def show_item(self):
        item=self.ui.treeWidget.currentItem()
        page=self.page_dict[item.text(0)][0]
        self.pagenumber=page
        self.set_page_number()
        pic_path="imgs/images_"+str(self.pagenumber)+".png"
        self.ui.graphicsView.setStyleSheet("border-image:url("+pic_path+")")

    def show_time(self):
        t=time.strftime("%H:%M:%S", time.localtime())
        self.ui.lcdNumber.display(t)
    def set_det_db_box_thresh(self):
        self.ui.label_9.setText(str(self.ui.horizontalSlider.value()/100))
        self.det_db_box_thresh=self.ui.horizontalSlider.value()/100
    def set_det_db_thresh(self):
        self.ui.label_10.setText(str(self.ui.horizontalSlider_2.value()/100))
        self.det_db_thresh=self.ui.horizontalSlider_2.value()/100
    def get_pages_num(self):
        # 查看imgs文件夹下有多少张图片
        imgs_list = os.listdir('imgs')
        return len(imgs_list)
    def set_page_number(self):
        self.ui.label_2.setText(str(self.pagenumber+1)+'/'+str(self.page_num))
    def set0(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def set1(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def page_forward(self):
        self.pagenumber+=1
        # 如果图片不存在，就不显示
        pic_path="imgs/images_"+str(self.pagenumber)+".png"
        if os.path.exists(pic_path):
            self.ui.graphicsView.setStyleSheet("border-image:url("+pic_path+")")
            self.detect_result = None
            self.set_page_number()
        else:
            self.pagenumber-=1
    def page_backward(self):
        self.pagenumber-=1
        # 如果图片不存在，就不显示
        pic_path="imgs/images_"+str(self.pagenumber)+".png"
        if os.path.exists(pic_path):
            self.ui.graphicsView.setStyleSheet("border-image:url("+pic_path+")")
            self.detect_result = None
            self.set_page_number()
        else:
            self.pagenumber+=1
    def search(self):
        word = self.ui.lineEdit.text()
        if len(word)>1:
            self.ui.label.setText('请输入单个字')
            return
        if self.detect_result==None:
            ocr = PaddleOCR(use_angle_cls=True, lang="ch", det_db_box_thresh=self.det_db_box_thresh, det_db_thresh=self.det_db_thresh,
                            cls_model_dir='C:\\Users\\xujiadong/.paddleocr/whl\\cls\\ch_ppocr_sever_v2.0_cls_infer')  # need to run only once to download and load model into memory

            pic_path = "imgs/images_" + str(self.pagenumber) + ".png"
            result = ocr.ocr(pic_path, cls=True)
            self.detect_result = []
            for line in result:
                for item in line:
                    coordinates = item[0]
                    text = item[1][0]
                    confidence = item[1][1]
                    self.detect_result.append({
                        'coordinates': coordinates,
                        'text': text,
                        'confidence': confidence
                    })
        result=[]
        origin=[]
        for item in self.detect_result:
            if word in item['text']:
                # 获取word在字符串中的位置
                index=item['text'].index(word)
                print(item['text'])
                print(item['coordinates'])
                print(index)
                length=len(item['text'])
                print(length)
                if length == 1:
                    result.append(item['coordinates'])
                    origin.append(item['coordinates'])
                else:
                    point0=item['coordinates'][0].copy()
                    point1=item['coordinates'][1].copy()
                    point2=item['coordinates'][2].copy()
                    point3=item['coordinates'][3].copy()
                    if point1[0]-point0[0]<point3[1]-point0[1]:
                        # 如果是竖着的字
                        point0[1]=point0[1]+index/length*(item['coordinates'][3][1]-item['coordinates'][0][1])
                        point1[1]=point1[1]+index/length*(item['coordinates'][2][1]-item['coordinates'][1][1])
                        point2[1]=point1[1]+(item['coordinates'][2][1]-item['coordinates'][1][1])/length
                        point3[1]=point0[1]+(item['coordinates'][3][1]-item['coordinates'][0][1])/length
                    else:
                        # 如果是横着的字
                        point0[0]=point0[0]+index/length*(item['coordinates'][1][0]-item['coordinates'][0][0])
                        point1[0]=point0[0]+(item['coordinates'][1]-item['coordinates'][0][0])/length
                        point3[0]=point3[0]+index/length*(item['coordinates'][2][0]-item['coordinates'][3][0])
                        point2[0] = point3[0] + (item['coordinates'][2][0] - item['coordinates'][3][0]) / length
                    result.append([point0,point1,point2,point3])
                    print([point0,point1,point2,point3])
                    origin.append(item['coordinates'])

        pic_path = "imgs/images_" + str(self.pagenumber) + ".png"
        # 通过opencv读取图片并绘制框
        img = cv2.imread(pic_path)
        for coordinate in result:
            cv2.rectangle(img, (int(coordinate[0][0]), int(coordinate[0][1])), (int(coordinate[2][0]), int(coordinate[2][1])+1), (0, 0, 255), 2)
        #for origin_coordinate in origin:
            #cv2.rectangle(img, (int(origin_coordinate[0][0]), int(origin_coordinate[0][1])), (int(origin_coordinate[2][0]), int(origin_coordinate[2][1])), (0, 255, 0), 2)
        save_path='imgs/temp.png'
        cv2.imwrite(save_path, img)
        self.ui.graphicsView.setStyleSheet("border-image:url("+save_path+")")
        if len(result)==0:
            self.ui.label.setText('未找到该汉字')
        else:
            self.ui.label.setText('找到'+str(len(result))+'个')

    def trans_pages(self):
        page=int(self.ui.lineEdit_2.text())-1 # 从0开始
        pic_path="imgs/images_"+str(page)+".png"
        if os.path.exists(pic_path):
            self.ui.graphicsView.setStyleSheet("border-image:url("+pic_path+")")
            self.detect_result = None
            self.pagenumber=page
            self.set_page_number()


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=mainwindow()
    sys.exit(app.exec_())