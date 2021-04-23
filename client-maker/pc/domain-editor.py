# Special thanks to Matcool for the gist he provided. you can check him out here: https://github.com/matcool
# NOTE: although this will be automated in stable release 1.0.0, I HIGHLY suggest you run this script manually.

from base64 import b64encode
from os import path

url = input('Input your gdps url (without the / at the end). Reference:\nhttp://www.boomlings.com\nhttp://www.boomlings.com/database\n')
to_replace = 'http://www.boomlings.com'

while len(url) != 24 and len(url) != 33:
    print(f'wrong size ({len(url)}), needs to be either 24 or 33')
    url = input()

if len(url) > 24:
    print('url longer than http://www.boomlings.com, using /database')
    to_replace = 'http://www.boomlings.com/database'

print('Checking base64...')

replace_b64 = b64encode(bytes(to_replace, 'utf-8'))
url_b64 = b64encode(bytes(url, 'utf-8'))
print(f'{replace_b64}\n{url_b64}')

if len(replace_b64) != len(url_b64):
    print('base64 size does not match up... somehow\nexiting')
    exit()

gd = 'GeometryDash.exe'
while not path.isfile(gd):
    gd = input(f'{gd} not found, input gd exe path: ')

output = input('output exe path: ')
print(f'Opening {gd} ...')
with open(gd, 'rb') as file:
    print('opened')
    raw = file.read()

print('replacing...')
raw = raw.replace(bytes(to_replace, 'utf-8'), bytes(url, 'utf-8')).replace(replace_b64, url_b64)

print('writing...')
with open(output, 'wb') as file:
    file.write(raw)
print('done!')
