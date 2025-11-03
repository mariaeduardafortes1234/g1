import requests
from bs4 import BeautifulSoup

def manchete_do_dia():
    # Usando site de comparação de preços (mais estável)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive'
    }
    url = "https://g1.globo.com/fantastico/noticia/2025/11/02/exclusivo-fuzis-feitos-em-fabricas-clandestinas-de-sp-e-mg-abastecem-o-comando-vermelho-no-rio.ghtml"
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Buscar primeiro resultado
        # Buscar span que está dentro de h2 com aquela classe
      #   manchete = soup.select_one('h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal span')
        # manchete = soup.find('span', class_='a-size-base-plus')
        manchete = soup.find('span', class_='acontent-head__title')
        
        if manchete :
            # print(f"📱 {produto.text.strip()}")
            print(f"📰  {manchete.text.strip()}")
        else:
            print("🔍 Manchete não encontrado")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

manchete_do_dia()