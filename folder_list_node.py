from comfy.utils import ProgressBar
import os

class FolderList:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": ("STRING", {"default": "C:/", "multiline": False, "dynamicFilename": True}),
                "show_count": ("BOOLEAN", {"default": False, "label": "显示文件夹数量"}),
                "count": ("INT", {"default": 0, "min": 0, "max": 100, "step": 1, "display": "number", "label": "输出文件夹数量"}),
                "start_index": ("INT", {"default": 0, "min": 0, "max": 100, "step": 1, "display": "number", "label": "起始文件夹索引"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "list_folders"
    CATEGORY = "list/IO"

    def list_folders(self, folder_path, show_count=False, count=0, start_index=0):
        try:
            # 获取指定目录下的所有文件夹名称
            folders = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
            
            # 处理起始索引
            if start_index > 0:
                folders = folders[start_index:]
                
            # 处理输出数量
            if count > 0 and count < len(folders):
                folders = folders[:count]
            
            # 如果需要显示文件夹数量
            if show_count:
                result = f"总共有{len(folders)}个文件夹：{'、'.join(folders)}"
            else:
                result = '、'.join(folders)
                
            return (result,)
        except Exception as e:
            return (f"错误：{str(e)}",)