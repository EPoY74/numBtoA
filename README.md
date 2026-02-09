# Maximize A using digits from B (Python + uv)

Проект решает задачу по **максимизации строкового числа `A`** за счёт **замены цифр** на цифры из строки `B` при ограничении: **каждую цифру из `B` можно использовать только один раз**.  
Формат репозитория удобен для практики тем **алгоритмы**, **строки**, **жадные стратегии (greedy)**, обработка **краевых случаев** и подготовка к задачам формата *coding challenge / interview*.

## Условие задачи

Даны два строковых представления чисел `A` и `B`. Нужно максимизировать `A`, заменяя в нём любую цифру на цифру из `B`. Каждую цифру `B` можно использовать только один раз.

Особенности (по твоим уточнениям):
- ✅ **Отрицательные числа допустимы** (`-` — знак, не цифра; не заменяется).
- ✅ **Ведущие нули допустимы и значимы** (например, `"0009"`, `"-0120"`).

> ⚠️ ПРЕДПОЛАГАЮ: замен может быть **несколько** (пока есть доступные цифры в `B`).  
> Если по условию должна быть **ровно одна** замена — описание/алгоритм нужно подогнать под это правило.

## Структура проекта

```text
.
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

- `src/main.py` — точка входа и функция `main()`
- `tests/test_main.py` — тесты (pytest)
- `pyproject.toml` / `uv.lock` — окружение и зависимости через **uv**

## Требования

- Python **3.12+**
- **uv** (устанавливается глобально)

---

# Установка uv (глобально) — ОСНОВНОЙ СПОСОБ ✅

Ниже — несколько вариантов глобальной установки. Рекомендуемый путь — **официальный standalone installer** от Astral (он ставит `uv` в пользовательский PATH).

## Windows (PowerShell)

### Вариант A — официальный installer (рекомендуется)
Открой PowerShell и выполни:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Проверь установку:

```powershell
uv --version
```

> Если после установки команда `uv` не находится — закрой и открой терминал заново (обновится PATH).

### Вариант B — WinGet
```powershell
winget install --id=astral-sh.uv -e
```

### Вариант C — Scoop
```powershell
scoop install main/uv
```

---

## Linux (bash/zsh)

### Вариант A — официальный installer (рекомендуется)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Если `curl` нет:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

Проверь установку:

```bash
uv --version
```

> Если `uv` не находится — перезапусти терминал или перечитай профиль (`~/.bashrc`, `~/.zshrc`).

---

## Альтернативный способ (когда нельзя запускать скрипты)

### Через pipx (глобально, изолировано)
```bash
pipx install uv
```

### Через pip (глобально, но менее предпочтительно)
```bash
python -m pip install -U uv
```

---

# Работа с проектом (uv)

## Установка зависимостей

В корне репозитория:

```bash
uv sync
```

> `uv sync` устанавливает зависимости проекта согласно `pyproject.toml` и фиксирует/использует lock-файл `uv.lock` для воспроизводимости окружения.

## Запуск приложения

### Linux
```bash
uv run python src/main.py
```

### Windows (PowerShell)
```powershell
uv run python .\src\main.py
```

## Запуск тестов

### Linux
```bash
uv run pytest -q
```

### Windows (PowerShell)
```powershell
uv run pytest -q
```

---

## Текущее состояние реализации

Сейчас `main()` является **заглушкой**: выводит входные значения и возвращает `"1"`.
После добавления алгоритма README останется актуальным (интерфейс `main(numA: str, numB: str) -> str` уже задан).

---

## Тэги (topics)

python, uv, algorithms, greedy, strings, digit-replacement, maximize-number, optimization, coding-challenge, interview-problem, pytest, leading-zeros, negative-numbers
