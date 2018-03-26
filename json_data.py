import json
from flask import Flask


app = Flask(__name__)


@app.route('/json_data', methods=['GET'])
def get_json_data():
    return json.dumps(
        {
            "_id": "5a9d1f6b837cfd803c8361b6",
            "house_id": "389783",
            "album": [
                [
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/0600006a119b08254af72b5b21a36570/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/c38ffe73178202ed564ca119c3d016e9/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/c176a0ef1e276232572f7321693259af/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/1e085c0146a11063490272d743ff756f/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/4245ca087751d447f9b4685a1e560f2c/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/dade55447fa93f5f8415bcc5a4158c88/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/d02d568420ea332d8832135bb50c74ed/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/2518bfa298a842b81a4024cef81a282b/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/0e7786adf115a01013229b32fbf645f6/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/b7ba034d8ce92ffc78844f459c4e5964/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "实景图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/17f5266529372e124c92dedefcd42bdf/860x10000.jpg",
                        "picture_description": "楼盘现场环境"
                    },
                    {
                        "picture_label": "效果图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/2fac25910f3d4a14258a8eb709067c12/860x10000.jpg",
                        "picture_description": "楼盘建筑物外景"
                    },
                    {
                        "picture_label": "规划图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/e53be70964f9956248bf695c413b7f9f/860x10000.jpg",
                        "picture_description": "规划沙盘"
                    },
                    {
                        "picture_label": "规划图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/73cac86af570ef7e1dc253f2ade2e431/860x10000.jpg",
                        "picture_description": "规划沙盘"
                    },
                    {
                        "picture_label": "规划图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/33bdadc8d07c53176387a1a13ef576c6/860x10000.jpg",
                        "picture_description": "规划沙盘"
                    },
                    {
                        "picture_label": "配套图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/aa215d810f6474c825024746941607ad/860x10000.jpg",
                        "picture_description": "项目紧邻公园，环境非常好，一些老人在这里散步。"
                    },
                    {
                        "picture_label": "配套图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/bdee6345dcd0cc2b06c8c875578de77a/860x10000.jpg",
                        "picture_description": "项目打造的公园，适合老人茶余饭后散步，环境非常好。"
                    },
                    {
                        "picture_label": "配套图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/806f8d17c9c16fe3ffcdd64778120f00/860x10000.jpg",
                        "picture_description": "周边的公园，紧邻着项目案场，步行仅需要10分钟。"
                    },
                    {
                        "picture_label": "配套图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/81479f6fa1f12aac86b498203eab4b87/860x10000.jpg",
                        "picture_description": "项目周边的一些简单生活配套，可满足住户日常所需。"
                    },
                    {
                        "picture_label": "配套图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/7212201b229efef09ca087e11fe36069/860x10000.jpg",
                        "picture_description": "项目附近的一些生活配套，可以满足住户的日常所需。"
                    },
                    {
                        "picture_label": "配套图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/04a344b0b09657e31b4582625e01ea91/860x10000.jpg",
                        "picture_description": ""
                    },
                    {
                        "picture_label": "配套图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/9afdd45bd8541a792824976277effb08/860x10000.jpg",
                        "picture_description": ""
                    },
                    {
                        "picture_label": "交通图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/893beb0a2b4ea6ea4064372204689be8/860x10000.jpg",
                        "picture_description": "楼盘区位规划"
                    },
                    {
                        "picture_label": "交通图",
                        "picture_url": "https://pic1.ajkimg.com/display/xinfang/e12ad39dd51b813f2645a721c96c12cf/860x10000.jpg",
                        "picture_description": "楼盘区位规划"
                    }
                ]
            ],
            "sale_status": "售罄",
            "city": "北京市",
            "name": "龙熙旭辉六号院",
            "labels": [
                "人车分流",
                "投资地产",
                "广场",
                "六环以外",
                "车位充足"
            ],
            "price": "别墅 待定",
            "property_type": "别墅",
            "developer": "尚未公开",
            "region": "六环以外-大兴-第二机场区",
            "address": "京开高速G45出口南1000米右转，北京龙熙温泉度假酒店北侧",
            "min_deposit": "尚未公开",
            "house_type": [
                "别墅户型"
            ],
            "opening_time": "2015-11-01",
            "delivery_time": "2018-06-15",
            "sale_address": "南四环诺德中心底商，汽车博物馆旁",
            "building_type": "双拼别墅",
            "story_status": "待定",
            "project_progress": "已竣工，交房时间：2015-11-20",
            "property_fee": "尚未公开",
            "property_company": "待定",
            "parking_ratio": "1:1",
            "formatted_address": "北京市大兴区龙熙旭辉六号院",
            "province": "北京市",
            "district": "大兴区",
            "location": "116.304234,39.628435",
            "pois": {
                "supermarket": [],
                "retail_store": [],
                "shopping_center": [],
                "catering_service": [
                    {
                        "poi_name": "宏轩饺子馆",
                        "poi_address": "团结路龙景湾4区33号楼109号",
                        "poi_location": "116.308967,39.629759",
                        "poi_distance": 431
                    },
                    {
                        "poi_name": "徐老师厨房",
                        "poi_address": "团结路龙景湾四区33号楼1至2层102",
                        "poi_location": "116.309040,39.629950",
                        "poi_distance": 445
                    },
                    {
                        "poi_name": "望京小腰(庞各庄店)",
                        "poi_address": "龙景湾四区35号楼115",
                        "poi_location": "116.309318,39.629787",
                        "poi_distance": 461
                    },
                    {
                        "poi_name": "六品居忆.京味北京菜",
                        "poi_address": "庞各庄镇团结路龙景湾四区35号楼12115号底商",
                        "poi_location": "116.310636,39.629932",
                        "poi_distance": 573
                    },
                    {
                        "poi_name": "三千茶农合作社",
                        "poi_address": "团结路龙景湾4区36号楼106",
                        "poi_location": "116.311354,39.629784",
                        "poi_distance": 628
                    },
                    {
                        "poi_name": "秦聚(庞各庄店)",
                        "poi_address": "龙景湾四区36号楼",
                        "poi_location": "116.311320,39.629906",
                        "poi_distance": 629
                    },
                    {
                        "poi_name": "老北京自助火锅",
                        "poi_address": "龙景湾四区33号楼1至2层103",
                        "poi_location": "116.311349,39.629831",
                        "poi_distance": 629
                    },
                    {
                        "poi_name": "老邻居家常菜",
                        "poi_address": "民生路龙景湾2区西北门旁",
                        "poi_location": "116.311108,39.626334",
                        "poi_distance": 634
                    },
                    {
                        "poi_name": "微食·原产地湘菜",
                        "poi_address": "龙景湾4区125号楼",
                        "poi_location": "116.311588,39.626850",
                        "poi_distance": 654
                    },
                    {
                        "poi_name": "飞常小厨",
                        "poi_address": "民生路路口西100米",
                        "poi_location": "116.311629,39.626938",
                        "poi_distance": 655
                    },
                    {
                        "poi_name": "鑫福园家常菜",
                        "poi_address": "庞各庄民生路龙景湾二区北门",
                        "poi_location": "116.311456,39.626488",
                        "poi_distance": 656
                    },
                    {
                        "poi_name": "一品烤肉",
                        "poi_address": "庞各庄镇李福路富力华庭苑南",
                        "poi_location": "116.311724,39.626722",
                        "poi_distance": 669
                    },
                    {
                        "poi_name": "巫山烤鱼家常菜(庞各庄店)",
                        "poi_address": "庞各庄镇团结路龙景湾四区37号楼E-101",
                        "poi_location": "116.311933,39.629965",
                        "poi_distance": 681
                    },
                    {
                        "poi_name": "木穆烧烤",
                        "poi_address": "龙景湾二区1号1至2层102",
                        "poi_location": "116.311886,39.626594",
                        "poi_distance": 687
                    },
                    {
                        "poi_name": "沙县小吃(庞各庄店)",
                        "poi_address": "庞各庄镇龙景湾四区37号楼",
                        "poi_location": "116.312084,39.629825",
                        "poi_distance": 690
                    },
                    {
                        "poi_name": "晋味香面馆(大兴店)",
                        "poi_address": "团结路与隆兴大街交叉口西南100米",
                        "poi_location": "116.312096,39.629969",
                        "poi_distance": 695
                    },
                    {
                        "poi_name": "渔把头饭店",
                        "poi_address": "庞各庄镇龙景湾二区1号楼101",
                        "poi_location": "116.312140,39.626438",
                        "poi_distance": 713
                    },
                    {
                        "poi_name": "山西刀削面(庞各庄)",
                        "poi_address": "庞各庄镇丹麦小镇D座E4-107",
                        "poi_location": "116.312329,39.629975",
                        "poi_distance": 714
                    },
                    {
                        "poi_name": "海华阿里美食",
                        "poi_address": "团结路隆兴大街交叉口南50米",
                        "poi_location": "116.312864,39.629328",
                        "poi_distance": 746
                    },
                    {
                        "poi_name": "川味火锅",
                        "poi_address": "团结路童话时光东区北门向西200米处",
                        "poi_location": "116.313774,39.632659",
                        "poi_distance": 943
                    }
                ],
                "theater": [],
                "hotel": [],
                "primary_school": [],
                "middle_school": [],
                "high_school": [],
                "museum": [
                    {
                        "poi_name": "龙熙维景国际会议中心",
                        "poi_address": "隆华大街55号院7号楼",
                        "poi_location": "116.302128,39.624751",
                        "poi_distance": 448
                    }
                ],
                "bus": [
                    {
                        "poi_name": "旭辉6号院(公交站)",
                        "poi_address": "兴65路",
                        "poi_location": "116.300407,39.627399",
                        "poi_distance": 347
                    },
                    {
                        "poi_name": "龙景湾四区(公交站)",
                        "poi_address": "兴65路",
                        "poi_location": "116.307831,39.630066",
                        "poi_distance": 357
                    },
                    {
                        "poi_name": "天恒7号院(公交站)",
                        "poi_address": "兴64路",
                        "poi_location": "116.303795,39.632809",
                        "poi_distance": 488
                    },
                    {
                        "poi_name": "富力丹麦小镇北站(公交站)",
                        "poi_address": "兴55路",
                        "poi_location": "116.309395,39.626030",
                        "poi_distance": 517
                    },
                    {
                        "poi_name": "兴展地块(公交站)",
                        "poi_address": "兴64路;兴65路",
                        "poi_location": "116.300293,39.631966",
                        "poi_distance": 518
                    },
                    {
                        "poi_name": "龙熙酒店西(公交站)",
                        "poi_address": "兴64路;兴65路",
                        "poi_location": "116.300407,39.624805",
                        "poi_distance": 520
                    },
                    {
                        "poi_name": "龙熙庄园(公交站)",
                        "poi_address": "X108路",
                        "poi_location": "116.305550,39.623775",
                        "poi_distance": 530
                    },
                    {
                        "poi_name": "龙景湾小区北(公交站)",
                        "poi_address": "X108路",
                        "poi_location": "116.313004,39.629444",
                        "poi_distance": 760
                    },
                    {
                        "poi_name": "龙景湾小区(公交站)",
                        "poi_address": "X108路",
                        "poi_location": "116.312439,39.625599",
                        "poi_distance": 771
                    },
                    {
                        "poi_name": "富力丹麦小镇(公交站)",
                        "poi_address": "兴55路;兴65路",
                        "poi_location": "116.314301,39.630024",
                        "poi_distance": 881
                    },
                    {
                        "poi_name": "隆顺路北口(公交站)",
                        "poi_address": "X108路",
                        "poi_location": "116.307121,39.620720",
                        "poi_distance": 893
                    },
                    {
                        "poi_name": "中瑞酒店管理学院(公交站)",
                        "poi_address": "兴54路;兴65路",
                        "poi_location": "116.307137,39.620720",
                        "poi_distance": 894
                    },
                    {
                        "poi_name": "中瑞酒店学院(公交站)",
                        "poi_address": "兴54路",
                        "poi_location": "116.307602,39.620609",
                        "poi_distance": 917
                    },
                    {
                        "poi_name": "隆顺路口(公交站)",
                        "poi_address": "兴65路",
                        "poi_location": "116.300438,39.620014",
                        "poi_distance": 992
                    },
                    {
                        "poi_name": "富力华庭北门(公交站)",
                        "poi_address": "兴64路",
                        "poi_location": "116.314354,39.632843",
                        "poi_distance": 996
                    }
                ],
                "subway": [],
                "train": [],
                "plane": [
                    {
                        "poi_name": "南苑机场航空货运代理",
                        "poi_address": "金安路37号",
                        "poi_location": "116.390194,39.778095",
                        "poi_distance": 18214
                    },
                    {
                        "poi_name": "北京南苑机场",
                        "poi_address": "南苑镇警备东路6号",
                        "poi_location": "116.39428,39.784163",
                        "poi_distance": 18973
                    },
                    {
                        "poi_name": "北京南苑机场货运处",
                        "poi_address": "南小街北路附近",
                        "poi_location": "116.398689,39.790364",
                        "poi_distance": 19757
                    }
                ],
                "coach": [
                    {
                        "poi_name": "窑上客运站",
                        "poi_address": [],
                        "poi_location": "116.196143,39.610772",
                        "poi_distance": 9474
                    }
                ],
                "exit_entrance": [
                    {
                        "poi_name": "庞各庄出口(G45大广高速南向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.323771,39.638330",
                        "poi_distance": 2004
                    },
                    {
                        "poi_name": "庞各庄收费站入口(北京城区方向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.324167,39.638802",
                        "poi_distance": 2062
                    },
                    {
                        "poi_name": "薛营收费站入口(开封方向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.326461,39.610717",
                        "poi_distance": 2742
                    },
                    {
                        "poi_name": "庞各庄出口(G45大广高速北向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.326951,39.611013",
                        "poi_distance": 2748
                    },
                    {
                        "poi_name": "三融收费站入口(开封方向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.323501,39.654540",
                        "poi_distance": 3342
                    },
                    {
                        "poi_name": "西庄出口(G45大广高速北向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.324035,39.654742",
                        "poi_distance": 3384
                    },
                    {
                        "poi_name": "梨花桥收费站入口(北京城区方向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.327871,39.595176",
                        "poi_distance": 4221
                    },
                    {
                        "poi_name": "梨园出口(G45大广高速南向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.327316,39.594923",
                        "poi_distance": 4223
                    },
                    {
                        "poi_name": "魏永路出口(G45大广高速南向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.324361,39.671507",
                        "poi_distance": 5095
                    },
                    {
                        "poi_name": "天宫院收费站入口(北京城区方向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.324911,39.671986",
                        "poi_distance": 5161
                    },
                    {
                        "poi_name": "魏永路北出口(G45大广高速南向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.324482,39.672523",
                        "poi_distance": 5205
                    },
                    {
                        "poi_name": "北臧村收费站入口(黄村方向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.288035,39.691464",
                        "poi_distance": 7152
                    },
                    {
                        "poi_name": "芦城出口(南六环东向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.283683,39.691256",
                        "poi_distance": 7211
                    },
                    {
                        "poi_name": "北臧村出口(南六环西向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.284023,39.691528",
                        "poi_distance": 7233
                    },
                    {
                        "poi_name": "北臧村收费站入口(房山方向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.281414,39.691405",
                        "poi_distance": 7277
                    },
                    {
                        "poi_name": "黄村出口(南六环东向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.315686,39.695219",
                        "poi_distance": 7498
                    },
                    {
                        "poi_name": "念坛收费站入口(马驹桥方向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.314003,39.696026",
                        "poi_distance": 7570
                    },
                    {
                        "poi_name": "念坛收费站入口(南六环西南向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.313655,39.696223",
                        "poi_distance": 7589
                    },
                    {
                        "poi_name": "黄村出口(南六环西向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.315790,39.698123",
                        "poi_distance": 7820
                    },
                    {
                        "poi_name": "大礼路收费站入口(京开高速方向)",
                        "poi_address": "大兴区",
                        "poi_location": "116.324728,39.554960",
                        "poi_distance": 8366
                    }
                ],
                "medical_service": [
                    {
                        "poi_name": "嘉美口腔",
                        "poi_address": "团结路龙景湾四区33号楼E1-111",
                        "poi_location": "116.309257,39.629813",
                        "poi_distance": 457
                    },
                    {
                        "poi_name": "中国人寿健康养老北京体验中心",
                        "poi_address": "庞各庄顺景路8号",
                        "poi_location": "116.303634,39.623610",
                        "poi_distance": 539
                    },
                    {
                        "poi_name": "北京仁宠动物医院",
                        "poi_address": "庞各庄丹麦小镇团结路宠物都市E3",
                        "poi_location": "116.311248,39.629904",
                        "poi_distance": 623
                    },
                    {
                        "poi_name": "北京掌控慢病科技服务中心",
                        "poi_address": "隆兴大街附近",
                        "poi_location": "116.311930,39.626773",
                        "poi_distance": 685
                    },
                    {
                        "poi_name": "北京家和安康医药有限公司",
                        "poi_address": "团结路与隆兴大街交叉口西100米",
                        "poi_location": "116.312116,39.629895",
                        "poi_distance": 695
                    },
                    {
                        "poi_name": "千草安瑞平价大药房(富力店)",
                        "poi_address": "团结路19号院4号楼1层102",
                        "poi_location": "116.314685,39.632680",
                        "poi_distance": 1012
                    },
                    {
                        "poi_name": "北京鑫兴祥瑞药店",
                        "poi_address": "瓜乡路32号院2",
                        "poi_location": "116.309675,39.620036",
                        "poi_distance": 1044
                    },
                    {
                        "poi_name": "恒泰乐民大药房",
                        "poi_address": "幸福村隆兴大街富力华庭苑",
                        "poi_location": "116.316110,39.630672",
                        "poi_distance": 1048
                    },
                    {
                        "poi_name": "于记镶牙馆",
                        "poi_address": "瓜乡路10-8号楼附近",
                        "poi_location": "116.312395,39.620244",
                        "poi_distance": 1149
                    },
                    {
                        "poi_name": "庞各庄镇残疾人康复服务指导站",
                        "poi_address": "庞各庄镇繁荣村附近",
                        "poi_location": "116.319063,39.628905",
                        "poi_distance": 1272
                    },
                    {
                        "poi_name": "北京市大兴区庞各庄镇中心卫生院",
                        "poi_address": "庞各庄镇繁荣村",
                        "poi_location": "116.319224,39.628937",
                        "poi_distance": 1286
                    },
                    {
                        "poi_name": "庞各庄医院-急诊",
                        "poi_address": "庞北路与隆源大街交叉口东100米",
                        "poi_location": "116.319710,39.628761",
                        "poi_distance": 1327
                    },
                    {
                        "poi_name": "北京京兴振国诊所",
                        "poi_address": "隆盛大街附近",
                        "poi_location": "116.321608,39.631459",
                        "poi_distance": 1527
                    },
                    {
                        "poi_name": "德宜康门诊",
                        "poi_address": "幸福路与隆盛大街交叉口南100米",
                        "poi_location": "116.321626,39.632814",
                        "poi_distance": 1568
                    },
                    {
                        "poi_name": "阳光百益大药房(第八分店)",
                        "poi_address": "团结路与隆盛大街交叉口东北200米",
                        "poi_location": "116.322251,39.631478",
                        "poi_distance": 1581
                    },
                    {
                        "poi_name": "德益康诊所(口腔)",
                        "poi_address": "幸福路与隆盛大街交叉口东南100米",
                        "poi_location": "116.321760,39.632980",
                        "poi_distance": 1585
                    },
                    {
                        "poi_name": "京南口腔",
                        "poi_address": "团结路与隆盛大街交叉口东北150米",
                        "poi_location": "116.322405,39.631349",
                        "poi_distance": 1591
                    },
                    {
                        "poi_name": "恒泰祥和大药房(御园店)",
                        "poi_address": "民生路",
                        "poi_location": "116.322610,39.626414",
                        "poi_distance": 1591
                    },
                    {
                        "poi_name": "越一堂中医诊所",
                        "poi_address": "幸福路与隆盛大街交叉口东南100米",
                        "poi_location": "116.322034,39.632972",
                        "poi_distance": 1607
                    },
                    {
                        "poi_name": "猫小院的宠物健康生活馆",
                        "poi_address": "隆丰大街1号院1号楼1-5",
                        "poi_location": "116.323497,39.633142",
                        "poi_distance": 1732
                    }
                ],
                "bank": [],
                "ATM": [
                    {
                        "poi_name": "中国农业银行ATM(顺景路)",
                        "poi_address": "龙熙维景国际会议中心1层",
                        "poi_location": "116.302026,39.624614",
                        "poi_distance": 465
                    }
                ],
                "radiation_pollution": [],
                "gas": [],
                "funeral_parlor": [
                    {
                        "poi_name": "繁盛寿衣店",
                        "poi_address": "庞各庄收费站西北70米(京开路西)",
                        "poi_location": "116.323060,39.638714",
                        "poi_distance": 1978
                    },
                    {
                        "poi_name": "大兴殡仪馆",
                        "poi_address": "天堂河地区京开高速三融桥东200米",
                        "poi_location": "116.327957,39.658293",
                        "poi_distance": 3896
                    },
                    {
                        "poi_name": "北京市大兴区天堂公墓",
                        "poi_address": "黄村镇西庄路18号",
                        "poi_location": "116.344149,39.660845",
                        "poi_distance": 4972
                    }
                ],
                "park": [
                    {
                        "poi_name": "体育公园",
                        "poi_address": "团结路与隆兴大街交叉口东南150米",
                        "poi_location": "116.314081,39.629516",
                        "poi_distance": 852
                    },
                    {
                        "poi_name": "庞各庄众美公园",
                        "poi_address": "幸福路与G45大广高速交叉口西南50米",
                        "poi_location": "116.324510,39.633246",
                        "poi_distance": 1818
                    }
                ],
                "square": [],
                "water_system": [
                    {
                        "poi_name": "永兴河",
                        "poi_address": "大兴区",
                        "poi_location": "116.318166,39.626562",
                        "poi_distance": 1212
                    }
                ],
                "scenic_area": []
            }
        }
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)