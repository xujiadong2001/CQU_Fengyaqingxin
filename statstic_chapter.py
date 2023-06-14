import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# 依次读取imgs文件夹下的图片
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
ocr = PaddleOCR(use_angle_cls=True, lang="ch",det_db_box_thresh=0.3,det_db_thresh=0.2 ,cls_model_dir='C:\\Users\\xujiadong/.paddleocr/whl\\cls\\ch_ppocr_sever_v2.0_cls_infer') # need to run only once to download and load model into memory
import csv
chapters_dic={'封面':[0,1],'序幕':[2,5],'第一章':[6,26],'第二章':[27,58],'第三章':[59,86],'第四章':[87,120],'第五章':[121,151],'第六章':[152,183],'第七章':[184,210],'第八章':[211,237],'书后':[238,239]}

for chapter in chapters_dic:
    dic = {}
    for page in range(chapters_dic[chapter][0],chapters_dic[chapter][1]+1):
        img_path="imgs/images_"+str(page)+".png"
        result = ocr.ocr(img_path, cls=True)
        txts = [detection[1][0] for line in result for detection in line]
        for txt in txts:
            for word_ids in range(len(txt)):
                if txt[word_ids] in dic:
                    dic[txt[word_ids]]+=1
                else:
                    dic[txt[word_ids]]=1

    with open(chapter+'_word_count.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['word', 'count'])
        for key in dic:
            writer.writerow([key, dic[key]])
'''
for img in imgs_list:
    img_path="imgs/"+img
    result = ocr.ocr(img_path, cls=True)
    txts = [detection[1][0] for line in result for detection in line]
    for txt in txts:
        for word_ids in range(len(txt)):
            if txt[word_ids] in dic:
                dic[txt[word_ids]]+=1
            else:
                dic[txt[word_ids]]=1
print(dic)
# 将字典保存为csv文件
import csv
with open('word_count.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['word','count'])
    for key in dic:
        writer.writerow([key,dic[key]])
'''