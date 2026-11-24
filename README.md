# Toolkit de Guardrails e Sanitização de Prompts para LLM

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-5b3cf5.svg)](https://tavardt-portugal.github.io/llm-guardrails-toolkit-pt/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![OWASP LLM](https://img.shields.io/badge/OWASP-LLM01%20Injection-red.svg)](https://owasp.org/)
[![NIST AI](https://img.shields.io/badge/NIST-AI%20RMF-blue.svg)](https://www.nist.gov/itl/ai-risk-management-framework)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Camada de Proteção Ativa contra Injeção de Prompts, Fuga de Contexto e Exfiltração de Dados em Aplicações de IA**

Desenvolvido e mantido pela divisão de engenharia de defesas adversariais da TAVARDT Portugal.

***

## Portais e Demonstração Online

Aceda à ferramenta interativa oficial e aos canais soberanos da TAVARDT:

* **Aplicação Web Oficial no GitHub Pages**: [https://tavardt-portugal.github.io/llm-guardrails-toolkit-pt/](https://tavardt-portugal.github.io/llm-guardrails-toolkit-pt/)
* **Portal Institucional**: [https://ag.tavardt.com/pt/](https://ag.tavardt.com/pt/)
* **Central de Ferramentas**: [https://tools.tavardt.com/pt/](https://tools.tavardt.com/pt/)

***

## Blueprints Técnicos e Recursos Disponíveis

1. **Aplicação Web Interativa**: Diagnóstico determinístico, cálculo de postura defensiva e recomendações imediatas no navegador.
2. **Utilitário CLI Local**: Script Python determinístico executado diretamente no ambiente de produção para auditoria offline.
3. **Especificações de Segurança**: Manifestos e configurações de hardening em conformidade com as normas internacionais.

***

## Uso do Utilitário CLI Determinístico

Para executar a inspeção técnica no ambiente local:

```bash
git clone https://github.com/TAVARDT-Portugal/llm-guardrails-toolkit-pt.git
cd llm-guardrails-toolkit-pt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 scanner.py -json
```

***

## Links Úteis

* **Portal Corporativo:** https://ag.tavardt.com/pt/
* **Suíte de Diagnósticos:** https://tools.tavardt.com/pt/
* **Contacto Técnico:** https://ag.tavardt.com/pt/contacto/

***

© 2026 TAVARDT Portugal. Todos os direitos reservados. Soberania e Defesa de Infraestrutura.
