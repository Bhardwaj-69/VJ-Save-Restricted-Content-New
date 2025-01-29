import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7339888650:AAGCOGVV1VdZoWih8bc3-shOWD2HWQ-L8T8")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27392387"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "37ee47c18c8be62716a27335a771e7da")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5787359348"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mihaja5084:yeIh95RrMkRNZ3It@cluster0.6voc3fm.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
