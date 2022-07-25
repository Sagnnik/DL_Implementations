import os

for i in range(1,157):
    old_img = f'{i}.jpg'
    old_xml = f'{i}.xml'

    if not os.path.exists(old_img):
        continue

    else:
        new_img = f'scissors_{i}.jpg'
        new_xml = f'scissors_{i}.xml'
        os.rename(old_img, new_img)
        os.rename(old_xml, new_xml)