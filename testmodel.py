# make a prediction for a new image.
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np

# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(32, 32))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 32, 32, 3)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img


# load an image and predict the class
def run_example():
    classes = ['airplane','automobile','bird', 'cat', 'deer','dog','frog','horse','ship','truck']
    # load the image
    img = load_image('sample_image.png')
    # load model
    # model = load_model('media/cnnModel.h5')
    # # predict the class
    # result = model.predict(img)
    model = load_model('media/final_model.h5')
    # predict the class
    result = model.predict(img)
    print("Predicted class Index:",result[0].argmax())
    rstlt = classes[np.argmax(result[0])]
    print("Result:",rstlt)

# entry point, run the example
run_example()