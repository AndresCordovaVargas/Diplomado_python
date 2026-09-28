import numpy as np
import pandas as pd
from sklearn.dummy import dummyRegressor
from sklearn.linear_model import LinearRegression
from aklearn.metrics import mean_adsolute_error, mean_equared_error, r2_score
from sklear.model_selection import train_test_split

df = pd.read_csv("viviendas_reto.csv")

print("Exploracion Inicial")
print(df.head(),"\n")
print(df.info(),"\n")
print(df.describe(),"\n")
# Definir X
X = df[["metros", "habitaciones", "baños", "antiguedad", "distancia_centro"]]

# 3. Definir y 
# Seleccionamos la variable objetivo que queremos predecir
y = df["precio"]

# 4. Separar Train/Test

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# 5. Entrenar LinearRegression 
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

# 10. Baseline (DummyRegressor) 
# Usamos la estrategia de la media (predice siempre el promedio del precio)
model_dummy = DummyRegressor(strategy="mean")
model_dummy.fit(X_train, y_train)

# 6. Generar predicciones
pred_lr = model_lr.predict(X_test)
pred_dummy = model_dummy.predict(X_test)

# Funciones para calcular métricas (7, 8, 9) 
def evaluar_modelo(y_true, y_pred, nombre):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    print(f"--- Métricas: {nombre} ---")
    print(f"MAE  (Error Absoluto Medio): {mae:.2f}")
    print(f"RMSE (Raíz del Error Cuadrático Medio): {rmse:.2f}")
    print(f"R²   (Coeficiente de Determinación): {r2:.4f}\n")


# 7, 8, 9 y 10. Comparar contra el baseline 
evaluar_modelo(y_test, pred_lr, "Linear Regression")
evaluar_modelo(y_test, pred_dummy, "Dummy Regressor (Baseline)")

