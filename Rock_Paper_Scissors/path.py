import os

for i in range(1, 150):
    file_path = f'paper_{i}.xml'
    if not os.path.exists(file_path):
        continue

    with open(f'paper_{i}.xml', 'r') as file:
        data = file.readlines()

    #'\t<path>E:\\Kaggle\\Project_1\\Rock_Paper_Scissors\\data\\paper\\1.jpg</path>\n'
    data[3] = f'\t<path>/content/training/images5/train/paper_{i}.jpg</path>\n'
    data[1] = f'\t<folder>images5</folder>\n'
    data[2] = f'\t<filename>paper_{i}.jpg</filename>\n'

    with open(f'paper_{i}.xml', 'w') as file:
        file.writelines(data)

for i in range(1, 150):
    file_path = f'rock_{i}.xml'
    if not os.path.exists(file_path):
        continue

    with open(f'rock_{i}.xml', 'r') as file:
        data = file.readlines()

    #'\t<path>E:\\Kaggle\\Project_1\\Rock_Paper_Scissors\\data\\rock\\1.jpg</path>\n'
    data[3] = f'\t<path>/content/training/images5/train/rock_{i}.jpg</path>\n'
    data[1] = f'\t<folder>images5</folder>\n'
    data[2] = f'\t<filename>rock_{i}.jpg</filename>\n'

    with open(f'rock_{i}.xml', 'w') as file:
        file.writelines(data)

for i in range(1, 150):
    file_path = f'scissors_{i}.xml'
    if not os.path.exists(file_path):
        continue

    with open(f'scissors_{i}.xml', 'r') as file:
        data = file.readlines()

    #'\t<path>E:\\Kaggle\\Project_1\\Rock_Paper_Scissors\\data\\scissors\\1.jpg</path>\n'
    data[3] = f'\t<path>/content/training/images5/train/scissors_{i}.jpg</path>\n'
    data[1] = f'\t<folder>images5</folder>\n'
    data[2] = f'\t<filename>scissors_{i}.jpg</filename>\n'

    with open(f'scissors_{i}.xml', 'w') as file:
        file.writelines(data)


