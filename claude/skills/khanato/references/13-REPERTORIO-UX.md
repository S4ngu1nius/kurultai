# Repertório de interfaces por necessidade

Consulte os padrões pertinentes ao criar ou revisar uma interface de trabalho. Esta referência complementa o cartão `ux-ui-designer` em [Empresas — execução](03-EMPRESAS-SQUAD.md); não exige aplicar todos os padrões a cada tela.

Comece pela tarefa do usuário, pelos dados e pelas restrições do projeto. Confira os componentes e a identidade existentes antes de escolher alternativas. O nome do setor não determina tema visual, paleta, animação, densidade ou frequência de atualização. Preserve decisões aceitas no design system do projeto; registre ali mudanças materiais e seus motivos, sem criar uma segunda fonte canônica por rotina.

## Tabelas densas

**Quando:** comparar registros, conferir valores ou executar uma operação sobre um conjunto. Exemplo: conciliação com valor previsto, realizado e divergência por lançamento.

**Decisão:** priorize as colunas necessárias à comparação e à identificação de negócio. Detalhes secundários podem ficar em uma expansão ou página de detalhe. Cabeçalho fixo, ordenação e filtros ajudam quando o volume e a tarefa os justificam. Em espaço estreito, compare rolagem horizontal com outra apresentação: cartões podem facilitar leitura individual, mas dificultar comparação entre linhas. Distinga seleção da página e seleção de todos os resultados antes de uma ação em lote.

**Conferir:** valores, totais e exportação usam o escopo declarado de filtros; números e unidades permitem comparação; rótulos longos não escondem o identificador necessário; ordenação e seleção continuam compreensíveis por teclado. Teste o conjunto e a largura representativos do uso.

## Formulários extensos

**Quando:** uma operação exige vários grupos de informações, como cadastro, prestação de contas ou configuração de regras.

**Decisão:** agrupe por significado e dependência. Seções favorecem consulta e edição transversal; etapas favorecem uma sequência com pré-requisitos reais. Escolha a estrutura pelo trabalho, sem fragmentar apenas para reduzir a altura da página. Explique formato, consequência e obrigatoriedade onde houver dúvida concreta. Se houver rascunho ou salvamento automático, especifique sua persistência e como o usuário reconhece o estado salvo.

**Conferir:** erro aponta o campo e a correção possível; falha de envio preserva os dados quando tecnicamente possível; retornar a uma etapa não apaga entradas; campos condicionais têm tratamento definido ao mudar a condição. Observe teclado, foco e revisão antes de uma conclusão com consequências relevantes.

## Navegação entre lista e detalhe

**Quando:** o usuário pesquisa um conjunto e examina ou altera itens sucessivos, como processos, documentos e conciliações.

**Decisão:** página de detalhe comporta conteúdo e ligações diretas; painel lateral pode manter o conjunto visível em consultas curtas, mas reduz espaço e exige cuidado com foco e telas menores. Preserve o contexto de retorno que ajuda o trabalho: filtros, ordenação e posição na lista, conforme a implementação. Diferencie navegação para o item e ações sobre o item.

**Conferir:** voltar à lista não reinicia desnecessariamente a busca; abrir uma ligação direta resolve o contexto e a autorização; a seleção continua identificável; fechar painel ou concluir uma ação devolve o foco a um ponto útil. Mudanças de estado do item aparecem no conjunto sem induzir ação sobre dados antigos.

## Gráficos e indicadores

**Quando:** a representação facilita uma pergunta de comparação, evolução, distribuição ou composição. Valores exatos para conferência podem continuar melhor servidos por uma tabela.

**Decisão:** para comparar categorias, considere barras; para acompanhar uma série ordenada no tempo, linhas; para examinar dispersão de valores, uma distribuição. São alternativas iniciais, sujeitas ao dado e à pergunta. Identifique unidade, período, origem e momento de atualização quando afetam a interpretação. Diferencie ausência de dado e valor zero. Atualização em tempo real só se justifica pela decisão operacional e pela disponibilidade da fonte.

**Conferir:** agregações e filtros correspondem aos números de origem; escala e denominador não distorcem a comparação; cor não é a única forma de distinguir informação. Forneça acesso útil aos valores ou uma descrição equivalente conforme a tarefa. Confira texto longo, dado faltante e períodos sem observação quando pertinentes.

## Estados, validação e permissão

**Quando:** uma operação pode aguardar processamento, falhar, retornar vazio ou depender de acesso.

**Decisão:** distinga primeira utilização, busca sem resultados, carregamento, falha e informação desatualizada. Ofereça uma ação que corresponda à causa: criar, ajustar filtro, tentar novamente ou solicitar acesso pelo fluxo existente. Confirmação visual deve refletir o resultado real; operação assíncrona precisa comunicar aceitação e conclusão separadamente quando isso importar. Visibilidade de botão não substitui a autorização no servidor.

**Conferir:** repetir envio não provoca efeitos duplicados indevidos; uma falha permite recuperação compatível com o fluxo; mensagens ajudam sem revelar dados restritos; estados de permissão seguem a política de privacidade, inclusive quando ela exige ocultar a existência de um registro. Priorize estados afetados pela entrega, sem criar todos os cenários possíveis por obrigação.

## Verificação de interface

Selecione os itens afetados pela entrega e confira na interface renderizada, com dados e larguras representativos. Código sem erro e captura estática não comprovam interação.

- **Teclado e foco:** percorra o fluxo sem mouse; ações e navegação usam elementos semânticos. Confira ordem e indicação visível do foco, ausência de bloqueio indevido e, em diálogos/painéis, fechamento e retorno do foco coerentes. Cabeçalhos e sobreposições não devem esconder o controle focado.
- **Formulários:** rótulos associados aos controles, nome acessível em botões de ícone e indicação de erro que permita localizar e corrigir o campo. Confira envio, correção e recuperação nos estados pertinentes descritos acima; preserve colagem e dados de entrada quando compatíveis com o fluxo.
- **Movimento:** se houver animação, confira a preferência de movimento reduzido (`prefers-reduced-motion` na Web), suprimindo movimento não essencial sem perder informação ou ação. Um efeito visual não justifica exigir arraste ou gesto como única forma de operar.
- **Conteúdo e estado:** teste texto longo, dados ausentes e estados de carregamento, falha e permissão que a mudança afeta. Confira legibilidade, contraste e informação não dependente apenas de cor; notificações relevantes precisam ser perceptíveis pelas tecnologias assistivas pertinentes.

Origem: adaptação seletiva das [Web Interface Guidelines da Vercel](https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md), consultadas em 02/10/2026, com fontes primárias W3C sobre [verificação inicial](https://www.w3.org/WAI/test-evaluate/preliminary/), [rótulos](https://www.w3.org/WAI/tutorials/forms/labels/) e [movimento reduzido](https://www.w3.org/WAI/WCAG22/Techniques/css/C39). Preferências de stack, tipografia e redação do catálogo não são normas globais do Khanato.

## Aceite e procedência

Converta as escolhas relevantes em critérios observáveis e confira o resultado renderizado e as interações disponíveis. Quando precisar afirmar conformidade com uma norma, consulte sua fonte primária vigente e delimite o que foi testado. Revisão heurística e protótipo não demonstram usabilidade com usuários nem benefício medido.

Síntese original do Khanato, inspirada na organização por domínio e em alternativas com condições de uso do projeto **UI/UX Pro Max**, de **nextlevelbuilder**. Referência examinada em 14/09/2026: commit `7f69fed6a2717900085f1bc3b263721f8ba025e2`, [estrutura do catálogo de gráficos](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7f69fed6a2717900085f1bc3b263721f8ba025e2/src/ui-ux-pro-max/data/charts.csv) e [busca por domínio e plataforma](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7f69fed6a2717900085f1bc3b263721f8ba025e2/src/ui-ux-pro-max/scripts/search.py). Estes padrões são critérios de julgamento adaptados ao Khanato, sem reprodução do catálogo ou alegação de pesquisa de usabilidade executada. A referência não instala nem executa o mecanismo externo.
