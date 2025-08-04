# ComfyUI Folder List Plugin

这是一个简单的ComfyUI插件，用于列出指定文件夹中的所有子文件夹和文件。

## 功能

### 文件夹列表 (FolderList)
- 输入一个文件夹路径
- 输出该文件夹下所有子文件夹的名称，用顿号分隔
- 可选是否显示文件夹数量
- 可选设置输出的文件夹数量
- 可选设置从第几个文件夹开始输出

### 文件列表 (FileListNode)
- 输入一个文件夹路径
- 输出该文件夹下所有文件的名称，用顿号分隔
- 可选是否显示文件数量
- 可选设置从第几个文件开始输出
- 可选按文件格式过滤（例如：png, jpg, mp4等）

## 使用方法

### 文件夹列表 (FolderList)
1. 在ComfyUI中添加`FolderList`节点
2. 设置`folder_path`参数为你想要查询的文件夹路径
3. 选择是否要显示文件夹数量（show_count）
4. 设置要输出的文件夹数量（count）
5. 设置从第几个文件夹开始输出（start_index）
6. 运行流程图，获取子文件夹列表

### 文件列表 (FileListNode)
1. 在ComfyUI中添加`FileListNode`节点
2. 设置`folder_path`参数为你想要查询的文件夹路径
3. 选择是否要显示文件数量（show_count）
4. 设置从第几个文件开始输出（start_index）
5. 设置要过滤的文件格式，多个格式用逗号分隔（file_formats）
6. 运行流程图，获取文件列表

## 示例

### 文件夹列表示例
假设文件夹"a"下有子文件夹"a1"、"a2"、"a3"、"a4"、"a5"
1. 不显示数量：当输入文件夹地址"C:\a"的时候输出"a1、a2、a3、a4、a5"
2. 显示数量：当输入文件夹地址"C:\a"的时候输出"总共有5个文件夹：a1、a2、a3、a4、a5"
3. 输出2个文件夹：当设置count=2时输出"a1、a2"
4. 从第2个文件夹开始：当设置start_index=2时输出"a3、a4、a5"
5. 组合使用：设置start_index=1，count=3时输出"a2、a3、a4"

### 文件列表示例
假设文件夹"a"下有文件"a1.png"、"a2.jpg"、"a3.mp4"、"a4.txt"、"a5.png"
1. 列出所有文件：当输入文件夹地址"C:\a"的时候输出"a1.png、a2.jpg、a3.mp4、a4.txt、a5.png"
2. 显示数量：设置show_count=true时输出"a1.png、a2.jpg、a3.mp4、a4.txt、a5.png (Total: 5)"
3. 从第2个文件开始：当设置start_index=2时输出"a3.mp4、a4.txt、a5.png"
4. 过滤PNG文件：当设置file_formats="png"时输出"a1.png、a5.png"
5. 过滤多种格式：当设置file_formats="png, jpg"时输出"a1.png、a2.jpg、a5.png"