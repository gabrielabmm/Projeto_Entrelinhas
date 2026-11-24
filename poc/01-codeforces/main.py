import requests
import time
import json
from collections import Counter
from pathlib import Path

BASE_URL = "https://codeforces.com/api"
ultima_requisicao = 0

def consultar_api(metodo, parametros=None):
    global ultima_requisicao
    intervalo = time.monotonic() - ultima_requisicao
    if intervalo < 2.1:
        time.sleep(2.1 - intervalo)
    ultima_requisicao = time.monotonic()
    resposta = requests.get(f"{BASE_URL}/{metodo}", params=parametros, timeout=30)
    dados = resposta.json()
    if dados.get("status") != "OK":
        raise ValueError(dados.get("comment", "Erro desconhecido"))
    resposta.raise_for_status()
    return dados["result"]

def obter_perfil(handle):
    return consultar_api("user.info", {"handles": handle})[0]

def obter_submissoes(handle, inicio=1, quantidade=100):
    return consultar_api("user.status", {"handle": handle, "from": inicio, "count": quantidade})

def obter_rating(handle):
    return consultar_api("user.rating", {"handle": handle})

def obter_problemas():
    return consultar_api("problemset.problems", {"tags": "binary search"})["problems"]

def analisar_submissoes(submissoes):
    resolvidos, tentados = set(), set()
    resultados, assuntos = Counter(), Counter()
    for submissao in submissoes:
        problema = submissao["problem"]
        identidade = (problema.get("contestId"), problema.get("problemsetName"), problema["index"], problema["name"])
        resultado = submissao.get("verdict", "PENDING")
        resultados[resultado] += 1
        tentados.add(identidade)
        if resultado == "OK" and identidade not in resolvidos:
            resolvidos.add(identidade)
            assuntos.update(problema.get("tags", []))
    return {"total_submissoes": len(submissoes), "problemas_tentados": len(tentados), "problemas_resolvidos": len(resolvidos), "resultados": dict(resultados), "assuntos_resolvidos": dict(assuntos)}

def salvar_json(nome, dados):
    pasta = Path(__file__).parent / "data"
    pasta.mkdir(exist_ok=True)
    (pasta / nome).write_text(json.dumps(dados, indent=4, ensure_ascii=False), encoding="utf-8")

def main():
    handle = input("ENTRELINHAS - POC01\nDigite seu handle: ").strip()
    if not handle:
        print("Handle invalido.")
        return 1
    try:
        perfil = obter_perfil(handle)
        handle = perfil["handle"]
        submissoes = obter_submissoes(handle)
        historico = obter_rating(handle)
        problemas = obter_problemas()
        analise = analisar_submissoes(submissoes)
        resumo = {k: perfil.get(k) for k in ("handle", "rating", "maxRating", "rank")}
        for nome, dados in [("perfil", resumo), ("submissoes", submissoes), ("rating", historico), ("problemas", problemas), ("analise", analise)]:
            salvar_json(nome + ".json", dados)
        print(json.dumps(resumo, indent=2, ensure_ascii=False))
        print(json.dumps(analise, indent=2, ensure_ascii=False))
        print("Problemas de busca binaria:", len(problemas))
        print("Arquivos JSON salvos.")
        return 0
    except (requests.RequestException, ValueError, KeyError, IndexError, OSError) as erro:
        print("Erro:", erro)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
