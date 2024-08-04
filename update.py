import re
from datetime import datetime
import pytz
with open('README.md', 'r', encoding='utf-8') as file:
    data = file.read()
updated_data = re.sub(r'\d{2}:\d{2}:\d{2} \d{4}-\d{2}-\d{2}', datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%H:%M:%S %Y-%m-%d'), data)
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(updated_data)
print('File has been updated')
