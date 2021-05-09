""""
Formule possibili per indici Rt tra cui quella utilizzata dall'ISS
https://covid19.infn.it/sommario/rt-info.html

ISS calcola Rt solo sui casi sintomatici, ma non presenti nei dati della Protezione Civile
(ci sono i ricoverati con sintomi)
https://www.iss.it/coronavirus/-/asset_publisher/1SRKHcCJJQ7E/content/faq-sul-calcolo-del-rt
"""
from collections import deque
import math
import numpy as np
import pandas as pd


def rt_rki(smoothed_new_positives: pd.Series) -> pd.Series:
    """
    L'istituto RKI, Robert Koch Institut, calcola  come il rapporto tra la somma del numero di contagiati
    negli ultimi 4 giorni e la somma del numero dei contagiati nei 4 giorni precedenti.
    :param smoothed_new_positives: nuovi positivi giornalieri smoothed
    :return: serie Rt calcolate con formula RKI
    """
    last_8_days = deque(maxlen=8)

    rt_values = dict()

    for index, new_daily_positives_value in smoothed_new_positives.items():
        # print(f"Nuovi positivi smoothed: {new_daily_positives}")
        # Discard NaN at the beginning
        if math.isnan(new_daily_positives_value) is False:
            last_8_days.append(new_daily_positives_value)
        # Then start to calculate Rt e shift deque
        if len(last_8_days) == last_8_days.maxlen:
            rt = np.sum(list(last_8_days)[4:]) / np.sum(list(last_8_days)[:4])
            # Print debug
            # print(f"Sum last 4 days: {np.sum(list(last_8_days)[4:]) }")
            # print(f"Sum last 5-8 days: {np.sum(list(last_8_days)[:4])}")
            # print(f"Rt RKI: {rt}")
            # We want x value of the latest day
            rt_values[index] = rt
        else:
            rt_values[index] = np.nan

    # Return the new series
    return pd.Series(rt_values)


if __name__ == "__main__":
    import os
    prociv_repo_dir = "/home/michele/Covid/prociv-covid"

    # Manual tests
    # andamento_nazionale_csv = os.path.join(prociv_repo_dir,
    #                                        "dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
    # andamento_nazionale = pd.read_csv(andamento_nazionale_csv, parse_dates=[0])
    # andamento_nazionale['nuovi_positivi_mov_avg'] = andamento_nazionale['nuovi_positivi'].rolling(7).mean()
    # series_nazionale = rt_rki(andamento_nazionale['nuovi_positivi_mov_avg'])
    # print(series_nazionale)

    dati_regioni_csv = os.path.join(prociv_repo_dir, "dati-regioni/dpc-covid19-ita-regioni.csv")
    andamento_regioni = pd.read_csv(dati_regioni_csv, parse_dates=[0])
    andamento_regionale = andamento_regioni[andamento_regioni["denominazione_regione"] == "Toscana"]
    andamento_regionale['nuovi_positivi_mov_avg'] = andamento_regionale['nuovi_positivi'].rolling(7).mean()
    andamento_regionale['rt_rki'] = rt_rki(andamento_regionale['nuovi_positivi_mov_avg'])
    print(andamento_regionale['rt_rki'])
