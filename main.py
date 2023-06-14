import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from paddleocr import PaddleOCR, draw_ocr
# Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
# 参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
ocr = PaddleOCR(use_angle_cls=True, lang="ch",det_db_box_thresh=0.3,det_db_thresh=0.2 ,cls_model_dir='C:\\Users\\xujiadong/.paddleocr/whl\\cls\\ch_ppocr_sever_v2.0_cls_infer') # need to run only once to download and load model into memory
img_path = 'test.png'
# 对图像进行二值化
from PIL import Image
#img = Image.open(img_path).convert('L')
#img = img.point(lambda x: 255 if x > 180 else 0)

# img.save('test_prod.png')
# img_path = 'test_prod.png'
# 进行识别
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)

# 显示结果

image = Image.open(img_path).convert('RGB')
boxes = [detection[0] for line in result for detection in line] # Nested loop added
print(boxes)
txts = [detection[1][0] for line in result for detection in line] # Nested loop added
print(txts)
scores = [detection[1][1] for line in result for detection in line] # Nested loop added
im_show = draw_ocr(image, boxes, txts, scores)
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')

# 词云、前十个高频词（不同章节堆叠图）、每个章节的字数比例（饼图）、tfidf、树图（显示层次结构）、关键词（用jieba）、
# 页码、输入字数检测、时钟、文件系统、模型阈值

