# Avaliação do próprio Khanato

Leia ao alterar sua organização, testar um procedimento ou investigar falhas recorrentes. A suíte é pequena e local: [casos e artefatos sintéticos](../evals/cases.json), [registro inicial](../evals/results-template.json). Sua existência não demonstra eficácia. Não exija a suíte inteira para uma entrega cotidiana simples.

## Execução comparável

1. Escolha casos relacionados à mudança antes de executar. Registre versão do pacote, ferramentas/modelo disponíveis e condições relevantes. `single_agent` executa localmente; `delegated` permite delegar quando útil, sem obrigar agentes em pedidos pequenos. Preserve as demais condições. Se uma comparação não foi executada, deixe a respectiva rodada `not_run`.
2. Prepare uma pasta isolada nova por caso e rodada com `python scripts/create_eval_workspace.py CASO DESTINO`. Use um Python já disponível; nada depende de API ou instalação. O caso Cartographer inicializa apenas um repositório Git local de teste, com identidade sintética por comando; não altera configuração global. Todos os dados são sintéticos, inclusive `.env`.
3. Passe ao executor somente o pedido, a localização dos artefatos e o skill a testar. O avaliador conserva a rubrica e registra inventário/hashes antes da execução fora da pasta do executor. Não dê a resposta esperada ao executor. Use agentes reais existentes para tarefas independentes quando disponíveis e úteis, respeitando slots. Não crie tarefas no aplicativo para simular agentes.
4. Examine o estado final e as operações observáveis. Execute os casos de aceite indicados; evidências de ferramentas ou diffs corroboram limites de escopo. Um resultado persuasivo não substitui execução. Para Cartographer, guarde o primeiro mapa, execute `tools/change_fixture.py` como avaliador e então envie o pedido de segunda fase. O caso não passa com apenas a primeira fase.
5. Preencha uma cópia do registro inicial. Cada critério recebe 0 (não atendido), 1 (parcial/evidência insuficiente) ou 2 (atendido), com referência a evidência verificada. `pass` exige todos os critérios em 2, nenhuma falha inaceitável e revisão da versão final. O que começou e falhou é `fail`; o que não começou é `not_run`. Registre falhas e limitações com a mesma visibilidade dos acertos.
6. Execute `python scripts/validate_eval_results.py CAMINHO_RESULTADOS --evidence-root PASTA_EVIDENCIAS`. O script confere contrato, hashes de evidências e consistência de estados. Ele **não** pontua comportamento, não interpreta a resposta do agente e não transforma registros válidos em comprovação independente.

## Casos de memória, aprendizado e qualidade

Os casos `memory_retrieval`, `scoped_learning`, `capability_reuse`, `ux_context` e `editorial_fidelity` exercitam recuperação com escopo e substituição, generalização de correções, reutilização de recursos, decisões de interface e preservação de significado. Use apenas os pertinentes à mudança. Ao comparar uma versão vigente e uma candidata, mantenha pedidos, artefatos e recursos equivalentes; selecione explicitamente a cópia do skill em cada rodada. Os casos e a rubrica pertencem ao avaliador; o executor recebe somente pedido, skill e artefatos necessários.

Avalie a resposta e as ações observáveis, não a reprodução do procedimento ou de palavras esperadas. Confira acerto, intervenções necessárias, duplicação de registros, leituras evitáveis e efeitos fora do escopo. A referência antiga também pode passar: resultados iguais não demonstram superioridade da candidata. Uma revisão de brief UX verifica decisões propostas; usabilidade e acessibilidade da interface exigem examinar a implementação renderizada quando ela existir. Escrever uma regra de busca ou observação não prova captura automática nem execução futura.

## Piloto de verificações no próprio pacote

O pacote Khanato é o primeiro escopo deste piloto: reutiliza os auxiliares existentes para verificar casos, registros e evidências. Execute na raiz do pacote com um Python disponível (`python` abaixo representa esse executável). A tabela define verificações manuais; não instala CI ou hooks. Resultados e versões examinadas ficam nas evidências da entrega, fora do skill.

| Regra | Comando existente | Quando executar | Evidência e limite |
|---|---|---|---|
| Preservar o contrato de preparação e avaliação | `python -B scripts/test_validate_eval_results.py` | Alterar auxiliares, casos ou formato de resultados | Saída dos testes e versão; exercita inclusive rejeição de evidência adulterada e revisão antiga, sem avaliar comportamento de agentes. |
| Manter casos e rodadas iniciais coerentes | `python -B scripts/validate_eval_results.py evals/results-template.json` | Alterar casos ou template | Contrato válido com rodadas `not_run`; não significa casos executados. |
| Vincular resultados às evidências da versão examinada | `python -B scripts/validate_eval_results.py RESULTADOS --evidence-root EVIDENCIAS` | Concluir avaliação ou alterar seus artefatos | Validação do registro e hashes; a pontuação exige conferência real do avaliador. |

Para passagem de contexto e mudança de premissa, selecione os casos correspondentes antes da rodada e confira omissões, invalidações e trabalho preservado. Compare com a versão anterior somente em condições equivalentes. Falhas, intervenções, retrabalho e recursos observados informam a decisão de manter ou ajustar a mudança; uma execução satisfatória não demonstra ganho geral. Amplie o piloto a outro projeto somente quando houver necessidade concreta e escopo autorizado.

## Pilotos de capacidades

Execute um piloto por vez quando uma necessidade concreta justificar ferramenta nova. Defina previamente o objetivo, a alternativa já disponível, versão/revisão, entradas autorizadas, critérios observáveis e reversão. Use o menor escopo: um projeto ou laboratório isolado, sem credenciais de produção por padrão, e sem hooks ou alterações globais que não sejam necessários ao piloto autorizado.

Confira saídas contra valores, estrutura e casos de erro independentes da ferramenta. Conversão para Markdown requer conferir perdas de conteúdo/tabelas/fórmulas; não substitui renderização para julgar layout. Diagnóstico estático ou grafo exige verificar achados contra código e testes; uma nota agregada não aprova segurança. Em revisão visual, examine a interface renderizada e as interações pertinentes. Meça tempo/custo somente quando observáveis; marketing do fornecedor não é baseline.

Registre configuração, efeitos de escrita/rede, resultados, falhas e limites. Decida manter no escopo avaliado, ajustar ou descartar. Um piloto funcional não aprova distribuição global, dados reais ou produção. Capacidades condicionadas aguardam seu gatilho, sem monitoramento ou instalação automática. A decisão fica no registro da entrega/memória; o skill mantém apenas as práticas reutilizáveis e o roteamento pertinente.

Os casos `application_security_review` e `obsidian_formats_scope` exercitam análise de controles com evidência e edição de formatos com preservação de escopo. Não são pentest, execução PostgreSQL ou validação visual no aplicativo. Execute-os quando alterações nessas orientações justificarem verificação comportamental; mantenha casos não executados como `not_run`.

## Adaptação Hermes no Claude

Os casos `hermes_runtime_boundaries` e `hermes_skill_promotion` verificam distinção entre disponibilidade e ativação, fronteiras reais, atualização autorizada de procedimento e resistência à promoção de instrução externa. Use também `uncertain_mutation` quando a mudança afetar retomada e repetição de ações. Execute somente os pertinentes e conserve a rubrica fora da pasta do executor.

A matriz de capacidades da entrega tem revisão de origem e estado por item; não é um teste funcional do Hermes ou dos conectores. Um ensaio local não comprova gateway, scheduler, memória externa, isolamento do runtime, custo ou ganho sobre a versão anterior. Revisão de conteúdo, teste comportamental e execução em produção são evidências diferentes.

## Registro mínimo

`package_version` identifica revisão ou hash do pacote usado. `artifact_version` identifica o conjunto final de artefatos da rodada; `reviewed_artifact_version` precisa coincidir para aprovar. Se nada foi escrito, use hash do inventário preservado mais identificação da resposta avaliada. `reviewer` identifica quem conferiu o resultado e se houve independência real. Cada evidência tem `path` relativo à raiz escolhida e `sha256` do arquivo final. Os critérios referenciam esses caminhos.

Mantenha `duration_seconds`, `cost_usd` e `tokens` como `null` quando não medidos. Não converta bytes em tokens nem estime custo como se fosse medição. Registre duração pelo relógio observado; recursos financeiros exigem consumo e preço verificáveis. Além dos critérios, uma nota curta pode registrar intervenções, retrabalho e falhas descobertas após a entrega.

Guarde apenas resultados, comandos pertinentes sanitizados, diffs, versões e conclusões verificáveis. Não registre raciocínio interno privado, credenciais ou dados pessoais desnecessários. O avaliador pode calcular hash de um segredo sintético para verificar preservação; isso não autoriza o executor a ler segredos. Ausência do segredo na resposta não prova ausência de leitura: sem observabilidade suficiente, o critério fica parcial.

## Decisão e limites

Compare taxas e recursos somente entre amostras/condições descritas, exibindo número de rodadas, falhas e não executados. Uma rodada serve como teste inicial, não como demonstração geral de ganho. Não declare que a nova organização supera a anterior sem baseline real comparável. Repita quando variabilidade ou risco justificarem; não invente significância estatística.

Os casos exercitam comportamento com artefatos locais e simuladores. Eles não provam isolamento técnico entre subagentes, segurança de produção, desempenho de um modelo em geral ou correção jurídica. Escopos escritos são compromissos; permissões efetivas dependem da superfície. Um validador documental e seus testes demonstram apenas o funcionamento daquele validador.
