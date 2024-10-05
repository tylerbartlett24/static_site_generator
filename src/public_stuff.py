import os
import shutil

def actual_copy(source, destination):
    contents = os.listdir(source)
    for content in contents:
        source_path = os.path.join(source, content)
        destination_path = os.path.join(destination, content)
        if os.path.isfile(source_path) or os.path.islink(source_path):
            shutil.copy(source_path, destination_path)
        else:
            os.mkdir(destination_path)
            actual_copy(source_path, destination_path)

def copy_from_static_to_public(source, destination):
    if not os.path.exists(source):
        raise Exception("Source does not exist")
    if not os.path.exists(destination):
        os.mkdir(destination)
    contents = os.listdir(destination)
    for content in contents:
        file_path = os.path.join(destination, content)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    actual_copy(source, destination)