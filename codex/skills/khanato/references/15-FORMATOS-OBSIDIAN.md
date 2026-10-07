# Formatos do Obsidian por necessidade

Consulte ao criar ou editar propriedades e links de notas, arquivos `.base` ou `.canvas`. A política do cofre e [Missões e memória](08-MISSOES-MEMORIA.md#memória-autoridade-e-atualização) continuam definindo destino, modelos, sigilo e histórico. Usar estes formatos não ativa CLI, plugins, JavaScript, pesquisa externa ou manutenção agendada.

## Markdown, propriedades e links

- Preserve o esquema do cofre. Propriedades ficam no início da nota, em frontmatter YAML; cada chave é única. Um mesmo nome de propriedade usa o mesmo tipo no cofre, portanto não troque lista por texto ou data por descrição para resolver uma nota isolada.
- Wikilinks em propriedades precisam ser strings entre aspas, inclusive dentro de listas: `organization: "[[Organização]]"`. Preserve listas, booleanos e datas conforme os modelos; conteúdo extenso pertence ao corpo da nota.
- Use caminho a partir da raiz do cofre quando nomes forem ambíguos e `/` nos links internos mesmo no Windows. Confira o destino real, inclusive cabeçalho ou ID de bloco, não apenas o texto exibido pelo alias. Link para nota inexistente pode ser intencional; identifique-o como pendência, sem alegar resolução.
- Ao renomear ou mover fora do aplicativo, confira as referências afetadas: não presuma que a atualização automática do Obsidian foi executada. Preserve a sintaxe e os caminhos de embeds; não substitua anexos ou fontes canônicas por cópias por conveniência.

Fontes: [Properties](https://obsidian.md/help/properties) e [Internal links](https://obsidian.md/help/links), documentação oficial do Obsidian.

## Bases (`.base`)

O arquivo é YAML conforme o esquema de Bases; não use SQL ou sintaxe Dataview. Sem filtro, a base abrange todos os arquivos do cofre. Declare o escopo necessário por propriedades/pastas; filtros globais e da visão se combinam com `AND`.

Distinga propriedades da nota (`note.status` ou `status`), do arquivo (`file.name`) e calculadas (`formula.total`). Fórmulas são strings YAML e não podem ter referências circulares. `displayName` muda apresentação; filtros e fórmulas continuam usando o identificador da propriedade. Não use uma fórmula de exibição como atualização do dado da nota.

Ao usar `this`, confira o contexto: na base aberta refere-se à base; numa incorporação, à nota/Canvas que a contém; na barra lateral, ao arquivo ativo. Valide YAML, nomes de propriedades/fórmulas, referências e filtros com exemplos que devem entrar e ficar fora. Parsing correto não comprova que a visão selecionou o conjunto esperado.

Fonte: [Bases syntax](https://obsidian.md/help/bases/syntax), documentação oficial do Obsidian.

## Canvas (`.canvas`)

Preserve os IDs e campos existentes ao editar o JSON. Nós precisam de `id`, `type`, `x`, `y`, `width` e `height`, além do conteúdo exigido pelo tipo (`text`, `file`, `link` ou `group`). A especificação exige IDs únicos como strings, sem impor 16 caracteres hexadecimais. A ordem de `nodes` define a sobreposição visual; reordenar a lista pode alterar a apresentação.

Confira unicidade de IDs, campos/tipos, dimensões úteis e se `fromNode`/`toNode` de cada aresta apontam a nós existentes. Para nós de arquivo, verifique o caminho no cofre e o `subpath` quando usado; este começa com `#`. Cor predefinida é string, como `"1"`. Não remova campos de extensões ao regravar um arquivo conhecido apenas parcialmente.

Fonte: [JSON Canvas 1.0](https://jsoncanvas.org/spec/1.0/).

## Verificação e procedência

Depois de salvar, releia os arquivos e confira somente os vínculos e visões afetados. Use os validadores já disponíveis para sintaxe e integridade; quando houver acesso ao aplicativo, confira também renderização e interação pertinentes. Sem essa verificação, declare o limite visual ou funcional em vez de afirmar que a visão funciona. Inspeção de arquivo não exige instalar um plugin para abri-lo.

Síntese própria motivada por [obsidian-skills, de kepano](https://github.com/kepano/obsidian-skills), consultado em 02/10/2026; os detalhes acima foram conferidos nas especificações oficiais vinculadas. Não reproduz o pacote nem importa sua skill de CLI ou seus auxiliares de extração. Reconfira a documentação ao usar recurso novo ou encontrar incompatibilidade com a versão instalada.
