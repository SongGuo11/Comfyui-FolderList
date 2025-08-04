"""
ComfyUI Folder List Plugin
"""

from .folder_list_node import FolderList, FileListNode

NODE_CLASS_MAPPINGS = {
    "FolderList": FolderList,
    "FileListNode": FileListNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FolderList": "文件夹列表",
    "FileListNode": "文件列表"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]