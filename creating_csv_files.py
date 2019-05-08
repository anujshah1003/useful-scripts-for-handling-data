import cv2
import os
data_path = 'flowers_renamed'
data_dir_list = os.listdir(data_path)
print ('the data list is: ',data_dir_list)

# Assigning labels to each flower category
num_classes = 5
labels_name={'daisy':0,'dandelion':1,'rose':2,'sunflower':3,'tulip':4}

train_df = pd.DataFrame(columns=['FileName', 'Label', 'ClassName'])
test_df = pd.DataFrame(columns=['FileName', 'Label', 'ClassName'])

num_images_for_test = 60

for dataset in data_dir_list:
    img_list = os.listdir(os.path.join(data_path,dataset))
    print ('Loading the images of dataset-'+'{}\n'.format(dataset))
    label = labels_name[dataset]
    num_img_files = len(img_list)
    num_corrupted_files=0
    test_list_index = random.sample(range(1, num_img_files-1), num_images_for_test)
        
    for i in range(num_img_files):
        img_name = img_list[i]
        img_filename = os.path.join(data_path,dataset,img_name)
        try:
            input_img = cv2.imread(img_filename)
            img_shape=input_img.shape
            if i in test_list_index:
                test_df = test_df.append({'FileName': img_filename, 'Label': label,'ClassName': dataset},ignore_index=True)
            else:
                train_df = train_df.append({'FileName': img_filename, 'Label': label,'ClassName': dataset},ignore_index=True)
                
        except:
            print ('{} is corrupted\n'.format(img_filename))
            num_corrupted_files+=1
    print ('Read {0} images out of {1} images from data dir {2}\n'.format(num_img_files-num_corrupted_files,num_img_files,dataset))



print ('completed reading all the image files and assigned labels accordingly')

if not os.path.exists('data_files'):
    os.mkdir('data_files')

train_df.to_csv('data_files/flower_recognition_train.csv')
test_df.to_csv('data_files/flower_recognition_test.csv')
print('The train and test csv files are saved')