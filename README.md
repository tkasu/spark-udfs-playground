# Spark UDFs examples

This project started as a trial of creating Maturin-based Rust UDFs for Apache Spark.
However, it turned out to be my Spark UDF testing playground.

Note that the benchmarks are run within single machine, and the order of the execution impact the results
slightly. So the results are not completely deterministic, but they give some idea of the performance of the UDFs.

## Development

### Requirements

* rustup
* poetry
* jdk 11
* sbt

### Build

#### Python & Rust

```shell
poetry install
poetry run maturin develop
```

#### Scala

```shell
bash -c "cd scala/scala-udfs && sbt package"
```

### Formatting

```shell
poetry run black .
```

### Test

```shell
poetry run pytest
```

## Run (unscientific) UDF benchmarks

```shell
poetry run maturin develop --release
poetry run python -m python.spark_udfs.benchmark
```

Example output with Apple Macbook Air M1, 8GB:

```
--------------------------------------------------------------------------------
Benchmarking sqrt_and_mol -> sqrt(x) + 42
--------------------------------------------------------------------------------
native_sqrt_and_mol exec time: 0.3543, result: 237802256859.78                  
python_udf_sqrt_and_mol exec time: 15.7128, result: 237802256859.68             
python_udf_spark35arrow_sqrt_and_mol exec time: 6.1456, result: 237802256859.68 
python_arrow_udf_sqrt_and_mol exec time: 4.2768, result: 237802256859.68        
pandas_udf_sqrt_and_mol exec time: 2.5103, result: 237802256859.68              
rust_sqrt_and_mol_udf exec time: 15.7215, result: 237802256859.68               
rust_sqrt_and_mol_arrow_udf exec time: 3.7996, result: 237802256859.68          
polars_udf_sqrt_and_mol exec time: 2.4725, result: 237802256859.68              
polars_udf_sqrt_and_mol_arrow_optimized exec time: 2.6491, result: 237802256859.78
map_in_arrow_polars, exec time: 1.9444, result: 237802256859.78                 
scala_udf_sqrt_and_mol exec time: 0.4729, result: 237802256859.78
--------------------------------------------------------------------------------
Benchmarking average_crt -> avg(clicks_arr / views_arr)
--------------------------------------------------------------------------------
Warmup: sum of clicks: 674990418, sum of views: 674990418
native_average_crt exec time: 1.6229, result: 0.1216
python_udf_average_crt exec time: 2.5796, result: 0.1216
python_udf_spark35arrow_average_crt exec time: 2.9333, result: 0.1216
rust_udf_average_crt_udf exec time: 1.7411, result: 0.1216
```
