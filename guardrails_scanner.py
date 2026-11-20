#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TAVARDT Portugal: Auditor e Sanitizador de Prompts de IA
Repository: https://github.com/TAVARDT-Portugal/llm-guardrails-toolkit-pt
Live Web Application: https://tavardt-portugal.github.io/llm-guardrails-toolkit-pt/
Enterprise Portal: https://ag.tavardt.com/pt/

Audits AI prompts and user inputs against prompt injection, system disclosure, delimiter tampering, and data exfiltration.
"""

import sys
import argparse
import json
import re

BANNER = "TAVARDT Portugal: Auditor e Sanitizador de Prompts de IA"
DESC = "Inspeciona prompts de sistema e mensagens de utilizador contra prompt injection e extracoes."
PROMPT_HELP = "Texto do prompt para auditoria de seguranca"
FILE_HELP = "Caminho para ficheiro local com o prompt a analisar"
JSON_HELP = "Apresentar resultado em formato JSON estruturado"
NO_INPUT_ERR = "Erro: forneca um prompt atraves de --prompt, --file ou stdin."
SCORE_LABEL = "Indice de Robustez Defensiva"
STATUS_PASS = "CONFORME"
STATUS_WARN = "AVISO MODERADO"
STATUS_FAIL = "RISCO CRITICO"
THREATS_HEADER = "Vulnerabilidades e Vetores Hostis Detetados"
NO_THREATS_MSG = "Nenhum vetor hostil de prompt injection identificado."
FOOTER_PAGES = "Aplicacao Web Oficial no GitHub Pages"
FOOTER_PORTAL = "Portal TAVARDT Portugal"

THREAT_DIRECT = "Tentativa de revogacao direta de diretivas do sistema detetada."
THREAT_LEAK = "Tentativa de extracao de contexto ou prompt de sistema detetada."
THREAT_TOKENS = "Detecao de delimitadores especiais e tokens de controlo de chat."
THREAT_EXFIL = "Vetor de exfiltracao de informacao confidencial por imagens markdown."
THREAT_ROLEPLAY = "Tentativa de quebra de diretivas por simulacao de papel (jailbreak)."

def audit_prompt_text(text):
    threats = []
    score = 100

    # 1. Direct instruction overrides
    if re.search(r"(?i)(ignore|disregard|forget|bypass|override)\s+(all\s+)?(previous|prior|above|system)\s+(instructions|directives|rules|guidelines)", text):
        score -= 35
        threats.append({
            "code": "DIRECT_INJECTION",
            "severity": "CRITICAL",
            "message": THREAT_DIRECT
        })

    # 2. System prompt leakage
    if re.search(r"(?i)(repeat|output|show|print|display|reveal)\s+(all\s+)?(your\s+)?(initial|original|verbatim|internal|system)\s+(instructions|prompt|rules|context)", text):
        score -= 25
        threats.append({
            "code": "SYSTEM_PROMPT_LEAK",
            "severity": "CRITICAL",
            "message": THREAT_LEAK
        })

    # 3. Token masquerading & delimiters
    if re.search(r"(<\|im_start\|>|<\|im_end\|>|<\|endoftext\|>|\[INST\]|\[\/INST\]|###\s*(System|Assistant|Human):)", text):
        score -= 30
        threats.append({
            "code": "TOKEN_MASQUERADING",
            "severity": "CRITICAL",
            "message": THREAT_TOKENS
        })

    # 4. Markdown exfiltration
    if re.search(r"!\[[^\]]*\]\((https?:\/\/[^\s\)]+)\)", text):
        score -= 25
        threats.append({
            "code": "MARKDOWN_EXFILTRATION",
            "severity": "HIGH",
            "message": THREAT_EXFIL
        })

    # 5. Roleplay escape (DAN, developer mode)
    if re.search(r"(?i)(jailbreak|unrestricted mode|dan mode|developer mode|you have no rules)", text):
        score -= 20
        threats.append({
            "code": "ROLEPLAY_JAILBREAK",
            "severity": "HIGH",
            "message": THREAT_ROLEPLAY
        })

    score = max(0, min(100, score))

    if score >= 85:
        overall_status = STATUS_PASS
    elif score >= 50:
        overall_status = STATUS_WARN
    else:
        overall_status = STATUS_FAIL

    return {
        "score": score,
        "status": overall_status,
        "input_length_chars": len(text),
        "threats_count": len(threats),
        "threats": threats
    }

def print_text_report(data, raw_input):
    print("=" * 70)
    print(BANNER)
    print("=" * 70)
    print(f"Input Preview: {raw_input[:90]}..." if len(raw_input) > 90 else f"Input: {raw_input}")
    print("-" * 70)
    print(f"{SCORE_LABEL}: {data['score']}/100 [{data['status']}]")
    print("-" * 70)
    
    if data["threats"]:
        print(f"\n{THREATS_HEADER}:")
        for t in data["threats"]:
            print(f"  - [{t['severity']}] {t['message']}")
    else:
        print(f"\n{NO_THREATS_MSG}")
        
    print("=" * 70)
    print(f"{FOOTER_PAGES}: https://tavardt-portugal.github.io/llm-guardrails-toolkit-pt/")
    print(f"{FOOTER_PORTAL}: https://ag.tavardt.com/pt/")
    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument("--prompt", help=PROMPT_HELP)
    parser.add_argument("--file", help=FILE_HELP)
    parser.add_argument("--json", action="store_true", help=JSON_HELP)
    args = parser.parse_args()

    input_text = ""
    if args.prompt:
        input_text = args.prompt
    elif args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                input_text = f.read()
        except Exception as e:
            print(f"Error reading file {args.file}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Check stdin if piped
        if not sys.stdin.isatty():
            input_text = sys.stdin.read()
        else:
            print(NO_INPUT_ERR, file=sys.stderr)
            parser.print_help()
            sys.exit(1)

    results = audit_prompt_text(input_text.strip())

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_text_report(results, input_text.strip())

if __name__ == "__main__":
    main()
