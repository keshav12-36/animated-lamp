import os
from pathlib import Path

class Config:
    
    API_ID = os.environ.get('1039030')
    API_HASH = os.environ.get('725797d62aca2512897545f93ce91f00')
    BOT_TOKEN = os.environ.get('826251513:AAFjJvHqVMYYOU6DAs1FoR36Nw1TVtL7udc')
    SESSION_NAME = os.environ.get('@rokulu_bot')
    LOG_CHANNEL = os.environ.get('-34643225798')
    DATABASE_URL = os.environ.get('DATABASE_URL')
    AUTH_USERS = [int(i) for i in os.environ.get('57887435', '').split(' ')]
    MAX_PROCESSES_PER_USER = int(os.environ.get('MAX_PROCESSES_PER_USER', 2))
    MAX_TRIM_DURATION = int(os.environ.get('MAX_TRIM_DURATION', 600))
    TRACK_CHANNEL = os.environ.get('TRACK_CHANNEL', False)
    SLOW_SPEED_DELAY = os.environ.get('SLOW_SPEED_DELAY', 15)
    HOST = os.environ.get('HOST', '')
    
    SCRST_OP_FLDR = Path('screenshots/')
    SMPL_OP_FLDR = Path('samples/')
    THUMB_OP_FLDR = Path('thumbnails/')
    COLORS = ['white', 'black', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'gold', 'silver', 'pink']
    FONT_SIZES_NAME = ['Small', 'Medium', 'Large']
    FONT_SIZES = [30, 40, 50]
