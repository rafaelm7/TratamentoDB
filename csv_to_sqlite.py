import pandas as pd
import sqlite3
from pathlib import Path
import logging

def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def clean_dataframe(df):
    """Clean the dataframe by removing extra whitespace and quotes."""
    # Remove leading/trailing whitespace from all string columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()
    
    # Convert 'Valor US$ FOB' to numeric, removing any non-numeric characters
    df['Valor US$ FOB'] = pd.to_numeric(df['Valor US$ FOB'], errors='coerce')
    
    # Convert 'Ano' to numeric
    df['Ano'] = pd.to_numeric(df['Ano'], errors='coerce')
    
    return df

def create_database(csv_path, db_path):
    """
    Create SQLite database from CSV file.
    
    Parameters:
        csv_path (str): Path to the CSV file
        db_path (str): Path where the SQLite database will be created
    """
    logger = logging.getLogger(__name__)
    
    try:
        # Read CSV file
        logger.info(f"Reading CSV file: {csv_path}")
        df = pd.read_csv(csv_path, 
                        sep=';',
                        encoding='utf-8',
                        decimal=',')
        
        # Clean the dataframe
        logger.info("Cleaning data")
        df = clean_dataframe(df)
        
        # Create SQLite database
        logger.info(f"Creating SQLite database: {db_path}")
        with sqlite3.connect(db_path) as conn:
            # Create the main table
            df.to_sql('comercio_exterior', 
                     conn, 
                     if_exists='replace',
                     index=False,
                     dtype={
                         'Fluxo': 'TEXT',
                         'Ano': 'INTEGER',
                         'Países': 'TEXT',
                         'UF do Produto': 'TEXT',
                         'URF': 'TEXT',
                         'Código Seção': 'TEXT',
                         'Descrição Seção': 'TEXT',
                         'Via': 'TEXT',
                         'Código SH6': 'TEXT',
                         'Descrição SH6': 'TEXT',
                         'Valor US$ FOB': 'REAL'
                     })
            
            # Create indexes for better query performance
            logger.info("Creating indexes")
            conn.execute('CREATE INDEX idx_ano ON comercio_exterior(Ano)')
            conn.execute('CREATE INDEX idx_pais ON comercio_exterior(Países)')
            conn.execute('CREATE INDEX idx_uf ON comercio_exterior("UF do Produto")')
            conn.execute('CREATE INDEX idx_codigo_sh6 ON comercio_exterior("Código SH6")')
            
        logger.info("Database creation completed successfully")
        
    except Exception as e:
        logger.error(f"Error creating database: {str(e)}")
        raise

def main():
    """Main function to execute the database creation process."""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Define paths
    current_dir = Path.cwd()
    csv_file = current_dir / "V_EXPORTACAO_E IMPORTACAO_GERAL_2018-01_2023-12_DT20241127.csv"
    db_file = current_dir / "comercio_exterior.db"
    
    try:
        create_database(csv_file, db_file)
        logger.info(f"Database created successfully at {db_file}")
    except Exception as e:
        logger.error(f"Failed to create database: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())