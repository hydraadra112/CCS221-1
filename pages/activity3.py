import streamlit as st
import numpy as np
import matplotlib as plt
import cv2

#to read images
png = str(".png")
path = str("pages/")

x = []
y = []


def translation(i,x,y):
        m_translation_ = np.float32([[1, 0, x],
                                    [0, 1, y],
                                    [0, 0, 1]
                                 ])
        
        image = cv2.imread(path + str(i) + png)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cols, rows, dims = image.shape
        
        translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
        plt.imshow(translated_image)
        plt.show()
        st.pyplot (fig)
        
        
def rotation(i):
        angle = np.radians(10)
        m_rotation = np.float32([[np.cos(angle), -(np.sin (angle)), 0],
                             [np.sin(angle), np.cos(angle), 0],
                             [0, 0, 1]])
        
        image = cv2.imread(path + str(i) + png)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cols, rows, dims = image.shape
        
        rotated_image = cv2.warpPerspective(image, m_rotation, (int(cols), int(rows)))
        plt.axis('off')
        plt.imshow(rotated_image)
        plt.show()
        st.pyplot (fig)
        
def scaling(i):
        m_scaling_ = np.float32([[1.5, 0, 100],
                            [0, 1.8, 0],
                            [0, 0, 1]
                            ])
        
        image = cv2.imread(path + str(i) + png)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cols, rows, dims = image.shape
        
        scaled_image = cv2.warpPerspective(image, m_scaling_, (cols * 2, rows * 2))
    
        plt.axis('off')
        plt.imshow(scaled_image)
        plt.show()
        st.pyplot (fig)
        
       
def shear(i):
        m_shearing_ = np.float32([[1,0, 0],
                            [0, 1, 0],
                            [0, 0, 1]
                            ])
        
        image = cv2.imread(path + str(i) + png)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cols, rows, dims = image.shape
        
        sheared_image = cv2.warpPerspective(image, m_shearing_, (int(cols * 1.5), int(rows * 1.5)))
    
        plt.axis('off')
        plt.imshow(sheared_image)
        plt.show()
        st.pyplot (fig)
       
    
def reflection(i):
        m_reflection_ = np.float32([[1, 0, 0],
                                [0, -1, rows],
                                [0, 0, 1]
                                ])
        
        image = cv2.imread(path + str(i) + png)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cols, rows, dims = image.shape
        
        reflected_image = cv2.warpPerspective(image, m_reflection_, (int(cols), int(rows)))
    
        plt.axis('off')
        plt.imshow(reflected_image)
        plt.show ()
        st.pyplot(fig)
        
       
def main ():
    st.title ("Activity 3: Image Manipulator")
    Manipulation = ["Translation", "Rotation", "Scaling", "Shear", "Reflection"]
    choice = st.sidebar.selectbox("Manipulation", Manipulation)
    
    if choice == "Translation" :
        st.subheader ("Translation")
        i = st.sidebar.slider('Choose Image (1-3)', 1, 3)
        x = st.sidebar.slider('X',0 , 300)
        st.write('Value of X: ', x)
        y = st.sidebar.slider('Y',0 , 300)
        st.write('Value of Y1: ', y)
        translation (i,x,y)
         
         
    if choice == "Rotation" :
        st.subheader ("Rotation")
                      
    if choice == "Scaling" :
        st.subheader ("Scaling")
                      
    if choice == "Shear" :
        st.subheader ("Shear")
   

    if choice == "Reflection" :
        st.subheader ("Reflection")
         
    
if __name__ == '__main__':
    main()    

