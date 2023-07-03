# autofind
Automatically find scholarly article.

把pdf文件全部放入origin文件夹中，程序将自动转pdf为txt格式，然后通过输入的关键词句查找对应的pdf文件

该程序用到了tesseract识别引擎


## notice
chmod +x restore.sh
chmod +x build.sh

restore.sh用于测试时快捷删除处理得到的source和data.json，每次commit要把测试的.config清空

build.sh用于构建程序


## step
1. 安装tesseract（别忘了安装时选择中文语言包chi_sim.traineddata），https://digi.bib.uni-mannheim.de/tesseract/
2. 在windows系统下，应该需要创建环境变量，在系统变量里，创建一个新的变量名为:TESSDATA_PREFIX，值为:C:\Program Files\Tesseract-OCR\tessdata(根据自己安装的tesserocr安装路径为准)
3. pip install -r requirements.txt
4. 设置pyinstaller的环境变量
5. python main.py