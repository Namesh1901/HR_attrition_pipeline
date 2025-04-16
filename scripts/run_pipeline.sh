#!/bin/bash
dbt run
py -m ../ml_pipeline/random_forest.py
