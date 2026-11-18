# Технологии анализа и визуализации данных

| Работа | Тема | Основная среда | Датасеты |
| --- | --- | --- | --- |
| 1 | Настройка среды разработки и управление виртуальными окружениями | Anaconda Jupyter Notebook | Iris, Wine |
| 2 | Разведочный анализ данных | Anaconda Jupyter Notebook | Auto MPG, Palmer Penguins |
| 3 | Линейная регрессия | Anaconda Jupyter Notebook | Cars (R datasets), Advertising (ISL) |

## Лабораторная работа 1

- [Отчёт для защиты](lab1/report.docx) — версия с титульным листом БГУ ФПМИ, результатами аудита, снимками и графиками.
- [Блокнот Anaconda](lab1/lab1_anaconda.ipynb) — исходные результаты работы с таблицами pandas, два графика и контрольное обучение модели.
- [HTML-экспорт](lab1/lab1_anaconda.html) — копия блокнота для просмотра в браузере.
- [CSV](lab1/data), [графики](lab1/figures) и [вывод команд](lab1/outputs), включая [список пакетов conda](lab1/outputs/03_conda_list_lab1_terminal.txt).
- [Блокнот Colab](lab1/lab1_colab.ipynb) — фактические версии пакетов и диагностика двух облачных сеансов.
- [Снимки экрана](lab1/screenshots) — Anaconda Navigator, версии библиотек, выбор среды и результаты GPU и TPU.

В сеансе Tesla T4 проверены пять библиотек и видеопамять 15 360 МиБ. В отдельном сеансе TPU v5e-1 JAX обнаружил одно устройство TPU v5 lite. Для проверки Navigator отдельно создано и активировано окружение `dp2_lab01_gui`. В нём через Navigator установлены seaborn и scikit-learn вместе с numpy, pandas и matplotlib-base.

### Запуск блокнота Anaconda

```bash
conda create -n lab1_terminal python=3.11 numpy pandas matplotlib seaborn scikit-learn notebook ipykernel
conda activate lab1_terminal
python -m ipykernel install --user --name lab1_terminal --display-name 'Python (lab1_terminal)'
cd lab1
jupyter notebook
```

Откройте `lab1_anaconda.ipynb` и выберите ядро **Python (lab1_terminal)**. Если окружение уже есть, начните с его активации. Для повторения облачной проверки загрузите `lab1_colab.ipynb` в Google Colab и запустите ячейки аудита в соответствующих сеансах GPU и TPU.

## Лабораторная работа 2

- [Отчёт для защиты](lab2/report.docx) — подробный разбор каждого этапа работы с кодом ячеек, фактическим выводом, снимками Jupyter, таблицами результатов и пояснениями к девяти графикам.
- [Блокнот Anaconda](lab2/lab2_anaconda.ipynb) — аудит, очистка, распределения, выбросы и корреляции. Выводы ячеек и графики сохранены в блокноте.
- [Исходные данные](lab2/data) — Auto MPG, R. Quinlan ([UCI, CC BY 4.0](https://doi.org/10.24432/C5859H)), и Palmer Penguins, A. M. Horst, A. P. Hill, K. B. Gorman ([palmerpenguins, CC0](https://allisonhorst.github.io/palmerpenguins/)).
- [Графики](lab2/figures) — распределения, диаграммы размаха, тепловые карты и диаграммы рассеяния.
- [Снимки экрана](lab2/screenshots) — версии библиотек, аудит, очистка и сохранение результатов в Jupyter Notebook. Снимки 07–10 показывают итоговый вывод по выбросам и корреляциям для обоих наборов.
- [Таблицы результатов](lab2/outputs) — очищенные данные, матрицы корреляций Пирсона, границы и число выбросов по правилу IQR.

В Auto MPG шесть пропусков мощности заполнены медианой **93,5 л. с.** Сохранились все 398 строк, из которых 18 содержат статистические выбросы. В Palmer Penguins после удаления 11 неполных строк осталось 333 наблюдения. По общим границам IQR выбросов нет. Наиболее сильная связь в этом наборе — между длиной ласта и массой пингвина (**r = 0,873**).

### Запуск блокнота Anaconda

Используйте окружение `lab1_terminal` из первой работы. Если его ещё нет, создайте и зарегистрируйте ядро по инструкции выше. Затем из корня проекта выполните:

```bash
conda activate lab1_terminal
cd lab2
jupyter notebook
```

Откройте `lab2_anaconda.ipynb`, выберите **Python (lab1_terminal)** и выполните все ячейки. Блокнот загружает данные из локальных файлов и обновляет `figures/` и `outputs/`.

## Лабораторная работа 3

- [Отчёт для защиты](lab3/report.docx) — титульный лист БГУ ФПМИ, код, фактический вывод Jupyter, графики, таблицы и демонстрация симулятора.
- [Блокнот Anaconda](lab3/lab3_anaconda.ipynb) — парная регрессия Cars и три эксперимента Advertising с сохранёнными выводом и графиками.
- [Исходные данные](lab3/data) — Cars ([документация R](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/cars.html), [CSV из Rdatasets](https://vincentarelbundock.github.io/Rdatasets/csv/datasets/cars.csv)) и Advertising ([данные авторов ISL](https://www.statlearning.com/resources-first-edition)).
- [Графики](lab3/figures), [снимки экрана](lab3/screenshots) и [результаты](lab3/outputs) — метрики, коэффициенты Advertising, тестовые прогнозы и модель с тремя признаками.
- [Приложение Streamlit](lab3/app.py) — прогноз продаж по трём рекламным бюджетам и интерактивный график.

На Cars модель оценила прирост расстояния до остановки в **3,6857 фута** на 1 милю/ч. Тестовый R² составил **0,6158**. На Advertising вариант **TV + radio** показал лучшие тестовые метрики (MAE **1,4443**, MSE **3,1379**, R² **0,9006**) среди трёх комбинаций признаков на одних и тех же 40 тестовых строках.

### Запуск блокнота Anaconda

Используйте окружение `lab1_terminal` из первой работы. Из корня проекта выполните:

```bash
conda activate lab1_terminal
cd lab3
jupyter notebook
```

Откройте `lab3_anaconda.ipynb`, выберите ядро **Python (lab1_terminal)** и выполните все ячейки. Блокнот использует локальные CSV и обновляет `figures/` и `outputs/`.

### Запуск симулятора

В окружении с Python 3.11 выполните из корня репозитория:

```bash
python -m pip install -r lab3/requirements-app.txt
python -m streamlit run lab3/app.py
```

Приложение загружает модель из `lab3/outputs/advertising_model.joblib`. Ползунки меняют бюджеты, а список над графиком выбирает канал, для которого показана линия прогноза.

[Условия курса](AGENTS.md). Следующие работы размещаются в папках `lab4/` и далее.
