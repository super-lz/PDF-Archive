# autofind
Automatically find scholarly article


# notice
chmod +x restore.sh
chmod +x build.sh

restore.sh用于测试时快捷删除处理得到的source和data.json
build.sh用于构建程序


# step
1. 安装tesseract，https://digi.bib.uni-mannheim.de/tesseract/，别忘了安装时选择中文语言包chi_sim.traineddata
2. 在windows系统下，应该需要创建环境变量，在系统变量里，创建一个新的变量名为:TESSDATA_PREFIX，值为:C:\Program Files\Tesseract-OCR\tessdata(根据自己安装的tesserocr安装路径为准)
3. pip install -r requirements.txt
4. 设置pyinstaller的环境变量
5. python main.py