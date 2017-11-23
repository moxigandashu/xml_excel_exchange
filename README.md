# xml_excel_exchange
xml与Excel互相转换的工具，含GUI界面

## xml和Excel互相转换工具说明
### 零、说明
包含三个文件：
1. baikal_strings.xml是一个xml文件的case
2. baikal_strings.xmlref_table是一个翻译过的case
3. change.py是运行脚本

### 一、背景和功能
功能：用于xml文件与Excel文件互相转换，
   app开发，特别是多语言的开发，为了开发的高效性，通常会用修改xml文件的方式，来快速替代文案，因此需要将xml中的字符串提取到xml，给到产品端进行翻译，之后从新替换，本工具用于提取xml的字符串到Excel，并将翻译后的Excel表格，再次转换到xml文件中。

### 二、工具运行环境
1. Python环境：python3.7,3.0以后的版本可以运行；
2. 需要的包：
    需要安装的包：
        - pandas用于数据处理
        - Beautifulsoup用于提取xml文件
    Python自带的包：
        - os用于修改工作路径；
        - tkinter用于GUI
 
 ### 三、操作步骤
 执行change.py，在框
 1. 提取xml中的字符串到Excel：点击xml->excel
 2. 将翻译后的excel替代xml字符串：点击Excel->xml
 
