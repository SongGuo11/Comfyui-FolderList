from comfy.utils import ProgressBar
import os

class FolderList:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": ("STRING", {"default": "C:/", "multiline": False, "dynamicFilename": True}),
                "show_count": ("BOOLEAN", {"default": False, "label": "显示文件夹数量"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "list_folders"
    CATEGORY = "list/IO"

    def list_folders(self, folder_path, show_count=False):
        try:
            # 获取指定目录下的所有文件夹名称
            folders = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
            
            # 如果需要显示文件夹数量
            if show_count:
                result = f"总共有{len(folders)}个文件夹：{'、'.join(folders)}"
            else:
                result = '、'.join(folders)
                
            return (result,)
        except Exception as e:
            return (f"错误：{str(e)}",)