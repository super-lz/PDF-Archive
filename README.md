# autofind
Automatically find scholarly article.

把pdf文件全部放入origin文件夹中，程序将自动转pdf为txt格式，然后通过输入的关键词句查找对应的pdf文件

该程序用到了tesseract识别引擎


## notice
chmod +x restore.sh
chmod +x build.sh

restore.sh用于测试时快捷删除处理得到的source和data.json，每次commit要把测试的.config清空

build.sh用于构建程序

## for normal step
4. pip install -r requirements.txt
5. 设置pyinstaller的环境变量
6. python main.py

## for ocr step
1. 安装tesseract（别忘了安装时选择中文语言包chi_sim.traineddata），https://digi.bib.uni-mannheim.de/tesseract/
2. 在windows系统下，应该需要创建环境变量，在系统变量里，创建一个新的变量名为:TESSDATA_PREFIX，值为:C:\Program Files\Tesseract-OCR\tessdata(根据自己安装的tesserocr安装路径为准)
3. 确保你已经安装了Poppler。你可以从Poppler的官方网站（https://poppler.freedesktop.org/）下载适合你操作系统的版本，并按照安装说明进行安装。或者，你也可以使用包管理器（如apt、brew或choco）来安装Poppler。添加Poppler到系统的环境变量中这样，当你运行pdf2image库时，系统就能够找到Poppler的可执行文件。
4. pip install -r requirements.txt
5. 设置pyinstaller的环境变量
6. python main.py

## pip env
可以使用虚拟环境安装python库，避免污染