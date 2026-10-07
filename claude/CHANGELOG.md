# Crônicas do Khanato

## Edição pública — distribuição 2026.10.06-1

Mesmo método da 2.0.0. Referências pessoais e caminhos locais foram generalizados; o cofre Obsidian passa a ser opcional e indicado nas instruções locais. Pacotes regenerados das fontes desta edição.

## 2.0.0 — Paridade de método com o Codex — 03/10/2026

Núcleo derivado de `2026.10.03-hermes-v1`; adaptação Claude `2026.10.03-claude-v1`. Mantidos os seis IDs de skills e 50 IDs de agentes, agora ligados às mesmas competências canônicas. A sessão principal executa e integra; equipe, revisão e delegação são proporcionais à tarefa.

Incorporados Constituição vigente, segurança de aplicações, formatos Obsidian, avaliação, memória, retomada e métodos Hermes. Adaptadores específicos tratam Cartographer e diferenças Code/Cowork/Chat. Sem hooks, MCP, serviços, permissões ampliadas ou modelo fixado.

Os registros abaixo descrevem versões históricas, inclusive regras posteriormente substituídas. Para execução, prevalecem `skills/khanato/SKILL.md` e suas referências atuais. Pacote instalado não comprova comportamento nem ativação em outra sessão.

Registro das expansões do império, por decreto do Imperador.

## 1.2.0 — Nous, Divisão de Inteligência Artificial

Diretora de IA **Minerva** + 8 especialistas sêniores: Cientista de Dados, Eng. de Machine Learning, Eng. de IA Generativa/LLM, Eng. de Agentes & Orquestração, Eng. de MLOps, Eng. de Avaliação (AI Evals), Segurança de IA (AI Red Team) e Governança, Ética e Conformidade de IA. Skill `nous`.

Três princípios gravados na divisão: (1) a triagem começa perguntando **se o problema precisa de IA** — dizer que não é entrega legítima; (2) **nada vai a produção sem veredito do Eng. de Avaliação**, que mede taxa de alucinação contra golden dataset; (3) o Artigo 5 vale em dobro, porque esta é a divisão onde agentes de IA opinam sobre IA — o terreno onde a alucinação é mais confortável.

Fronteiras declaradas com Vetra (guarda o dado × aprende com o dado), Vigil (código × modelo), Curia (traduz × dá a palavra jurídica) e as empresas (constrói pipeline × consome e devolve modelo).

Total: **50 agentes**, 6 skills. Sete divisões.

## 1.1.0 — Curia ganha Sucessões & Patrimônio

Novo assento na Curia: **Advogado(a) Sênior de Sucessões, Patrimônio & Família Patrimonial** — herança, inventário e partilha (judicial e extrajudicial), testamento, legítima e herdeiros necessários, ITCMD (estadual, sempre a verificar por UF), planejamento sucessório em vida, holding familiar, doação com usufruto, regimes de bens, meação × herança, união estável, sucessão de empresa familiar, transição de bens e herança digital.

Exigência gravada no agente: **atualização permanente** — verificação do estado atual da legislação federal e estadual, dos entendimentos dos tribunais superiores e das normas de cartório antes de cada parecer, com fonte oficial e data-base declaradas. O que vier só da memória sai marcado `[VERIFICAR — pode estar desatualizado]`.

Total: **41 agentes**, 5 skills. Curia passa de 5 para 6 integrantes.

## 1.0.0 — Império consolidado

Selo da estrutura completa: **41 agentes** (o Grande Khan + 16 papéis de empresa + 5 juristas + 8 marqueteiros + 10 da Vigil, sendo o `dev-senior` instanciável 5 vezes em paralelo) e **5 skills** de orquestração.

- Organograma corrigido: as três empresas (Forja, Vetra, Bastion) agora nomeadas explicitamente, com o bloco interno de 16 papéis separado do tronco imperial.
- Constituição fechada em 6 artigos, gravada em todos os agentes.
- Adendo do Social Media incorporado (atualização permanente de plataformas + letalidade competitiva).

## 0.5.2 — Adendo imperial ao Social Media

Obrigação de atualização permanente sobre políticas, regras de publicidade, APIs (escopos, rate limits, depreciações), formatos e integrações de cada rede, com fonte oficial e data-base. Letalidade competitiva definida como execução — contra desconhecimento, lentidão, mediocridade e o próprio erro — com limite inviolável: jamais contra pessoas.

## 0.5.1 — Correção de manifesto

Descrição do plugin reduzida para caber no limite de 500 caracteres.

## 0.5.0 — Vigil, Divisão de Segurança & Operações

Diretor(a) de Segurança **Aquila** + 9 especialistas: SOC, NOC, Blue Team, Red Team, Purple Team, Threat Intelligence, DFIR, GRC e AppSec. Lei zero: ética white-hat absoluta. Cultura: presunção de comprometimento. Skill `vigil`.

## 0.4.0 — Artigo 6: Desconfie de Todos

Dupla verificação obrigatória (revisão do superior + auditoria do Khan em dois passes, com reverificação das correções) e classificação de confiabilidade de fontes (A oficial/primária, B secundária idônea, C fraca — C sozinha não sustenta afirmação crítica). Gravado em todos os agentes, inclusive no próprio Khan.

## 0.3.0 — Arauto, Agência de Marketing

CMO **Aurora** + 7 especialistas: Estrategista de Marca, Redator, SEO, Tráfego Pago, Social Media, Analista de Marketing e Designer de Marca. Regras: nenhum claim sem fonte, nenhuma campanha sem métrica definida a priori, publicidade enganosa é crime capital. Skill `arauto`.

## 0.2.0 — Curia, Escritório Jurídico

Conselheiro-Geral **Ulpiano** + 4 advogados sêniores: LGPD & Privacidade, Contratual, Trabalhista (CLT/vínculos) e Generalista de Direito Brasileiro. Citações marcadas para verificação; todo parecer declara o que exige advogado inscrito na OAB. Skill `curia`.

## 0.1.0 — Fundação

Grande Khan **Temüjin** (distribuidor, voz do contra, auditor anti-alucinação) e três empresas: **Forja** (CEO Dante — Produto), **Vetra** (CEO Ada — Dados), **Bastion** (CEO Magno — Plataforma & Infra), cada uma com 16 papéis. Constituição com 5 artigos: PostgreSQL sempre, 5FN sempre, nomes amigáveis em inglês, PKs `gen_random_uuid()` (UUID v4) e anti-alucinação. Skills `khanato` e `voz-do-contra`.

---

**Nota sobre atualização — corrigida em 2.0.0:** a orientação antiga de remover o plugin antes de toda atualização foi substituída. O comportamento depende da superfície e da versão do instalador; confira o estado exibido e siga o [guia atual](README.md).
