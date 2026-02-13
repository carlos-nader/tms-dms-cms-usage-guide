import requests
from datetime import datetime
import sys
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# ===== CONFIGURAÇÃO =====
WAKATIME_API_KEY = os.getenv("WAKATIME_API_KEY")
PROJECT_NAME = "projeto-bms"
BRANCH_NAME = "main"

# Validação
if not WAKATIME_API_KEY:
    print("❌ Erro: WAKATIME_API_KEY não encontrada!")
    print("Crie o arquivo scripts/.env com sua chave.")
    sys.exit(1)

# Categorias do WakaTime
CATEGORIES = [
    "coding", "building", "debugging", "running tests", "browsing",
    "code reviewing", "designing", "indexing", "manual testing",
    "writing tests", "writing docs", "researching", "learning",
    "planning", "meeting", "translating", "communicating",
    "advising", "supporting", "configuring", "animating",
    "ai coding", "notes"
]

CATEGORY_DISPLAY = [
    "Coding", "Building", "Debugging", "Running tests", "Browsing",
    "Code reviewing", "Designing", "Indexing", "Manual testing",
    "Writing tests", "Writing docs", "Researching", "Learning",
    "Planning", "Meeting", "Translating", "Communicating",
    "Advising", "Supporting", "Configuring", "Animating",
    "AI coding", "Notes"
]

# Linguagens do seu projeto
LANGUAGES = ["HTML", "Markdown", "TeX", "Python", "YAML", "JSON", "Text", "Git", "Other"]

# ===== FUNÇÕES =====
def show_menu(title, options):
    """Exibe menu numerado e retorna escolha"""
    print(f"\n=== {title} ===")
    
    # Calcula quantas colunas (2 colunas para melhor visualização)
    half = (len(options) + 1) // 2
    
    for i in range(half):
        left_num = i + 1
        left_item = f"{left_num:2d}. {options[i]}"
        
        right_num = i + half + 1
        if right_num <= len(options):
            right_item = f"{right_num:2d}. {options[i + half]}"
            print(f"{left_item:30s}  {right_item}")
        else:
            print(left_item)
    
    while True:
        try:
            choice = int(input(f"\nDigite o número (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                return choice - 1
            else:
                print(f"❌ Escolha um número entre 1 e {len(options)}")
        except ValueError:
            print("❌ Digite apenas o número!")

def parse_time(time_str):
    """Converte string de horário (HH:MM ou YYYY-MM-DD HH:MM) para timestamp UNIX"""
    try:
        # Tenta formato completo primeiro
        if len(time_str) > 10:
            dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        else:
            # Assume hoje se só horário for fornecido
            today = datetime.now().strftime("%Y-%m-%d")
            dt = datetime.strptime(f"{today} {time_str}", "%Y-%m-%d %H:%M")
        return int(dt.timestamp())
    except ValueError:
        print(f"❌ Erro: Formato de horário inválido '{time_str}'")
        print("Use: HH:MM ou YYYY-MM-DD HH:MM")
        sys.exit(1)

def send_to_wakatime(start_time, end_time, category, language, file_entity):
    """Envia duração externa para WakaTime"""
    
    # Gera um ID único baseado no timestamp de início
    external_id = f"perplexity-{start_time}"
    
    # Monta o payload
    payload = {
        "external_id": external_id,
        "entity": file_entity,
        "type": "app",
        "category": category,
        "language": language,
        "branch": BRANCH_NAME,
        "project": PROJECT_NAME,
        "start_time": start_time,
        "end_time": end_time
    }
    
    # Headers da requisição
    headers = {
        "Authorization": f"Bearer {WAKATIME_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # URL da API
    url = "https://api.wakatime.com/api/v1/users/current/external_durations"
    
    # Envia requisição
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 201:
            duration_hours = (end_time - start_time) / 3600
            print(f"\n✅ Sucesso! Duração registrada: {duration_hours:.2f}h")
            print(f"   Projeto: {PROJECT_NAME}")
            print(f"   Branch: {BRANCH_NAME}")
            print(f"   Categoria: {category}")
            print(f"   Linguagem: {language}")
            print(f"   Descrição: {file_entity}")
            return True
        else:
            print(f"\n❌ Erro {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Erro de conexão: {e}")
        return False

# ===== MAIN =====
if __name__ == "__main__":
    print("=" * 60)
    print("  WakaTime Time Tracker - Perplexity AI Sessions")
    print("=" * 60)
    
    # 1. Horários
    print("\n📅 Formato de horário: HH:MM (ex: 14:30) ou YYYY-MM-DD HH:MM")
    start_str = input("Horário de início: ").strip()
    end_str = input("Horário de fim: ").strip()
    
    # Converte para timestamps
    start_time = parse_time(start_str)
    end_time = parse_time(end_str)
    
    # Valida
    if end_time <= start_time:
        print("❌ Erro: Horário de fim deve ser depois do início!")
        sys.exit(1)
    
    # 2. Categoria
    category_idx = show_menu("Escolha a Categoria", CATEGORY_DISPLAY)
    category = CATEGORIES[category_idx]
    
    # 3. Linguagem
    language_idx = show_menu("Escolha a Linguagem", LANGUAGES)
    language = LANGUAGES[language_idx]
    
    # 4. Descrição
    print("\n=== Descrição da Atividade ===")
    file_entity = input("Descrição (aparece como 'File' no WakaTime): ").strip()
    
    if not file_entity:
        file_entity = "Perplexity AI Assistant"
    
    # Confirmação
    duration_hours = (end_time - start_time) / 3600
    print("\n" + "=" * 60)
    print("📋 RESUMO DA SESSÃO")
    print("=" * 60)
    print(f"Duração: {duration_hours:.2f}h")
    print(f"Categoria: {CATEGORY_DISPLAY[category_idx]}")
    print(f"Linguagem: {language}")
    print(f"Descrição: {file_entity}")
    print(f"Projeto: {PROJECT_NAME}")
    print(f"Branch: {BRANCH_NAME}")
    print("=" * 60)
    
    confirm = input("\n✅ Enviar para WakaTime? (s/n): ").strip().lower()
    if confirm == 's':
        print("\nEnviando para WakaTime...")
        send_to_wakatime(start_time, end_time, category, language, file_entity)
    else:
        print("❌ Cancelado pelo usuário.")
