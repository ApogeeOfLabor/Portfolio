import re
'''
1. Parsing Email for dict {'username': 'something_username', 'domain': 'something_domain'}
2. And validation email.
'''


def email_parse(email_address):
    try:
        pattern = re.compile(r'^(?P<username>\w+[.-_]*)@(?P<domain>\w+\.\w{2,})$')
        user_match = re.match(pattern, email_address)
        return user_match.groupdict()
    except Exception:
        raise ValueError(f'wrong email: {email_address}')


if __name__ == '__main__':
    print(email_parse('qwzsdngdhn434r3ffe@qwasde.ruqweqweqweqwe'))
