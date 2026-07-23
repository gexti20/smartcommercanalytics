#componente matematico aislado que va realizar los calculos de la estimación del inventario futuro
import pandas as pd
import numpy as np

#Crear la clase principal del motor de prediccion
class   MotorPrediccion:
    """Este es el componente analitico para calcular la demanda futura del inventario"""
    def __init__(self,incremento_simulado=0.15):
        self.incremento = incremento_simulado


    def predecir_demanda(self, df_historico: pd.DataFrame) -> pd.DataFrame:
        """
        Toma los datos historicos y estima el stock necesario para el proximo mes
        logica del componente aislada del UI
        """
        if df_historico.empty:
            return pd.DataFrame()

        #Agrupamos por producto para ver el promedio de ventas mensuales
        ventas_promedio =df_historico.groupby('producto')['cantidad'].mean().reset_index()

        #Aplicamos la formula matematica de stock sugerida(demanda + margen de seguridad)
        ventas_promedio['stock_sugerido'] = np.ceil(ventas_promedio['cantidad'] * (1 + self.incremento)).astype(int)
        ventas_promedio.rename(columns={'cantidad': 'promedio historico'}, inplace=True)
        return round(ventas_promedio, 2)