# Cartographer no Codex — adaptador canônico

Versão do adaptador: 2026.09.12-missoes-v1. Este arquivo concentra a adaptação autorizada pelo Imperador; as convenções do plugin original continuam subordinadas a ele e às instruções superiores.

## Uso padrão

Ordem do Imperador de 12/09/2026: use o plugin **Cartographer de kingbootoshi/Bootoshi** (`cartographer@cartographer-marketplace`) como padrão de mapeamento e orientação em todos os projetos de código, inclusive novos projetos, checkouts isolados e subpastas. Aplique o skill `cartographer` do plugin instalado e estas adaptações ao Codex, que prevalecem sobre as convenções do pacote original. Resolva a raiz do projeto pelas instruções locais e pelo contexto do repositório antes de procurar ou criar o mapa; os caminhos desta regra são relativos a essa raiz, mesmo quando a tarefa começa em subpasta.

- Ao iniciar trabalho no projeto, leia `docs/CODEBASE_MAP.md`, se existir, e confira seu escopo e atualidade antes de confiar nele. Se faltar, produza o mapa na primeira demanda que envolva entendimento ou alteração do código, com profundidade proporcional ao projeto; em projeto novo, crie-o quando houver estrutura real para documentar. Em pedidos explicitamente somente leitura, faça a orientação sem gravar arquivos. Conversas sem projeto de código não exigem mapa.
- Ao concluir alterações que afetem arquitetura, módulos, interfaces, dependências ou fluxos, atualize as seções correspondentes e preserve anotações válidas. Reutilize o mapa e mapeie apenas as partes afetadas; não refaça uma leitura integral em toda tarefa pequena. Registre cobertura parcial e pendências em vez de afirmar mapeamento completo sem leitura.
- Verifique mudanças commitadas e também staged, unstaged e arquivos novos. Use revisão Git e estado real da árvore; sem Git, compare hashes de conteúdo. Não declare o mapa atual somente por data, quantidade de arquivos ou igualdade dos caminhos. Registre data UTC real, revisão quando houver, escopo coberto e limitações.
- No Codex, use os modelos, ferramentas e slots disponíveis; não imponha Opus, Sonnet, Haiku, `Task` ou variáveis de ambiente do Claude. O coordenador pode ler e verificar código. Delegue frentes independentes quando útil, com contratos e limites de escrita, e audite a síntese. Preserve o modelo configurado pelo usuário.
- Prefira inventário nativo com Git ou `rg --files`, respeitando exclusões e `.gitignore`. Não siga links simbólicos/junções para fora do projeto, nem inclua segredos, `.env` reais, chaves privadas ou credenciais no mapa ou nos contextos delegados. O scanner original é opcional: execute-o somente após conferir que o escopo e as exclusões são adequados. Contagem de tokens sem medição deve ser omitida ou declarada como estimativa; a ausência de `tiktoken` não impede mapear com as ferramentas nativas.
- O resultado canônico é `docs/CODEBASE_MAP.md`, com arquitetura, módulos, pontos de entrada, dependências, fluxos e guia de navegação sustentados pelo código lido. Preserve documentação manual e instruções locais; atualize somente uma referência curta no `AGENTS.md` do projeto quando útil e dentro do escopo. Não crie `CLAUDE.md` apenas por convenção do plugin.
- Esta regra define o uso nas tarefas; não cria monitoramento em segundo plano, não autoriza envio de código a serviços externos nem migração de banco. Nos projetos com cofre Obsidian adotado, cumpra também a política já estabelecida. O mapa complementa essa documentação e não a substitui.

## Compatibilidade e atualização

Origem instalada: `https://github.com/kingbootoshi/cartographer.git`, commit `a62d16981b6aa1f5f6ef56701c49b81a16a8e30a`, plugin `cartographer@cartographer-marketplace`. Essa referência identifica a versão examinada; não garante que o pacote remoto continue igual.

Preserve o plugin original; não corrija silenciosamente o cache. Ao atualizar o plugin ou adaptador, confira manifesto e origem, diferenças de ferramentas/modelos, dependências, exclusões, links/junções e critério de atualidade. Reexecute o caso Cartographer da [suíte do Khanato](09-AVALIACAO-KHANATO.md) antes de declarar compatibilidade verificada. Uma falha do scanner não impede o inventário nativo no escopo permitido.

O scanner legado exige avaliação antes do uso: seu tratamento de exclusões, separadores de caminho e links pode não corresponder ao repositório. Não instale dependência nem estime tokens como se fossem medidos apenas para satisfazer o scanner.

## Critério de conclusão de um mapa

Arquitetura e navegação derivam de arquivos realmente lidos. Registre arquivos ou áreas cobertas, lacunas, revisão Git e mudanças locais consideradas; sem Git, use hashes dos conteúdos relevantes. Um hash só identifica o conteúdo: mudança exige releitura da parte afetada, não mera troca da data do mapa. Preserve seções manuais válidas.

Validação: conferir o mapa contra o código, modificar conteúdo em caminho já existente e adicionar arquivo novo, então atualizar cobertura e explicação. Somente o resultado dessa execução permite afirmar que o ciclo foi verificado.
