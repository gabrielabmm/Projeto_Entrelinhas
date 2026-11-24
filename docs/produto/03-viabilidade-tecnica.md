# Estudo de viabilidade técnica — Entrelinhas
24/11/2026 | v1.0 preliminar | Gabriela Brasileiro Machado
## Parecer
Viabilidade documental favorável; Codeforces prioritário, AtCoder condicionado. Não houve teste real de API nesta preparação.
## Codeforces
API oficial JSON: https://codeforces.com/apiHelp ; métodos: https://codeforces.com/apiHelp/methods ; objetos: https://codeforces.com/apiHelp/objects . Métodos públicos user.info, user.status (from/count), user.rating, problemset.problems, contest.list, contest.status, contest.ratingChanges. Intervalo conservador de 2,1 segundos na POC; revalidar documentação antes de produção. Dados: handle, submissão, problema, verdict, timestamp, linguagem, tempo de execução, memória, tags, dificuldade e rating quando disponíveis.
## AtCoder
Projeto comunitário não oficial: https://github.com/kenkoooo/AtCoderProblems ; documentação: https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md . Recursos /atcoder-api/v3/user/submissions (até 500 por consulta, cursor temporal), /resources/problems.json, merged-problems.json, problem-models.json, contests.json, contest-problem.json. Verificar caminhos atuais, condições de uso, intervalo superior a um segundo e disponibilidade. Tags temáticas não confirmadas; classificação manual inicial. Rating histórico a investigar. Dificuldades não equivalentes ao Codeforces.
## Dados
Importados: perfil, submissões, problemas, resultados, datas, rating e tags quando disponíveis. Manuais: causa do erro, editorial, independência, tempo real e reflexão. Calculados: habilidades, recomendações, XP e revisões. Ausência não significa zero.
## Arquitetura candidata
React/TypeScript, Java/Spring Boot, PostgreSQL; monólito modular, REST, adaptadores por plataforma, JPA/Flyway, Spring Security, Tailwind/Recharts, OpenAPI, Docker Compose, GitHub Actions, JUnit/Mockito/Vitest/Playwright/axe-core. POCs Python. Frontend consulta backend, não APIs externas diretamente.
## Sincronização
Importação paginada, normalização, persistência e métricas. Inicialmente manual; proposta futura: perfis ativos 60 min, manual 5 min de intervalo, rating 6 h, catálogo 24 h. Controle central de limites, timeout, retry/backoff limitado, logs, idempotência, retomada e atualização de verdicts pendentes/reavaliados. Codeforces usa offset e IDs; AtCoder cursor temporal com sobreposição e deduplicação; testar fronteiras. Preservar dados em falhas.
## Normalização
Chave de submissão: plataforma + ID externo. Problemas: plataforma + identificador estável. Preservar verdict original e mapear OK/AC, WRONG_ANSWER/WA, TIME_LIMIT_EXCEEDED/TLE, MEMORY_LIMIT_EXCEEDED/MLE, RUNTIME_ERROR/RE, COMPILATION_ERROR/CE, TESTING/WJ; desconhecidos explícitos. UTC, apresentação no fuso do usuário. Taxonomia em português, múltiplas tags e origem da classificação. Não equiparar ratings entre plataformas.
## Modelo conceitual
Usuário, plataforma, perfil externo, problema, submissão, assunto, diário, causa de erro, habilidade, recomendação, revisão, conquista, amizade, desafio e sincronização.
## Módulos e algoritmos
| Módulo | Viabilidade | Complexidade |
|---|---|---|
| Trajetória | Alta | Média |
| Mapa de habilidades | Condicionada | Alta |
| Diário | Alta | Baixa |
| Próximos passos | Alta | Alta |
| Relembre | Alta | Média |
| Conexões | Alta | Alta |
| Retrospectiva | Alta | Média |

Habilidade experimental: 30% resolução, 25% dificuldade relativa, 20% independência, 15% consistência, 10% recência. Recomendações: 35% reforço, 25% revisão, 25% nível, 15% objetivos. Normalizar fatores e tratar dados ausentes e evidência insuficiente. Pesos não validados. Revisão experimental dias 1, 3, 7, 14, 30, adaptável. XP por problemas distintos, diversidade, revisões e objetivos, evitando farming. Retrospectiva por agregações temporais. Sem necessidade de IA generativa.
## Segurança e custos
Privacidade por padrão, autorização, TLS, proteção de segredos, exclusão de dados, limites de uso. Perfil público não comprova titularidade; verificar antes de rankings verificados. Não coletar senhas externas. Desenvolvimento local sem custos adicionais previstos; produção depende de hospedagem, backups, domínio e limites.
## Riscos
APIs instáveis, tags ausentes, escalas diferentes, duplicação, rate limits, métricas imprecisas, recomendações inadequadas, exposição de dados, custos, escopo e uso indevido de perfis. Mitigar com adaptadores, cache, unicidade, transparência, autorização e incrementos.
## POCs
1. Codeforces: perfil, submissões, rating, catálogo, paginação e erros.
2. AtCoder: submissões, catálogo, dificuldade, cursor e rating.
3. Normalização: DTOs, IDs, datas, verdicts e ausências.
4. Sincronização: repetição sem duplicação, novos registros, pendências e falhas.
5. Algoritmos: dados sintéticos, métricas, ordenação, revisão e evidência insuficiente.
Critérios: dados essenciais recuperados, normalização sem perda relevante, integridade em reexecução, resultados determinísticos e explicáveis. Todas aguardam validação prática.
