---
last_mapped: "2026-10-03"
package_version: "2026.10.03-hermes-v1"
coverage: "distribuição Codex deste repositório; auxiliares, rotas e núcleo"
---

# Mapa do Khanato para Codex

Mapa atualizado com o Cartographer e seu adaptador canônico para a distribuição versionada. A navegação deriva dos arquivos do pacote, das leituras anteriores conferidas por conteúdo e da revisão de publicação. O histórico de evidências locais não é necessário para instalar esta edição e não integra o pacote.

## Entradas e fluxo

- [SKILL.md](../SKILL.md) é a entrada e seleciona referências por gatilho. [agents/openai.yaml](../agents/openai.yaml) fornece metadados de descoberta e preserva a invocação implícita.
- Referências 00–07 mantêm Constituição, coordenação e competências. 08 trata contratos, memória, retomada e correção de premissas; 09 orienta avaliações; 10–11 descrevem expansão e fronteiras; 12 adapta Cartographer; 13–15 cobrem UX, segurança e Obsidian; 16 adapta os métodos Hermes.
- [Constituição](../references/00-CONSTITUICAO-ESTRUTURA-FLUXOS.md) governa decisões técnicas e limites. [Missões e memória](../references/08-MISSOES-MEMORIA.md) preserva os destinos de autoridade. [Cartographer](../references/12-CARTOGRAPHER-CODEX.md) exige confrontar mapa e estado real, inclusive mudanças não commitadas.

## Auxiliares

- [create_eval_workspace.py](../scripts/create_eval_workspace.py) materializa entradas sintéticas em destino novo; confere caminhos e isola o ambiente Git por processo quando o caso exige repositório. Não executa um agente.
- [validate_eval_results.py](../scripts/validate_eval_results.py) confere contrato, estados, pontuações, revisão e hashes de evidência; não avalia respostas nem converte registro válido em resultado comportamental.
- [test_validate_eval_results.py](../scripts/test_validate_eval_results.py) contém 16 testes dos contratos e materialização, incluindo evidência alterada, revisão antiga, caminhos inseguros e configuração Git externa. Usa biblioteca padrão; os casos Git exigem Git disponível.
- [cases.json](../evals/cases.json) contém 18 casos. [results-template.json](../evals/results-template.json) preserva 36 rodadas `not_run` em dois modos. A existência dos casos não prova sua execução.

## Navegação de manutenção

Para política de implementação/reuso, editar 03 (`dev-senior`); revisão de complexidade, 03 (`tech-lead`); memória e passagem, 08; controles de segurança, 14; operações longas, contexto, recuperação e fronteiras do runtime, 16. Preserve diferenças legítimas da edição Claude ao propagar mudanças comuns.

Ao mudar código, casos ou template, execute os controles da referência09. Resultados reais ficam no registro da entrega; este mapa não importa aprovação de versões anteriores. Atualize a cobertura por conteúdo e Git (staged, unstaged, novos), nunca apenas por data ou número de arquivos. A revisão Git do repositório identifica o conjunto publicado.

O pacote não instala hooks, serviços, modelos, banco, canal de mensagens, sincronização ou runtime Hermes. O caminho do cofre, quando adotado, vem das instruções locais do Imperador e precisa de acesso confirmado em cada host. Metadados, regra escrita e pacote instalado não comprovam comportamento de agentes ou controles de produção.
