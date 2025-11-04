import pandas as pd
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    find_patients = patients[patients['conditions'].str.contains(r'(^| )DIAB1')]
    return find_patients