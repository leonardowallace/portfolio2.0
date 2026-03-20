
import os
import shutil
import logging
from datetime import datetime

class Exporter:
    def __init__(self, output_dir='data/output', backup_dir='data/backup'):
        self.output_dir = output_dir
        self.backup_dir = backup_dir
        
        # Garantir diretórios
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(backup_dir, exist_ok=True)

    def save(self, content, filename):
        target_path = os.path.join(self.output_dir, filename)
        
        # Backup automático antes de sobrescrever
        if os.path.exists(target_path):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = os.path.join(self.backup_dir, f"{filename}_{timestamp}.bak")
            shutil.copy2(target_path, backup_path)
            logging.info(f"Backup criado: {backup_path}")

        # Escrita do arquivo
        try:
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(content)
            logging.info(f"Arquivo salvo com sucesso: {target_path}")
        except Exception as e:
            logging.error(f"Falha ao salvar {filename}: {str(e)}")
            raise
