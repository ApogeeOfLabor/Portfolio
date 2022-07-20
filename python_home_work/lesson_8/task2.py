import re
import requests

pattern_list = [
    r'(^\w+(?:[.:]*\w+){1,8})',             # pattern_ip = r'^\w+(?:[.:]*\w+){1,8}'
    r'(\d{1,2}(\/\w+){2,}(:\w+)*\s\+\d+)',  # pattern_datetime = r'\[[^\[\]]*\]'
    r'\"([A-Z]{3,4})\s[^\"\s]',             # pattern_type = r'\"([A-Z]{3,4})\s[^\"\s]'
    r'\s((/\w+){2,}[^\s])\s',               # pattern_resource = r'\s((/\w+){2,}[^\s])\s'
    r'\s(\d{3})\s',                         # pattern_code = r'\s(\d{3})\s'
    r'(?<=\s\d\d\d\s)(\d+)\s[^\s]'          # pattern_size = r'(?<=\s\d\d\d\s)(\d+)\s[^\s]'
]

response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text.split('\n')

for i, line in enumerate(response):
    if line:
        response_list = [re.search(pattern, line).group(1) for pattern in pattern_list]
        print(f'- {i} -', *response_list)
