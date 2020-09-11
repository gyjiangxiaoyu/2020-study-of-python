#!"C:\Users\PCSetupAccount\Desktop\知识沉淀\拷贝走的个人资料\leetcode 打卡\venv\Scripts\python.exe" -x
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==9.0.3','console_scripts','pip'
__requires__ = 'pip==9.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==9.0.3', 'console_scripts', 'pip')()
    )
