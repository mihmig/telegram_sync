# Загрузка файлов на Yandex-disk
# https://yandex.ru/dev/disk/rest/
# https://yadisk.readthedocs.io/ru/latest/intro.html
# Работа через REST https://ramziv.com/article/8
import os

import yadisk
y = yadisk.YaDisk(token=os.environ['YANDEX_TOKEN'])
# or
# y = yadisk.YaDisk("<application-id>", "<application-secret>", "<token>")

# Check if the token is valid
print(y.check_token())

# Get disk information
print(y.get_disk_info())

# Print files and directories at "/some/path"
print(list(y.listdir("/")))

# Upload "file_to_upload.txt" to "/destination.txt"
y.upload("yandex_webdav.py", "/backup/yandex_webdav.py")

# Same thing
# with open("file_to_upload.txt", "rb") as f:
#     y.upload(f, "/destination.txt")

# Download "/some-file-to-download.txt" to "downloaded.txt"
# y.download("/some-file-to-download.txt", "downloaded.txt")

# Permanently remove "/file-to-remove"
# y.remove("/file-to-remove", permanently=True)

# Create a new directory at "/test-dir"
print(y.mkdir("/test-dir"))