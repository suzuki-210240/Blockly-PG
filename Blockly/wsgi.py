import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise  # 注意: WhiteNoise と大文字でインポート

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blockly.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root="/home/ec2-user/Blockly-PG/staticfiles")  # WhiteNoise を使う
