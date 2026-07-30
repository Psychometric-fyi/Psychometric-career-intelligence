# Psychometric Career Intelligence 🧠🎯

[![npm](https://img.shields.io/npm/v/@psychometric-fyi/career-intelligence)](https://npmjs.com/package/@psychometric-fyi/career-intelligence)
[![PyPI](https://img.shields.io/pypi/v/psychometric-career-intelligence)](https://pypi.org/project/psychometric-career-intelligence)
 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21710607.svg)](https://doi.org/10.5281/zenodo.21710607)

Psychometric Career Intelligence is an educational resource that explores the science of psychometric assessments and career decision making. It explains how personality traits, cognitive abilities, interests, and motivations shape learning, career choices, and personal growth. Built by [Psychometric.fyi](https://psychometric.fyi).

## Features

- Personality Trait Score — evaluates personality dimensions shaping career fit
- Cognitive Ability Score — measures reasoning, problem solving, and learning potential
- Interest Alignment Score — matches personal interests with career pathways
- Motivation Clarity Score — identifies intrinsic motivators driving career decisions
- Strength Discovery Score — uncovers core strengths and natural talents
- Career Readiness Score — assesses overall readiness for academic and professional paths
- Assessment Types — personality, cognitive, interest, motivation, aptitude, and DMIT
- CLI support in Node.js and Python
- Benchmark dataset included (20 psychometric assessment cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @psychometric-fyi/career-intelligence
npx psychometric-career "student-profile" personality 82 78 85 74 88 76
```

### Python

```bash
pip install psychometric-career-intelligence
python -m career_intel "student-profile" personality 82 78 85 74 88 76
```

## Output

```
Profile: student-profile
Assessment Type: Personality
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Personality Trait Score:       82 / 100  [Healthy]
Cognitive Ability Score:       78 / 100  [Healthy]
Interest Alignment Score:      85 / 100  [Excellent]
Motivation Clarity Score:      74 / 100  [Healthy]
Strength Discovery Score:      88 / 100  [Excellent]
Career Readiness Score:        76 / 100  [Healthy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Career Intelligence:   81 / 100
Priority Action:               Motivation Clarity (lowest — act first)

Recommended Career Pathways:
  STEM & Technology:       82 / 100
  Creative & Design:       78 / 100
  Business & Leadership:   85 / 100
  Social & Education:      80 / 100
```

## Assessment Types

| Type | Description |
|------|-------------|
| personality | Big Five personality traits and career alignment |
| cognitive | Reasoning, problem solving, and learning ability |
| interest | Holland codes and career interest mapping |
| motivation | Intrinsic and extrinsic motivation profiling |
| aptitude | Specific skills and academic aptitude assessment |
| dmit | Dermatoglyphics Multiple Intelligence Test |
| emotional | Emotional intelligence and interpersonal skills |
| values | Core values and workplace culture alignment |

## Project Structure

```
Psychometric-career-intelligence/
├── index.ts                  # TypeScript career intelligence
├── career_intel.py           # Python career intelligence
├── setup.py                  # PyPI setup config
├── pyproject.toml            # PyPI build config
├── package.json              # NPM package config
├── package-lock.json         # NPM lock file
├── tsconfig.json             # TypeScript config
├── schema.json               # JSON-LD structured data
├── zenodo.json               # Zenodo metadata
├── heartbeat.txt             # Auto-updated daily
├── mkdocs.yml                # ReadTheDocs config
├── .readthedocs.yaml         # ReadTheDocs build config
├── docs/
│   ├── index.md              # Documentation
│   └── requirements.txt
├── dataset/
│   └── psychometric_benchmarks.csv
├── .github/workflows/
│   ├── heartbeat.yml
│   ├── npm-publish.yml
│   └── pypi-publish.yml
├── README.md
└── LICENSE
```

## Psychometric Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Personality Trait | Personality dimensions shaping career fit | 0–100 |
| Cognitive Ability | Reasoning, problem solving, learning potential | 0–100 |
| Interest Alignment | Personal interests matched to career pathways | 0–100 |
| Motivation Clarity | Intrinsic motivators driving career decisions | 0–100 |
| Strength Discovery | Core strengths and natural talents identified | 0–100 |
| Career Readiness | Overall readiness for academic and professional paths | 0–100 |

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate assessment and guidance required |
| 31–60 | At Risk | Active career counselling needed |
| 61–80 | Healthy | On track with targeted development |
| 81–100 | Excellent | Strong career intelligence — ready to act |

## Keywords

Psychometric Assessment · Career Intelligence · Personality Test · Cognitive Ability · Interest Mapping · Career Guidance · Strength Discovery · DMIT · Career Readiness · Psychometric.fyi

## Links

| Platform | URL |
|----------|-----|
| Website | https://psychometric.fyi |
| GitHub | https://github.com/Psychometric-fyi/Psychometric-career-intelligence |
| GitHub Pages | https://psychometric-fyi.github.io/Psychometric-career-intelligence/ |
| NPM | https://npmjs.com/package/@psychometric-fyi/career-intelligence |
| PyPI | https://pypi.org/project/psychometric-career-intelligence |
| Hugging Face | https://huggingface.co/datasets/psychometric-fyi/career-intelligence-benchmarks |
| Zenodo | https://zenodo.org/records/21710607 |
| Docs | https://psychometric-career-intelligence.readthedocs.io |
| SlideShare | https://www.slideshare.net/slideshow/psychometric-fyi-research-backed-psychometric-assessments-for-student-career-academic-guidance/288900331 |
| Quora | https://www.quora.com/profile/Psychometric-Fyi |
| Pinterest | https://www.pinterest.com/psychometricfyi/ |
| Medium | https://medium.com/@psychometric-fyi |

## About Psychometric.fyi

Psychometric.fyi is an educational platform that explores the science of psychometric assessments and career decision making — helping students discover their strengths, identify suitable career paths, and make informed academic and professional decisions through evidence based insights.

## License

MIT — [Psychometric.fyi](https://psychometric.fyi)
