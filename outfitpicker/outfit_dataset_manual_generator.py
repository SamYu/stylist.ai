import pandas as pd
import random
import csv
from IPython.display import Image, display
from IPython.core.display import HTML 

GENDER = 'Men'

def get_random_clothes_id_list(df):
    clothes_list = []
    jackets = df[df['articleType'] == 'Jackets'].sample(n=1)
    top = df[df['subCategory'] == 'Topwear'].sample(n=1)
    bottom = df[df['subCategory'] == 'Bottomwear'].sample(n=1)
    shoe = df[df['masterCategory'] == 'Footwear'].sample(n=1)
    accessory = df[df['masterCategory'] == 'Accessories'].sample(n=1)
    clothes_list.append(top.index.values[0])
    clothes_list.append(bottom.index.values[0])
    clothes_list.append(shoe.index.values[0])
    clothes_list.append(accessory.index.values[0])
    if (random.choice([0, 1]) == 1):
        jacket = jackets.sample(n=1)
        clothes_list.append(jacket.index.values[0])
    return clothes_list

def get_image_url_by_id(id):
    imdf = pd.read_csv('images.csv', error_bad_lines=False)
    row = imdf[imdf['filename'] == (str(id) + '.jpg')]['link'].values
    if (len(row) >= 1):
      return row[0]
    else:
      return ''

def generate_n_outfits(csv_file, output_file, num):
    df = pd.read_csv(csv_file, index_col=['id'], error_bad_lines=False)
    df = df[df['gender'] == GENDER]
    with open(output_file, mode='w') as outfit_data:
      outfit_writer = csv.writer(outfit_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      outfit_writer.writerow(['id', 'clothes_ids', 'rating'])
      for i in range(num):
          outfit_id = i
          clothes_id_list = get_random_clothes_id_list(df)
          for clothing_id in clothes_id_list:
              clothing = df.loc[clothing_id]
              url = get_image_url_by_id(clothing_id)
              print(url)
              image = Image(url=url, width=100, height=100)
              display(image)
              print("Name: " + clothing['productDisplayName'] + " | Color: " + clothing['baseColour'] + " | Type: " + clothing['subCategory'])
          rating = input("Type the Rating (1/10): ")
          while (not (1 <= int(rating) <= 10)):
            print('Error, please enter a rating between 1 and 10')
            rating = input("Type the Rating (1/10): ")
          outfit_writer.writerow([outfit_id, str(clothes_id_list)[1 : -1], rating])

generate_n_outfits('clothes_data.csv', 'output_data.csv', 100)
