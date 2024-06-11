import os
import sys
from src.utils.logger import logging
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_data_path: Path

@dataclass
class DataPreparationConfig:
    data_path: Path

@dataclass
class ModelTrainingConfig:
    cleaned_data_path: Path
    split_ratio: float

@dataclass
class ModelPredictionConfig:
    model_path: Path
    test_data_path: Path