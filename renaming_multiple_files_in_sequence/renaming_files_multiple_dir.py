import os

path = os.getcwd()

# path to the data folder
data_path = 'D:\\Trainings-2019\\flower_recognition\\flowers-recognition\\flowers_org'
#data_dir = 'daisy'
data_dir_list = os.listdir(os.path.join(data_path))

for data_dir in data_dir_list:
    print ('Renaming files from folder: {}'.format(data_dir))
    data_list = os.listdir(os.path.join(data_path,data_dir))
    os.chdir(os.path.join(data_path,data_dir))

    # The base name of image files
    base_name=data_dir
    
    for i in range(len(data_list)):
        img_name = data_list[i]
#        img_rename = base_name + '_{}'.format(i+1)+'.png' # here the file name is base_name_1.png
        img_rename = base_name + '_{:06d}'.format(i+1)+'.png' # here the file name is base_name_000001.png
        if not os.path.exists(img_rename):
            os.rename(img_name,img_rename)
        
    print ('------Complete renaming all folders: {}------'.format(data_dir))

    os.chdir(path)

print ('----Complete renaming files from all folders----')
