import os


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
