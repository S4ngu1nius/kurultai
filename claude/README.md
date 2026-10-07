# Khanato para Claude — 2.0.0

Núcleo de instruções derivado do Khanato do Codex `2026.10.03-hermes-v1`, com adaptação `2026.10.03-claude-v1`. A sessão principal coordena, executa e integra; competências são mobilizadas conforme a tarefa.

## Conteúdo e equivalência

- Seis skills: `khanato`, `arauto`, `curia`, `nous`, `vigil` e `voz-do-contra`.
- Os 50 IDs anteriores de agentes foram preservados, todos com `model: inherit`, ligados aos cartões atuais do núcleo. Especialidades opcionais adicionais permanecem no catálogo e podem ser exercidas sem criar agentes fixos.
- Mesma Constituição, competências, segurança de aplicações, memória, formatos Obsidian, revisão e métodos Hermes do Codex.
- Adaptadores para Cartographer e para as ferramentas, permissões, caminhos e contexto de Code/Cowork/Chat. Não há dependência de outro runtime Hermes.

Igualdade de instruções e critérios não significa ferramentas idênticas, mesma qualidade de modelo ou comportamento já comprovado no Claude. As 36 rodadas do template de avaliação continuam `not_run`; validação estrutural não as executa.

## Usar e verificar

O ponto de entrada é [skills/khanato/SKILL.md](skills/khanato/SKILL.md). O [adaptador de ambiente](skills/khanato/references/17-AMBIENTE-CLAUDE.md) trata a superfície em uso. O [mapa](skills/khanato/docs/CODEBASE_MAP.md) explica os arquivos e a manutenção.

No Claude com o plugin habilitado, invoque a skill Khanato pelo comando que a interface apresentar (em Code, normalmente `/khanato:khanato`) ou peça explicitamente para usá-la. A descrição permite descoberta automática, mas isso não garante carregamento em toda conversa. Para torná-la uma preferência permanente, a instrução pessoal/projeto da superfície deve mandar carregar a skill; preserve outras preferências existentes.

Texto de preferência: “Meu modo operacional padrão é Khanato. Use a skill Khanato instalada em toda demanda e apenas as referências pertinentes. A sessão principal coordena, executa e integra. Respeite instruções superiores, permissões, pedido direto e regras locais. Se a skill não estiver acessível, informe a ausência.”

Depois de recarregar/iniciar a sessão apropriada, confira o plugin `khanato` versão `2.0.0` e peça uma tarefa pequena com a skill. Verifique arquivos realmente lidos, resultado e restrições; uma resposta que apenas diz conhecer o Khanato não comprova que leu esta versão.

## Distribuição

O ZIP do plugin contém `.claude-plugin/plugin.json`, `skills/` e `agents/` na raiz. No Claude, use Customize → Plugins → Add → Upload plugin conforme a interface disponível. Ao atualizar uma instalação pessoal, confira o resultado exibido; não presuma substituição da conta apenas porque o nome do arquivo coincide.

No Claude Code, o diretório do plugin também pode ser carregado com `claude --plugin-dir CAMINHO_DO_PLUGIN` para validação local quando a CLI estiver disponível. Não instale um segundo runtime por consequência desta adaptação.

O ZIP de skill avulsa contém somente a pasta `khanato/`; é uma alternativa para a área de Skills onde essa importação estiver disponível. Ele contém o núcleo completo, mas não registra os 50 subagentes nativos nem os outros cinco comandos. Evite habilitar cópias divergentes com o mesmo nome.

Skills podem ser usadas nas três superfícies; agentes nativos e hooks não são recursos do Chat. Este pacote não acrescenta hooks, MCPs, credenciais, agendamentos ou permissões. Verifique as capacidades realmente expostas e a leitura do cofre em cada ambiente.

## Fonte, atualização e reversão

O núcleo canônico continua na edição Codex (`codex/skills/khanato` neste repositório). Esta edição distribui uma cópia identificada e adaptada; não há sincronização automática nem vínculo a caminhos de cache. Atualizações do núcleo pedem comparação de hashes/diff, adaptação apenas das diferenças de ambiente e reverificação proporcional.

Ao adaptar ou atualizar, mantenha baseline, diferenças, revisão e cópias importáveis fora do cache do Claude. Editar os arquivos locais de uma sessão Cowork não prova que o plugin foi salvo na conta ou ficará disponível em sessões futuras. Para reverter, compare o estado atual com a versão aplicada e restaure somente os arquivos desta mudança, preservando alterações posteriores.

Fontes oficiais: [formato e teste de plugins](https://claude.com/docs/plugins/build), [suporte por superfície](https://claude.com/docs/plugins/platform-support), [instalação e atualização no Cowork](https://claude.com/docs/cowork/guide/plugins), [carregamento no Code](https://code.claude.com/docs/en/plugins/loading).
