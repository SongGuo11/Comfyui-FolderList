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


class FileListNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "folder_path": ("STRING", {"default": ""}),
            },
            "optional": {
                "show_count": ("BOOLEAN", {"default": False}),
                "start_index": ("INT", {"default": 0, "min": 0, "max": 9999}),
                "file_formats": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "list_files"
    CATEGORY = "list/IO"

    def list_files(self, folder_path, show_count=False, start_index=0, file_formats=""):
        if not os.path.exists(folder_path):
            raise ValueError(f"Folder path '{folder_path}' does not exist.")
            
        files = os.listdir(folder_path)
        
        # Filter files by format if specified
        if file_formats:
            formats = [f.strip().lower() for f in file_formats.split(",") if f.strip()]
            if formats:
                files = [f for f in files if any(f.lower().endswith(ext) for ext in formats)]
        
        # Sort files for consistent output
        files.sort()
        
        # Apply start index
        files = files[start_index:]
        
        # Join files with "、"
        result = "、".join(files)
        
        # Add count if requested
        if show_count:
            result += f" (Total: {len(files)})"
            
        return (result,)