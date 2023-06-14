//将csv转为JSON
function CSVTOJSON(csv) {
    let lines = csv.split("\n");
    let result = [];
    let headers = lines[0].split(",");

    for (let i = 1; i < lines.length; i++) {
        let obj = {};
        let currentline = lines[i].split(",");
        for (let j = 0; j < headers.length; j++) {
            obj[headers[j].trim()] = currentline[j];
        }
        result.push(obj);
    }
    return result;
}

//读取饼图数据
function getData1() {
    //要读取的文件名
    let CSVFileName = [
        "总",
        "序幕",
        "封面",
        "书后",
        "第一章",
        "第二章",
        "第三章",
        "第四章",
        "第五章",
        "第六章",
        "第七章",
        "第八章",
    ];
    let res = [];
    let count = 0;
    //遍历读取所有文件
    for (let i = 0; i < CSVFileName.length; i++) {
        $.get("./data/" + CSVFileName[i] + "_word_count.csv", function (data) {
            let list = CSVTOJSON(data);
            //统计每章字数
            count = 0;
            for (let j = 0; j < list.length; j++) {
                if (list[j].count != "" && typeof list[j].count != "undefined") {
                    count += parseInt(list[j].count.replace("\r", ""));
                }
            }
            res.push({name: CSVFileName[i], value: count});
        });
    }
    console.log(res);
}

var data1 = [
    {name: "封面", value: 25},
    {name: "书后", value: 134},
    {name: "序幕", value: 800},
    {name: "第二章", value: 8701},
    {name: "第一章", value: 5247},
    {name: "第三章", value: 6885},
    {name: "第六章", value: 10145},
    {name: "第五章", value: 7964},
    {name: "第七章", value: 9137},
    {name: "第四章", value: 9573},
    {name: "第八章", value: 5382},
];
var data2_X = ["之", "不", "也", "日", "而", "其", "以", "者", "子", "人"];
var data2_Y = [
    [177, 106, 158, 155, 79, 144, 65, 74, 45, 35],
    [359, 232, 232, 249, 173, 213, 157, 145, 129, 124],
    [285, 182, 174, 116, 135, 135, 112, 116, 55, 82],
    [451, 299, 225, 181, 251, 154, 141, 123, 146, 104],
    [346, 255, 170, 238, 213, 150, 103, 111, 119, 102],
    [461, 265, 284, 253, 188, 219, 145, 177, 91, 147],
    [324, 230, 217, 206, 196, 220, 213, 138, 121, 103],
    [276, 136, 106, 102, 108, 77, 89, 84, 130, 86],
];
var data3 = [{'name': '销', 'value': 41}, {'name': '字', 'value': 41}, {'name': '顺', 'value': 41}, {
    'name': '英',
    'value': 41
}, {'name': '随', 'value': 41}, {'name': '将', 'value': 42}, {'name': '敢', 'value': 42}, {
    'name': '口',
    'value': 42
}, {'name': '调', 'value': 42}, {'name': '斯', 'value': 42}, {'name': '取', 'value': 42}, {
    'name': '市',
    'value': 43
}, {'name': '士', 'value': 43}, {'name': '立', 'value': 43}, {'name': '伯', 'value': 43}, {
    'name': '被',
    'value': 43
}, {'name': '土', 'value': 44}, {'name': '交', 'value': 44}, {'name': '避', 'value': 44}, {
    'name': '守',
    'value': 44
}, {'name': '入', 'value': 44}, {'name': '汝', 'value': 44}, {'name': '己', 'value': 45}, {
    'name': '告',
    'value': 45
}, {'name': '容', 'value': 46}, {'name': '女', 'value': 46}, {'name': '于', 'value': 46}, {
    'name': '將',
    'value': 46
}, {'name': '服', 'value': 46}, {'name': '雨', 'value': 46}, {'name': '因', 'value': 46}, {
    'name': '富',
    'value': 46
}, {'name': '寓', 'value': 47}, {'name': '分', 'value': 47}, {'name': '游', 'value': 47}, {
    'name': '色',
    'value': 47
}, {'name': '酒', 'value': 47}, {'name': '月', 'value': 48}, {'name': '由', 'value': 48}, {
    'name': '草',
    'value': 48
}, {'name': '時', 'value': 48}, {'name': '仲', 'value': 48}, {'name': '尼', 'value': 48}, {
    'name': '武',
    'value': 49
}, {'name': '牛', 'value': 49}, {'name': '管', 'value': 49}, {'name': '父', 'value': 49}, {
    'name': '藏',
    'value': 50
}, {'name': '工', 'value': 50}, {'name': '推', 'value': 51}, {'name': '哉', 'value': 51}, {
    'name': '木',
    'value': 52
}, {'name': '列', 'value': 52}, {'name': '写', 'value': 53}, {'name': '忘', 'value': 53}, {
    'name': '臣',
    'value': 53
}, {'name': '信', 'value': 53}, {'name': '法', 'value': 53}, {'name': '光', 'value': 54}, {
    'name': '志',
    'value': 54
}, {'name': '则', 'value': 54}, {'name': '存', 'value': 54}, {'name': '氏', 'value': 54}, {
    'name': '开',
    'value': 55
}, {'name': '恶', 'value': 55}, {'name': '元', 'value': 56}, {'name': '固', 'value': 56}, {
    'name': '待',
    'value': 56
}, {'name': '和', 'value': 56}, {'name': '万', 'value': 56}, {'name': '徒', 'value': 56}, {
    'name': '海',
    'value': 57
}, {'name': '及', 'value': 57}, {'name': '往', 'value': 57}, {'name': '集', 'value': 59}, {
    'name': '見',
    'value': 59
}, {'name': '失', 'value': 59}, {'name': '九', 'value': 59}, {'name': '静', 'value': 60}, {
    'name': '兄',
    'value': 60
}, {'name': '爱', 'value': 60}, {'name': '受', 'value': 60}, {'name': '情', 'value': 61}, {
    'name': '仁',
    'value': 61
}, {'name': '又', 'value': 61}, {'name': '黄', 'value': 62}, {'name': '教', 'value': 62}, {
    'name': '易',
    'value': 62
}, {'name': '果', 'value': 62}, {'name': '理', 'value': 62}, {'name': '乃', 'value': 63}, {
    'name': '北',
    'value': 63
}, {'name': '常', 'value': 64}, {'name': '家', 'value': 64}, {'name': '雅', 'value': 64}, {
    'name': '高',
    'value': 64
}, {'name': '求', 'value': 64}, {'name': '国', 'value': 65}, {'name': '助', 'value': 66}, {
    'name': '好',
    'value': 66
}, {'name': '前', 'value': 66}, {'name': '止', 'value': 67}, {'name': '七', 'value': 67}, {
    'name': '耳',
    'value': 68
}, {'name': '帝', 'value': 68}, {'name': '俊', 'value': 68}, {'name': '安', 'value': 69}, {
    'name': '来',
    'value': 69
}, {'name': '六', 'value': 70}, {'name': '神', 'value': 70}, {'name': '樂', 'value': 71}, {
    'name': '全',
    'value': 72
}, {'name': '解', 'value': 72}, {'name': '年', 'value': 72}, {'name': '去', 'value': 73}, {
    'name': '聖',
    'value': 73
}, {'name': '孔', 'value': 74}, {'name': '且', 'value': 75}, {'name': '本', 'value': 75}, {
    'name': '彼',
    'value': 76
}, {'name': '必', 'value': 77}, {'name': '南', 'value': 77}, {'name': '利', 'value': 77}, {
    'name': '水',
    'value': 78
}, {'name': '合', 'value': 78}, {'name': '象', 'value': 78}, {'name': '善', 'value': 79}, {
    'name': '意',
    'value': 80
}, {'name': '命', 'value': 80}, {'name': '百', 'value': 81}, {'name': '篇', 'value': 82}, {
    'name': '性',
    'value': 82
}, {'name': '惠', 'value': 82}, {'name': '矣', 'value': 83}, {'name': '云', 'value': 83}, {
    'name': '欲',
    'value': 84
}, {'name': '山', 'value': 85}, {'name': '作', 'value': 85}, {'name': '雕', 'value': 85}, {
    'name': '馬',
    'value': 85
}, {'name': '郭', 'value': 85}, {'name': '正', 'value': 86}, {'name': '司', 'value': 86}, {
    'name': '内',
    'value': 86
}, {'name': '二', 'value': 87}, {'name': '多', 'value': 88}, {'name': '注', 'value': 88}, {
    'name': '通',
    'value': 89
}, {'name': '虚', 'value': 91}, {'name': '音', 'value': 92}, {'name': '见', 'value': 93}, {
    'name': '就',
    'value': 95
}, {'name': '今', 'value': 95}, {'name': '治', 'value': 96}, {'name': '莫', 'value': 96}, {
    'name': '美',
    'value': 96
}, {'name': '具', 'value': 96}, {'name': '莊', 'value': 98}, {'name': '如', 'value': 99}, {
    'name': '精',
    'value': 99
}, {'name': '居', 'value': 102}, {'name': '先', 'value': 102}, {'name': '亦', 'value': 102}, {
    'name': '三',
    'value': 108
}, {'name': '放', 'value': 109}, {'name': '化', 'value': 109}, {'name': '食', 'value': 109}, {
    'name': '事',
    'value': 110
}, {'name': '真', 'value': 115}, {'name': '五', 'value': 116}, {'name': '四', 'value': 116}, {
    'name': '公',
    'value': 116
}, {'name': '古', 'value': 117}, {'name': '在', 'value': 119}, {'name': '小', 'value': 120}, {
    'name': '老',
    'value': 120
}, {'name': '弟', 'value': 121}, {'name': '民', 'value': 122}, {'name': '方', 'value': 123}, {
    'name': '外',
    'value': 123
}, {'name': '昶', 'value': 123}, {'name': '身', 'value': 128}, {'name': '皆', 'value': 131}, {
    'name': '邪',
    'value': 133
}, {'name': '十', 'value': 135}, {'name': '使', 'value': 136}, {'name': '反', 'value': 140}, {
    'name': '未',
    'value': 145
}, {'name': '八', 'value': 149}, {'name': '始', 'value': 151}, {'name': '出', 'value': 151}, {
    'name': '足',
    'value': 152
}, {'name': '死', 'value': 154}, {'name': '君', 'value': 158}, {'name': '文', 'value': 160}, {
    'name': '上',
    'value': 161
}, {'name': '成', 'value': 167}, {'name': '期', 'value': 169}, {'name': '名', 'value': 171}, {
    'name': '一',
    'value': 174
}, {'name': '用', 'value': 177}, {'name': '中', 'value': 179}, {'name': '同', 'value': 179}, {
    'name': '相',
    'value': 184
}, {'name': '我', 'value': 185}, {'name': '形', 'value': 192}, {'name': '周', 'value': 193}, {
    'name': '已',
    'value': 193
}, {'name': '行', 'value': 195}, {'name': '王', 'value': 197}, {'name': '笑', 'value': 200}, {
    'name': '典',
    'value': 202
}, {'name': '明', 'value': 207}, {'name': '面', 'value': 210}, {'name': '何', 'value': 211}, {
    'name': '爲',
    'value': 214
}, {'name': '案', 'value': 215}, {'name': '禽', 'value': 236}, {'name': '德', 'value': 240}, {
    'name': '世',
    'value': 240
}, {'name': '至', 'value': 241}, {'name': '地', 'value': 243}, {'name': '非', 'value': 253}, {
    'name': '平',
    'value': 260
}, {'name': '言', 'value': 264}, {'name': '心', 'value': 274}, {'name': '若', 'value': 275}, {
    'name': '吾',
    'value': 292
}, {'name': '得', 'value': 293}, {'name': '自', 'value': 295}, {'name': '能', 'value': 302}, {
    'name': '下',
    'value': 309
}, {'name': '可', 'value': 310}, {'name': '此', 'value': 317}, {'name': '夫', 'value': 345}, {
    'name': '生',
    'value': 349
}, {'name': '物', 'value': 351}, {'name': '然', 'value': 354}, {'name': '乎', 'value': 395}, {
    'name': '是',
    'value': 404
}, {'name': '於', 'value': 413}, {'name': '大', 'value': 440}, {'name': '道', 'value': 453}, {
    'name': '故',
    'value': 515
}, {'name': '知', 'value': 560}, {'name': '所', 'value': 565}, {'name': '無', 'value': 664}, {
    'name': '天',
    'value': 715
}, {'name': '有', 'value': 760}, {'name': '人', 'value': 789}, {'name': '子', 'value': 847}, {
    'name': '者',
    'value': 976
}, {'name': '以', 'value': 1036}, {'name': '其', 'value': 1338}, {'name': '而', 'value': 1347}, {
    'name': '日',
    'value': 1503
}, {'name': '也', 'value': 1571}, {'name': '不', 'value': 1715}, {'name': '之', 'value': 2711}];
