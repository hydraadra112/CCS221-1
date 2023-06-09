
import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("1.PNG")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cols, rows, dims = image.shape

Bx_old = []
By_old = []
Tx = []
Ty = []


def translation_old(Bx_old, By_old):

        
        m_translation_ = np.float32([[1, 0, Bx_old],
                                    [0, 1, By_old],
                                    [0, 0, 1]
                                    ])
    
        translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    
        plt.axis('off')
        plt.imshow(translated_image)
        plt.show()
        

        
def translation_new(Bx_new, By_new):
    
        m_translation_ = np.float32([[1, 0, Bx_new],
                                    [0, 1, By_new],
                                    [0, 0, 1]
                                    ])
    
        translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    
        plt.axis('off')
        plt.imshow(translated_image)
        plt.show()

        
def main():

        Bx_old = int(input("Enter Initial X: "))
        By_old = int(input("Enter Initial Y: "))
        Tx = int(input("Enter Translation X: "))
        Ty = int(input("Enter Translation Y: "))
        
        Bx_new = Bx_old + Tx
        By_new = By_old + Ty
        
        translation_old(Bx_old, By_old)
        
        translation_new(Bx_new, By_new)
    
if __name__ == '__main__':
       main()