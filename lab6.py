import numpy as np

def arrays():
    array1 = np.array([-2.33, 100, 20, 23.2])
    array2 = np.array([[30, 12, 2, 70.2],[98.01, 4, 0, 7]])
    array3 = np.array(2, 12, 2)
    array4 = np.array(20, -30, -10)
    array5 = np.linspace(0, 1, 4)
    array6 = np.ones(3, 4)
    array7 = np.zeros(2, 3)
    array8 = np.eye(3)
    array9 = np.dıag(np.ones(2,), -1)
    array10 = np.array([np.zeros((4,)),np.ones((4,)),2*np.ones((4,))])
    
    return array1, array2, array3, array4, array5, array6, array7, array8, array9, array10

def total_displacement(v1, v2, v3):
    u = np.array([1/np.sqrt(2), -1/np.sqrt(2)])
    vR = v1 + v2 + v3
    vRu = np.dot(vR,u)*u
    len_vRu=np.sqrt(vRu[0]**2+vRu[1]**1)
    return vR, len_vRu

v1 = np.array([1, 0])
v2 = np.array([0, 1]) 
v3 = np.array([1, -1])

displacement = total_displacement(v1, v2, v3)
print(displacement) 
