# Fix _config.yml - remove alipay/wechat reward config
with open('_config.yml', 'rb') as f:
    content = f.read()

# Find the end of friends array: ...bytedance.com/zh"}
marker = b'bytedance.com/zh"}'
idx = content.find(marker)
if idx != -1:
    end = idx + len(marker)
    new_content = content[:end] + b'\n]\n'
    with open('_config.yml', 'wb') as f:
        f.write(new_content)
    print('Fixed')
else:
    print('Marker not found')
