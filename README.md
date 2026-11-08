# Создаем навык ИИ-агента на примере записей архитектурных решений ADRs
Мастерская Skill Crafting на конференции Analyst Days 23, 20-21 ноября 2026, Москва

## Учебный курс
[Навыки AI-агентов для аналитиков и ИТ-архитекторов](https://www.itexpert.ru/aiask-online/)


## Структура репозитория
Репозиторий содержит семь последовательных версий скилла генерации Y-Statement ADR.

| Версия | Описание |
| --- | --- |
| `v0.1-inversion` | Базовая версия с **inversion pattern**. ADR генерируется только при наличии всех шести частей Y-Statement; при неполных данных задаётся один вопрос со всеми недостающими частями, максимум три попытки на ADR. |
| `v0.2-draft` | Минимальный скилл генерации черновика. Отказ от строгого контроля всех шести частей: пропуски обозначаются `—` и превращаются в задачи на доработку. |
| `v0.3-file` | Сохранение черновика плюс запись ADR в Markdown-файл в каталоге `adr/`. Автоматический номер записи (`scripts/next-adr-number.py`) и имя файла с номером и латинским `kebab-case` slug. |
| `v0.4-template` | Формат ADR вынесен из `SKILL.md` во внешний шаблон `assets/adr-template.md`; раздел `Формат` ссылается на шаблон и правила заполнения `{tasks_section}`. |
| `v0.5-validation` | Добавлена обязательная проверка ADR перед сохранением; чек-лист вынесен в `references/validation-checklist.md`. |
| `v0.6-trace` | Добавлено дописывание протокола в корневой `trace.md`: источник, reasoning trace, mapping, validation и путь ADR; предыдущие записи сохраняются. |
| `v0.7-techradar` | Добавлена сверка технологий решения с локальным Tech Radar (`references/techradar.csv`): ринг, квадрант и роль технологии; результат пишется в `trace.md`; добавлен демонстрационный CSV из 10 технологий. |

## Полезные ссылки
- [Agent Skills](https://agentskills.io/)
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
- [5 Agent Skill design patterns](https://x.com/GoogleCloudTech/status/2033953579824758855)
- [Introducing SkillsBench: The First Benchmark for Agent Skills](https://www.skillsbench.ai/blogs/introducing-skillsbench#self-generated-skills-barely-help) 


