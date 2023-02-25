import os
import shutil


os.environ['COMMITS_DIR'] = './tests/commits'
shutil.rmtree('./tests/commits')
os.makedirs('./tests/commits')
