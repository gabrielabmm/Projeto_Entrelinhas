# POC01 — Codeforces
Objetivo: testar perfil, últimas 100 submissões, histórico de rating e catálogo de busca binária.
## Execução
Na pasta desta POC:
```bash
python -m venv .venv
```
Windows PowerShell: `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` e `.\.venv\Scripts\python.exe main.py`.
Linux: `.venv/bin/python -m pip install -r requirements.txt` e `.venv/bin/python main.py`.
Informe um handle público. Cinco JSONs serão gravados em data/ (ignorado pelo Git).
## Testes reais pendentes
- [ ] CT01 perfil válido
- [ ] CT02 perfil inexistente
- [ ] CT03 submissões
- [ ] CT04 rating (inclusive vazio)
- [ ] CT05 catálogo
- [ ] CT06 problemas únicos
- [ ] CT07 intervalo entre requisições
- [ ] CT08 falha de conexão
- [ ] CT09 paginação (inicio=101)
- [ ] CT10 cinco JSONs
## Limitações
Amostra de 100 submissões, não histórico completo. Identidade de problemas experimental; não há banco, sincronização incremental, titularidade ou estimativa de domínio. Controle sequencial. API real não testada na preparação do pacote.
