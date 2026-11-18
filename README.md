# Технологии анализа и визуализации данных

| Работа | Тема | Основная среда | Датасеты |
| --- | --- | --- | --- |
| 1 | Настройка среды разработки и управление виртуальными окружениями | Anaconda Jupyter Notebook | Iris, Wine |

Google Colab используется в работе № 1 для аудита облачной среды и ускорителей.

- [Блокнот Anaconda](lab1/anaconda.ipynb) — версии пакетов, аудит компьютера, таблицы и два графика.
- [Блокнот Colab](lab1/colab.ipynb) — версии пакетов и диагностика GPU и TPU.
- [Полный список пакетов conda](lab1/conda-list.txt) — вывод команды `conda list` в терминальном окружении.
- [Отчёт для защиты](lab1/report.docx)
- [Условия курса](AGENTS.md)

## Запуск в Anaconda

```bash
conda create -n lab1_terminal python=3.11
conda activate lab1_terminal
conda install numpy pandas matplotlib seaborn scikit-learn notebook psutil
conda list
jupyter notebook
```

Откройте `lab1/anaconda.ipynb`. Iris и Wine поставляются со scikit-learn. Для аудита облачного оборудования откройте `lab1/colab.ipynb` в Google Colab и следуйте инструкциям в ячейках.

Последующие лабораторные работы размещаются в каталогах `lab2/`, `lab3/` и далее.
