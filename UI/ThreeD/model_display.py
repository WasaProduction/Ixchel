#   https://stackoverflow.com/questions/62949006/how-to-load-obj-file-to-pyopengl
#   https://nrotella.github.io/journal/first-steps-python-qt-opengl.html
#   https://stackoverflow.com/questions/64398984/opengl-how-to-show-obj-models-while-having-a-jpg-as-a-background
#   https://www.youtube.com/watch?v=zi8-XFTR-Sc
#   https://stackoverflow.com/questions/38280057/how-to-integrate-pygame-and-pyqt4
#   https://www.youtube.com/watch?v=DKt4HRBqH1I
"""
#'/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/threed_models/cube.obj', strict=True, encoding="iso-8859-1", parse=False
#'/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/threed_models/test.jpg'
"""
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
from assimp_py import *
import assimp_py


class OpenGLWidget(QOpenGLWidget):
    def __init__(self, model_paths, texture_paths, parent=None):
        super().__init__(parent)
        self.models = []
        self.rotation_angle = 0
        self.camera_distance = 5.0
        self.model_paths = model_paths
        self.texture_paths = texture_paths
        self.textures = []

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glClearColor(0.5, 0.4, 0.6, 1.0)  # Gray with a hint of blue

        for model_path, texture_path in zip(self.model_paths, self.texture_paths):
            self.load_model(model_path, texture_path)

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect_ratio = width / height
        gluPerspective(45.0, aspect_ratio, 0.1, 100.0)  # Apply perspective projection
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0.0, 0.0, -self.camera_distance)
        glRotatef(self.rotation_angle, 0.0, 1.0, 0.0)  # Rotate around the Y-axis

        for model, texture in zip(self.models, self.textures):
            self.draw_model(model, texture)

    def draw_model(self, model, texture):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture)
        for mesh in model.meshes:
            for face in mesh.faces:
                glBegin(GL_TRIANGLES)
                for vertex in face:
                    vertex_pos = model.vertices[vertex[0]]
                    vertex_tex = model.texturecoords[vertex[1]]
                    glTexCoord2f(vertex_tex[0], vertex_tex[1])
                    glVertex3f(vertex_pos[0], vertex_pos[1], vertex_pos[2])
                glEnd()
        glDisable(GL_TEXTURE_2D)

    def load_model(self, model_path, texture_path):
        try:
            assimp_py.
            scene = pyassimp.load(model_path)
            if scene.meshes:
                self.models.append(scene.meshes[0])  # Assuming there's only one mesh per model
                texture = glGenTextures(1)
                glBindTexture(GL_TEXTURE_2D, texture)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
                image = pyassimp.image_load(texture_path)
                if image:
                    glTexImage2D(
                        GL_TEXTURE_2D, 0, GL_RGBA,
                        image.width, image.height, 0,
                        GL_RGBA, GL_UNSIGNED_BYTE, np.array(image)
                    )
                    self.textures.append(texture)
        except Exception as e:
            print(f"Model loading failed: {e}")

    def rotate_left(self):
        self.rotation_angle += 10
        self.update()

    def rotate_right(self):
        self.rotation_angle -= 10
        self.update()

class ModelViewer(QWidget):
    def __init__(self, model_paths, texture_paths):
        super().__init__()
        self.initUI(model_paths, texture_paths)

    def initUI(self, model_paths=None, texture_paths=None):
        model_paths = ['/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/threed_models/wooden_sphere.obj']
        mtl_paths = ['/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/threed_models/wooden_sphere.mtl']

        layout = QVBoxLayout(self)
        self.opengl_widget = OpenGLWidget(model_paths, texture_paths)
        layout.addWidget(self.opengl_widget)

        button_layout = QHBoxLayout()
        rotate_left_button = QPushButton("Rotate Left")
        rotate_right_button = QPushButton("Rotate Right")

        rotate_left_button.clicked.connect(self.opengl_widget.rotate_left)
        rotate_right_button.clicked.connect(self.opengl_widget.rotate_right)

        button_layout.addWidget(rotate_left_button)
        button_layout.addWidget(rotate_right_button)
        layout.addLayout(button_layout)



