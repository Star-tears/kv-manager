import os
import shutil


def get_folder_list(path):
    """
    获取指定路径下的文件夹列表
    :param path: 指定路径
    :return: 文件夹列表
    """
    folder_list = []
    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)
        if os.path.isdir(folder_path):
            folder_list.append(folder)

    return folder_list


def create_folder(path):
    """
    创建文件夹
    :param path: 文件夹路径
    :return: 是否创建成功
    """
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:
        return False


def delete_folder(folder_path):
    """
    删除指定的文件夹及其包含的所有内容。

    :param folder_path: 要删除的文件夹路径
    """
    try:
        shutil.rmtree(folder_path)
        return True
    except OSError as e:
        print(f"删除文件夹时发生错误: {e.strerror}")
        return False


def rename_file(old_path, new_path):
    """
    重命名文件、文件夹
    :param old_path: 旧文件路径
    :param new_path: 新文件路径
    """
    # 使用os.rename()函数进行重命名操作
    try:
        os.rename(old_path, new_path)
        print(f"文件'{old_path}'已成功重命名为'{new_path}'")
    except OSError as e:
        print(f"重命名文件时发生错误: {e.strerror}")
