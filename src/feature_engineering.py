"""
feature_engineering.py
Simple feature engineering utilities for demo project.
"""
import pandas as pd

def build_gene_level_features(ngs_df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts NGS variant data into patient-level gene count features.
    Each row represents a patient, each column a gene, and values are counts of variants per gene.
    Args:
        ngs_df (pd.DataFrame): Input DataFrame with columns ['patient_id', 'gene', 'variant']
    Returns:
        pd.DataFrame: Patient-level gene count feature matrix (index: patient_id, columns: genes)
    """
    gene_counts = ngs_df.groupby(['patient_id', 'gene']).size().unstack(fill_value=0)
    return gene_counts
