## ATV 13 - TDD - Desenvolvimento Dirigido a Teste

O objetivo desta atividade é desenvolvedor uma aplicação usando a prática de TDD, ou seja desenvolver os teste da aplicação mesmo antes do desenvolvimento do código real.

### Preparação do ambiente e rode os testes

```bash
# 1
uvicorn app.main:app --reload --port 8000

# 2
pytest
```