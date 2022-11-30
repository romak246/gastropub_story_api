from PIL import Image

from menu.models.category import Category
from menu.models.dish import Dish


class Cropper:
    def __init__(self, obj: Category | Dish):
        self.image = obj.image
        self.cropping = obj.cropping

    def get_cropped_image(self):
        try:
            Image.open(f"{self.image}"[:-3] + f"{self.cropping}.jpg")
        except FileNotFoundError:
            self.__crop_image()
        return f"{self.image}"[:-3] + f"{self.cropping}.jpg"

    def __crop_image(self):
        img = Image.open(self.image)
        crop_points = self.cropping.split(',')
        area = (int(crop_points[0]), int(crop_points[1]), int(crop_points[2]), int(crop_points[3]))
        cropped_img = img.crop(area)
        cropped_img.save(f"{self.image}"[:-3] + f"{self.cropping}.jpg")
