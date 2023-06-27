from typing import List

import pandas as pd
from pyspark.sql.functions import udf, pandas_udf

from spark_rust_udfs import average_crt, sqrt_and_mol


@udf("float")
def rust_sqrt_and_mol_udf(value: int) -> float:
    return sqrt_and_mol(value)


@pandas_udf("float")
def rust_sqrt_and_mol_arrow_udf(value: pd.Series) -> pd.Series:
    return value.apply(sqrt_and_mol)


@udf("float")
def rust_average_crt_udf(clicks: List[int], views: List[int]) -> float:
    return average_crt(clicks, views)
