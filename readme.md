<a name="778d2597"></a>
# 一句话概述：
基于youtube和bilibili等其他平台和零一万物大模型构建大语言模型高质量训练数据集（计划支持可自定义输出的训练数据格式）

# update news！
<b>2024-5-2</b>：增加对webpage网页的question生成支持
<br>项目地址：https://github.com/zjrwtx/WebQuestions_databuilder
<br>通过Yi模型或ollama的本地小模型对输入的webpage网页地址的内容合成高质量的questions数据供微调数据合成使用

<b>2024-4-29</b>：增加对bilibili视频的question生成支持
<br>项目地址：https://github.com/zjrwtx/bilibiliQA_databuilder 
<br>可基于bilibili视频构建大模型问答训练数据，输入bilibili视频地址等信息即可生成questions数据供videoQA_databuilder项目使用


# 演示视频地址
[基于youtube和bilibili等其他平台和零一万物大模型构建大语言模型高质量训练数据集（计划支持可自定义输出的训练数据格式）
](https://www.bilibili.com/video/BV1GF4m1A7op/?spm_id_from=333.999.0.0)<br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/22859856/1714052729621-26e11c49-447e-4694-a9f6-7656d7fcd7ad.png#averageHue=%23fed776&clientId=uf7c9d25c-e51d-4&from=paste&height=611&id=u3e3215fc&originHeight=916&originWidth=1908&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=247556&status=done&style=none&taskId=ud7d91d8e-8e3d-4faa-9289-e9fa1998165&title=&width=1272)<br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/22859856/1714052768380-8c96a6aa-5138-4c9b-af5c-f2947958704d.png#averageHue=%23e6a68a&clientId=uf7c9d25c-e51d-4&from=paste&height=611&id=u91344d52&originHeight=916&originWidth=1908&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=358232&status=done&style=none&taskId=u2ca365e2-57bd-4a72-ab91-e804c4f6aba&title=&width=1272)

<a name="3c1bca16"></a>
## 使用过程描述：

使用youtubquestion_builder.py生成指定视频的questions文件——本项目读取questions文件——然后基于零一万物模型生成基于视频内容的回答后自我调整——最后将回答保存到answers.json文件。

本项目遵循GPL许可证，欢迎贡献代码或提出改进建议。项目地址：[https://github.com/zjrwtx/VideoQA_databuilder](https://github.com/zjrwtx/VideoQA_databuilder)

<a name="0cfeb4d9"></a>
# 如何运行

1、克隆到本地

```git
git clone https://github.com/zjrwtx/AIgene_anki.git
```

2、安装依赖

```git
pip install -r requirements.txt
```

3、复制.env.example文件为.env 填写大模型的环境变量

4、运行python main.py 如顺利无报错 即可看到可视化程序

5、使用youtubquestion_builder.py生成指定视频的questions文件

6、开始在可视化程序上读取questions文件，填写必要内容，利用零一万物大模型生成对应数据answers



<a name="bb966aa6"></a>
# 贡献

欢迎贡献。请先 fork 仓库，然后提交一个 pull request 包含你的更改。

<a name="e40a454f"></a>
# 联系我

<a name="da671a4d"></a>
## 微信：

agi_isallyouneed

<a name="e8c53647"></a>
## 微信公众号：正经人王同学

![](https://cdn.nlark.com/yuque/0/2024/jpeg/22859856/1713801561819-9d19cb9a-1233-4295-ad90-56042bbabd3c.jpeg#averageHue=%23a2a1a0&clientId=u7b5f5d88-e731-4&from=paste&height=172&id=u329dbc86&originHeight=430&originWidth=430&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=40862&status=done&style=none&taskId=u7551bc0b-a19a-4ff7-8b6e-1c0d27b3ae1&title=&width=171.66668701171875#averageHue=%23a2a1a0&id=SjL3U&originHeight=430&originWidth=430&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=#averageHue=%23a2a1a0&id=dJonX&originHeight=430&originWidth=430&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

<a name="58082d81"></a>
## X（推特)正经人王同学:[https://twitter.com/zjrwtx](https://twitter.com/zjrwtx)



<a name="20a28457"></a>
# 许可证

本项目遵循GPL许可证，欢迎贡献代码或提出改进建议。项目地址：[https://github.com/zjrwtx/VideoQA_databuilder](https://github.com/zjrwtx/VideoQA_databuilder)

非商业用途：本项目的所有源代码和相关文档仅限于非商业用途。任何商业用途均被严格禁止。

出处声明：任何个人或实体在修改、分发或使用本项目时，必须清楚地标明本项目的原始来源，并且保留原始作者的版权声明。

<a name="D4GjD"></a>
# 特别感谢
[零一万物](https://github.com/01-ai/Yi)

本项目主要参考以下项目而改造：<br />[https://github.com/huang1332/finetune_dataset_maker](https://github.com/huang1332/finetune_dataset_maker)

