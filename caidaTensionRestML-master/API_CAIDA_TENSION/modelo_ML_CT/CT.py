from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression as lr
import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
from sklearn.metrics import r2_score as r2
import os
from scipy.optimize import curve_fit
# from sklearn.externals import joblib
#SE UTILIZA EL MODULO OPTIMIZE DE SCIPY EN VEZ DEL LINEAR_MODEL de sklearn
#dataframe
data = pd.read_excel(os.getcwd()+'/API_CAIDA_TENSION/modelo_ML_CT/'+ 'file1.xlsx' )
#data[["ct"]]=data[["ct"]]*10000

datax=data[["carga"]]
datay=data[["temp"]]
dataz=data[["ct"]]

#def func(X, a, b, c, d, e):
 #   x,y = X
  #  return a*x+ b*(y**3) +c*(y**2)+ d*y + e
# line plus sigmoid
def func(X, a, b,c,d):
    x,y = X
    return d*x+(1/a+x*np.exp(b*y))+c

# some artificially noise data to fit
x= np.linspace(5,150,len(datax.values))
y= np.linspace(10,40,len(datay.values))
print(f"x:{x} e y:{y}")
#a, b, c, d, e= 9., 3., 5.
z = dataz["ct"].values
X,Y=np.meshgrid(x,y)
# initial guesses for a,b,c:
#p0 = 0.025,-0.000217,0.016,-0.28,0.4
Z,cov=curve_fit(func, (datax["carga"].values,datay["temp"].values), z)
#print(p0,Z)
print(Z)

figure= plt.figure()
axes=plt.axes(projection="3d")
axes.scatter3D(datax["carga"].values,datay["temp"].values,z,color="blue",label="data")
axes.plot_wireframe(X,Y,func((X,Y),Z[0],Z[1],Z[2],Z[3]),color="cyan")
plt.show()
x_model=data["carga"].values.reshape(len(data["carga"]),1)
y_model=data["temp"].values.reshape(len(data["temp"]),1)
#z_model=func((x_model,y_model),Z[0],Z[1],Z[2],Z[3],Z[4])
z_model=func((x_model,y_model),Z[0],Z[1],Z[2],Z[3])
print("RSCORE:%.2f" % r2(z_model,dataz[["ct"]]))
print("MSE: %.2f" % np.sqrt(np.mean((z_model-dataz[["ct"]])**2)))
result=z_model.reshape(len(z_model),)
df_t=pd.DataFrame({"Corriente de carga":x_model.reshape(len(data["carga"]),),"temperatura":y_model.reshape(len(data["temp"]),), "CT-REAL":z, "CT-PRED":result, "INDEX":result/z})
print(df_t)

#creating class  to export

class Ct (object):
    author="manuel"
    def predict(self,corriente,temperatura):
         # expresion del modelo
        result=Z[3]*corriente+(1/Z[0]+corriente*np.exp(Z[1]*temperatura))+Z[2]
        return result

CT= Ct()
prueba=CT.predict(130,10)
print(prueba)
 # save the model to disk
# filename = 'CT_MODEL.sav'
# print("si pasa")
# joblib.dump(CT, filename)
# print("si paso")
