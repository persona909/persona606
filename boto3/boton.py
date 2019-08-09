# -*- coding: utf-8 -*-
import boto3
import logging
import datetime

#access_key = getpass.getpass('         アクセスキー ID:')
#secret_key = getpass.getpass('シークレットアクセスキー:')
#s3 = boto3.client('s3',
#                  aws_access_key_id=[access_key],
#                  aws_secret_access_key=[secret_key],
#                  region_name=''
#                 )
#S3初期設定
s3 = boto3.resource('s3')
#ログ出力名を設定
logger = logging.getLogger('Connecrt_120')

# ログレベルの設定（2）
logger.setLevel(10)

# ログのコンソール出力の設定（3）
sh = logging.StreamHandler()
logger.addHandler(sh)

# ログのファイル出力先を設定（4）
fh = logging.FileHandler('test.log')
logger.addHandler(fh)

logger.log(20, 'info')

19
20
21
22
import logging

# ログの出力名を設定（1）
logger = logging.getLogger('LoggingTest')

# ログレベルの設定（2）
logger.setLevel(10)

# ログのコンソール出力の設定（3）
sh = logging.StreamHandler()
logger.addHandler(sh)

# ログのファイル出力先を設定（4）
fh = logging.FileHandler('test.log')
logger.addHandler(fh)

logger.log(20, 'info')
logger.log(30, 'warning')
logger.log(100, 'test')

bucket = s3.Bucket('test-basket-suzuki')
bucket.upload_file('test.log', 'test.log')