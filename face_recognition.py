# example of face detection with mtcnn
from matplotlib import pyplot
from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN

def find_face(file):
    filename = '8_peop.jpg'
    photo = pyplot.imread(filename)
    detector = MTCNN()
    faces = detector.detect_faces(photo)
    return faces
