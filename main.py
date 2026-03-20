
import logging
import os
from config.settings import CONFIG
from src.processor import PortfolioGenerator
from src.exporter import Exporter

# Garantir diretório de logs
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configuração de Logs
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    try:
        logging.info("Iniciando geração do portfólio para: " + CONFIG['personal']['name'])
        
        # 1. Instanciar Gerador
        generator = PortfolioGenerator(CONFIG)
        
        # 2. Processar HTML e CSS
        html_content = generator.generate_html()
        css_content = generator.generate_css()
        
        # 3. Exportar resultados
        exporter = Exporter()
        exporter.save(html_content, 'index.html')
        exporter.save(css_content, 'index.css')
        
        logging.info("Portfólio gerado com sucesso em data/output/")
        print("✅ Portfólio gerado com sucesso em data/output/")
        
    except Exception as e:
        logging.error(f"Erro crírico durante a geração: {str(e)}")
        print(f"❌ Erro: {str(e)}")

if __name__ == "__main__":
    main()
