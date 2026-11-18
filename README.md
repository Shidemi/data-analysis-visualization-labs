# Технологии анализа и визуализации данных

| Работа | Тема | Основная среда | Датасеты |
| --- | --- | --- | --- |
| 1 | Настройка среды разработки и управление виртуальными окружениями | Anaconda Jupyter Notebook | Iris, Wine |

## Лабораторная работа 1

- [Отчёт для защиты](lab1/report.docx) — сохранённая версия с титульным листом БГУ ФПМИ.
- [Блокнот Anaconda](lab1/lab1_anaconda.ipynb) — исходные результаты работы с таблицами pandas, два графика и контрольное обучение модели.
- [HTML-экспорт](lab1/lab1_anaconda.html) — копия блокнота для просмотра в браузере.
- [CSV](lab1/data), [графики](lab1/figures) и [вывод команд](lab1/outputs), включая [список пакетов conda](lab1/outputs/03_conda_list_lab1_terminal.txt).
- [Блокнот Colab](lab1/lab1_colab.ipynb) — фактические версии пакетов и диагностика двух облачных сеансов.

В отчёте сохранено исходное описание Colab. Результаты облачной проверки находятся в блокноте Colab. В сеансе Tesla T4 проверены пять библиотек и видеопамять 15 360 МиБ. В отдельном сеансе TPU v5e-1 JAX обнаружил одно устройство TPU v5 lite. Для проверки Navigator отдельно создано и активировано окружение `dp2_lab01_gui`. В нём через Navigator установлены seaborn и scikit-learn вместе с numpy, pandas и matplotlib-base.

### Запуск блокнота Anaconda

```bash
conda create -n lab1_terminal python=3.11 numpy pandas matplotlib seaborn scikit-learn notebook ipykernel
conda activate lab1_terminal
python -m ipykernel install --user --name lab1_terminal --display-name 'Python (lab1_terminal)'
cd lab1
jupyter notebook
```

Откройте `lab1_anaconda.ipynb` и выберите ядро **Python (lab1_terminal)**. Если окружение уже есть, начните с его активации. Для повторения облачной проверки загрузите `lab1_colab.ipynb` в Google Colab и запустите ячейки аудита в соответствующих сеансах GPU и TPU.

[Условия курса](AGENTS.md). Следующие работы размещаются в папках `lab2/`, `lab3/` и далее.
