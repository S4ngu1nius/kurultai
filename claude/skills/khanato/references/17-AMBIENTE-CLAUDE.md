# Ambiente Claude — execução e portabilidade

Leia a seção pertinente ao descobrir ferramentas, delegar, acessar arquivos, retomar trabalho ou agendar.
A [Constituição](00-CONSTITUICAO-ESTRUTURA-FLUXOS.md) e os [contratos de missão](08-MISSOES-MEMORIA.md) continuam vigentes.
Identifique a superfície e o ambiente efetivos; instalar o mesmo pacote não produz capacidades idênticas.

## Superfície e capacidade

| Superfície | O que conferir antes de depender dela |
|---|---|
| Claude Code — terminal, IDE ou aba Code | Host local, WSL ou remoto; raiz do projeto, ferramentas, instruções carregadas e permissões da sessão. |
| Cowork | Sessão local ou remota, pastas conectadas, ferramentas de arquivos e ambiente de execução de código; o caminho do host pode diferir do apresentado à ferramenta. |
| Chat — web ou aba Chat | Anexos, skills e conectores efetivamente disponíveis; não presumir acesso ao disco, subagentes ou hooks de plugin. |

Skills e comandos de plugin podem funcionar nas três superfícies; agentes e hooks são próprios de Cowork/Code.
Conector declarado não significa conta conectada. Consulte o [suporte por aplicativo](https://claude.com/docs/plugins/platform-support) quando isso afetar a entrega.

## Descoberta, instruções e caminhos

Use ferramentas e skills realmente expostas, lendo seus contratos; prefira recurso adequado já disponível.
`Read`, `Edit`, `Write`, Bash ou PowerShell são exemplos de interfaces, não uma lista garantida nesta sessão.
APIs, nomes de ferramentas, goals, chats e automações do Codex não são comandos Claude.
Uma ferramenta ausente pede alternativa autorizada ou dependência explícita, sem fingir execução.

Em Code, confira as instruções de usuário/projeto carregadas, inclusive `CLAUDE.md` e regras locais.
O suporte direto a `AGENTS.md` depende da versão/configuração e da presença de outros arquivos de instrução; não presuma que ambos foram lidos.
Um `CLAUDE.md` na raiz de plugin não é carregado como instrução de projeto. Preserve regras locais ao adaptar caminhos.
Fontes: [instruções e memória](https://code.claude.com/docs/en/memory), [componentes de plugin](https://code.claude.com/docs/en/plugins/components).

Resolva referências internas a partir do arquivo/skill que as contém, não do diretório corrente do shell.
O carregador de plugins do Claude Code expande `${CLAUDE_PLUGIN_ROOT}` no corpo Markdown de skills e agentes.
Use o caminho expandido para localizar arquivos irmãos; essa variável não é garantida no ambiente de um comando Bash.
Se vier literal, descubra a localização pelos recursos da sessão; não invente diretório nem procure indiscriminadamente fora do escopo.
Não fixe caminhos de cache ou identificadores de sessão na instrução durável. [Contrato de caminhos](https://code.claude.com/docs/en/plugins-reference#where-each-variable-resolves).

## Delegação e contexto

Delegue frentes independentes com objetivo, aceite, entradas, limites e destino da entrega, conforme 08.
Passe explicitamente as invariantes pertinentes, o caminho da skill e as referências necessárias.
Subagentes comuns não recebem o histórico, as skills já invocadas nem a auto memory da sessão principal; um fork tem contrato diferente.
Explore/Plan podem omitir `CLAUDE.md`; outros agentes podem ter configuração que omite instruções. Não dependa apenas de herança presumida.
O campo `skills` pode pré-carregar conteúdo, mas confirme resolução/disponibilidade; o nome curto de uma skill irmã não substitui essa conferência.
Ferramentas herdadas sofrem filtros; negar Edit/Write não elimina efeitos de shell ou MCP. Escopo textual não comprova isolamento entre agentes.
Preserve o modelo configurado e escolha a menor equipe útil; papéis não criam processos permanentes. [Subagentes](https://code.claude.com/docs/en/sub-agents).

Antes de compactação ou passagem material, registre estado confirmado, autorizações, artefatos, falhas e próximo passo.
Ao retomar, confronte o resumo com as fontes e o estado atual; instruções de compactação orientam preservação, sem garantir ausência de perdas.
Use [Hermes adaptado](16-HERMES-NO-CLAUDE.md) para recuperação e efeitos incertos. [Contexto no Code](https://code.claude.com/docs/en/how-claude-code-works).

## Fronteiras de execução

Identifique onde cada ferramenta executa e quais dados alcança antes de depender de isolamento.
O sandbox de shell do Claude Code não está disponível no Windows nativo; não declare comandos contidos por esse mecanismo nesse host.
Nos ambientes suportados, esse sandbox cobre comandos de shell e filhos, não ferramentas de arquivos, MCP e hooks.
Hooks de comando podem operar com permissões do usuário. Não os instale nem afrouxe controles para reproduzir comportamento do Codex.
Fontes: [sandbox Code](https://code.claude.com/docs/en/sandboxing), [segurança de hooks](https://code.claude.com/docs/en/hooks#security-considerations).

No Cowork local, execução de código usa VM, enquanto ferramentas de arquivos e MCP podem operar por outra fronteira.
Cowork remoto usa outro ambiente; acesso ao dispositivo depende do aplicativo, pastas conectadas e permissões efetivas.
Não interprete a VM como contenção integral de todos os componentes. [Arquitetura Cowork](https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview).

## Memória, Obsidian e mapas

Auto memory é recurso do aplicativo, não fonte canônica do Khanato. Preserve as autoridades e destinos definidos em 08.
Não replique conversas, segredos ou todo o cofre ali; prefira referência mínima à fonte quando memória auxiliar for pertinente.
Não ligue/desligue auto memory nem altere settings por consequência desta integração. [Memória do Code](https://code.claude.com/docs/en/memory#auto-memory).

O cofre canônico, quando adotado, é o indicado pelo Imperador nas instruções locais; o caminho indicado não prova acesso pela sessão.
No Code local Windows, confirme o caminho e a política antes de editar. Em WSL/remoto, resolva o caminho real autorizado.
No Cowork, use somente a pasta conectada e o caminho exposto pela ferramenta; não converta `C:\` em caminho de VM por suposição.
No Chat, anexar a nota não concede escrita no cofre. Sem acesso, prepare `docs/obsidian-pending/` no projeto autorizado, com destino e identificador.
Se nem essa escrita estiver disponível, entregue o conteúdo pendente como artefato acessível e informe a limitação; não declare incorporação ou sincronização.

Para mapear código, aplique [Cartographer no Claude](12-CARTOGRAPHER-CLAUDE.md) e confirme disponibilidade do plugin/skill.
Sem ele, use inventário e leitura nativos no escopo permitido, conservando os critérios do adaptador e declarando a indisponibilidade.
Não instale dependências, mude modelos ou crie mapas fora da raiz real apenas para satisfazer convenção do pacote.

## Recorrência e instalação verificável

Agende somente por pedido que autorize recorrência, com objetivo, fuso, término, notificação e efeitos definidos.
No Code, diferencie agendamento de sessão, tarefa local Desktop e rotina remota; encerramento, retomada e permissões têm contratos próprios.
No Cowork, confira o mecanismo de tarefas agendadas e onde executa. No Chat, sem recurso correspondente, entregue o plano sem afirmar agendamento.
Não transforme instalação do Khanato em monitoramento, cron, listener ou gateway. Fontes: [sessão](https://code.claude.com/docs/en/scheduled-tasks), [Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks), [rotinas](https://code.claude.com/docs/en/routines), [Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork).

Separe pacote preparado, arquivo instalado, plugin salvo na conta, componente carregado e comportamento verificado.
Um ZIP, hash ou versão no manifesto não comprova os estados seguintes. Confira origem e versão na superfície usada.
Cowork pode detectar edições locais antes de sobrescrevê-las; isso não comprova atualização da conta ou de futuras sessões.
Mantenha fonte estável e pacote recuperável; alterações de conta e instalação seguem seu escopo próprio, sem copiar credenciais ou editar caches como registro canônico.
Fontes: [instalação e atualização Cowork](https://claude.com/docs/cowork/guide/plugins), [carregamento de plugins](https://code.claude.com/docs/en/plugins/loading).

Síntese adaptada das fontes oficiais consultadas em 03/10/2026. Reconfira contratos quando mudarem superfície, versão, ferramentas ou permissões; documentação não substitui observação da sessão.
