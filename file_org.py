#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/5 14:16
# @Author: qyh


import glob
import os
import shutil


class FileType:
    def __init__(self):
        self.file_type = {
            "图片": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
            "视频": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".asf",
                   ".dat", ".rmvb", ".asx"],
            "音频": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".flac",
                   ".ape", ".wav"],
            "文档": [".md", ".pdf", ".csv", ".pptx", ".ppt", ".xlsx", ".xls", ".doc", ".docx", ".oxps", ".epub",
                   ".pages", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".rvg", ".rtf", ".rtfd"],
            "压缩文件": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xzr", ".zip", ".xz"],
            "文本": [".txt", ".in", ".out"],
            "程序脚本": [".py", ".html5", ".html", ".htm", ".xhtml", ".xml", ".c", ".cpp", ".hpp", ".java", ".css", ".js"],
            "可执行程序": [".exe"],
            "字体文件": [".ttf", ".OTF", ".WOFF", ".EOT"],
        }

    def judge_file(self, pathname):
        for name, type in self.file_type.items():
            if pathname in type:
                return name
        return "无法判断文件类型"


class FileOrg(object):
    def __init__(self):
        self.file_type = FileType()

    def organization(self):
        filepath = input("请输入需要整理的文件夹路径：")
        paths = glob.glob(filepath + "/*.*")
        print(paths)
        for path in paths:
            try:
                if not os.path.isdir(path):
                    file = os.path.splitext(path)
                    filename, type = file
                    print(type)
                    print(path)
                    save_path = '/'.join(path.split("\\")[:-1]) + '/{}'.format(self.file_type.judge_file(type))
                    if not os.path.exists(save_path):
                        os.mkdir(save_path)
                        shutil.move(path, save_path)
                    else:
                        shutil.move(path, save_path)
            except FileNotFoundError:
                pass
        print("执行结束")


if __name__ == '__main__':
    file_org = FileOrg()
    file_org.organization()
