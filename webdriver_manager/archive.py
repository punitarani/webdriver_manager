import tarfile
import zipfile


def extract_zip(zip_file, to_directory):
    archive = zipfile.ZipFile(zip_file)
    try:
        archive.extractall(to_directory)
    except Exception as e:
        if e.args[0] != 26:
            raise e
    return archive.namelist()


def extract_tar_file(tar_file_path, to_dir):
    try:
        tar = tarfile.open(tar_file_path, mode="r:gz")
    except tarfile.ReadError:
        tar = tarfile.open(tar_file_path, mode="r:bz2")
    members = tar.getmembers()
    tar.extractall(to_dir)
    tar.close()
    return members
