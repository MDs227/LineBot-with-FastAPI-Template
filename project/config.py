import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LINE Bot 設定
LINE_CHANNEL_SECRET = os.environ.get("83b2f1d02765902bddc2d3c005b48329")
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("DYuAmKRAkBRqRMBMxW5iy8aUaSiHeJsfKm3LRArxbSglCwhqS26PKomRAOrUXNUqCtWGSVUe4yWS85eMed2C6PyU6sh0rahw60YODevrg/1eJlNo5sTTTCmBNLp+W29ANIGhGVStHbPcf74loCOGDgdB04t89/1O/w1cDnyilFU=")
GOOGLE_API_KEY = os.environ.get('AIzaSyDO0bMFUJAH0uD20ZoByUizv3JxZt17VAE')
FIREBASE_URL = os.environ.get('https://console.firebase.google.com/u/0/project/md227-c608e/database/md227-c608e-default-rtdb/data/~2F')
