#!/bin/bash

# 进入当前文件夹
cd "$(dirname "$0")"

# 清空文件夹
rm -rf build
rm -rf soft

# 指定打包路径为当前文件夹的 dist 目录
distpath="./soft"

# 执行 PyInstaller 打包命令，单文件打包
pyinstaller -F -w -i icon.ico --distpath "$distpath" main.py

# 进入 soft 文件夹
cd $distpath

# 删除 origin 文件夹（如果存在），然后创建它
if [ -d "origin" ]; then
  rm -rf origin
fi
mkdir origin

# 删除 source 文件夹（如果存在），然后创建它
if [ -d "source" ]; then
  rm -rf source
fi
mkdir source

# 删除 data.json 文件（如果存在），然后创建它
if [ -f "data.json" ]; then
  rm data.json
fi
touch data.json

# 返回上级文件夹
cd ..

# 复制 origin 文件夹下的所有文件到 soft/origin
cp -r ./origin/* ./soft/origin/

cp -r .config ./soft/.config

# 打包完成后输出提示信息
echo "打包完成！可执行文件位于 $distpath 目录中。"
