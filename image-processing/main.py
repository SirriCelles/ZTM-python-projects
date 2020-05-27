
import images

image_list = ['./pokydex/pikachu.jpg', './pokydex/squirtle.jpg', './pokydex/bulbasaur.jpg']



if __name__ == '__main__':
    images.display_img(image_list)
    print('\n')
    images.convert_img()
    print('\n')
    images.get_filters("./pokydex/squirtle.jpg")



