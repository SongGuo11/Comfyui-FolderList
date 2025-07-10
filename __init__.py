"""
ComfyUI Folder List Plugin
"""

from .folder_list_node import FolderList

NODE_CLASS_MAPPINGS = {
    "FolderList": FolderList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FolderList": "文件夹列表"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]