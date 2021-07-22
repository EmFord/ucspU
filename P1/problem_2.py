import os
PATH = "testdir/"

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path is None:
        return -1

    c_files = []
    for dir_item in os.listdir(path):
        print("Starting....", dir_item)
        check_item_path = os.path.join(path, dir_item)
        if os.path.isfile(check_item_path):
            if check_item_path.endswith(suffix):
                c_files.append(check_item_path)

        elif os.path.isdir(check_item_path):
            print("Going into subdirectory....")
            sub_result = find_files(suffix, check_item_path)
            if len(sub_result) == 0:
                continue
            if isinstance(sub_result, list):
                [c_files.append(item) for item in sub_result]
            else:
                c_files.append(sub_result)

    return c_files


# Test cases
print(len(find_files(".c", PATH)))
# 4

print(find_files(" ", PATH))
# []

print(len(find_files("", PATH)))
# 10

print(find_files("testdir", PATH))
# []

print(find_files("testdir", None))
# -1
