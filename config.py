# coding=utf-8

context_feature_list = [
    1060,   # 上下文特征-一级地域
    1061,   # 上下文特征-二级类别
    1062,   # 上下文特征-三级类别
    1063,   # 用户是否登录
    1064,   # 当前小时
    1065,   # 所在推荐位,应考虑单推荐位建模
    1066,   # 展现位置,确认是分页后展现位置还是分页前展现位置
    1076,   # 搜索词长度
]

user_feature_list = [

]

info_feature_list = [
    1,      # 帖子要求学历 A
    2,      # 帖子招聘人数 A
    3,      # 帖子离散化后薪资 A
    4,      # 帖子五险一金福利 A
    5,      #
    6,      # 话补福利
    7,      # 房补福利
    8,      # 交通补助福利
    9,      # 周末双休福利 A
    10,     # 加班补助福利 A
    11,     # 包住福利 A
    12,     # 年底双薪福利
    13,     # 包吃福利 A
    14,     # 免费培训福利
    15,     # 环境好福利
    17,     # 工作经验年数要求 A
    18,     # 帖子发布日期与当前日期时间差 用户根本看不到
    19,     # 帖子更新日期与当前日期时间差 用户根本看不到
    20,     # info标题长度 A
    21,     # info标题是否包含数字
    22,     # 是否接受应届生
    28,     # 帖子发布地址1 A
    29,     # 帖子发布地址2 A
    30,     # 帖子发布地址3 A
    31,     # 帖子归属类别1 A
    32,     # 帖子归属类别2 A
    33,     # 帖子归属类别3 A
]

info_statistics_feature_list = [
    700,    # 帖子CTR, 有争议
    701,    # 帖子CVR, 有争议
    706,    # 过去7天点击量, 有争议
    707,    # 过去7天点击率, 有争议
    708,    # 过去7天im点击量, 有争议
    709,    # 过去7天电话点击量, 有争议
]

# 用到的特征
feature_list = list()
feature_list.append(user_feature_list)
feature_list.append(info_feature_list)
feature_list.append(context_feature_list)
