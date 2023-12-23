# Main.

from flet import app, Page, Text, ElevatedButton, Checkbox, ProgressRing, Slider, Dropdown, dropdown, ListView, PieChart, PieChartSection, matplotlib_chart, Row, Theme, colors

from flet_restyle import FletReStyle, FletReStyleConfig

from pytime_manager import time_thread, do_inf

from questions import questions, correct

from methods import Random, RandomWeights, EachNew, EachNewReversed, EachOdd, EachEven, choice

from matplotlib.pyplot import subplots


l_figure, l_ax = subplots()

def average(_list: list) -> float:
    """Get average number in list."""
    return sum(_list) / len(_list)

def main(page: Page) -> None:
    theme_config = FletReStyleConfig()

    theme_config.theme = Theme('teal900')

    theme_config.custom_title_bar_title = 'QuestionAnswerResearch'

    page.title = 'QuestionAnswerResearch'

    page.window_width = 1210
    page.window_height = 900

    page.window_min_width = 1210
    page.window_min_height = 900

    FletReStyle.apply_config(page, theme_config)

    def calculate(_):
        if method != 'All':
            correct_answers = []

            for _iterated in range(iterations_per_method):
                if method == 'Random':
                    answers = Random.solve(questions)

                elif method == 'RandomWeights':
                    answers = RandomWeights.solve(questions)

                elif method == 'EachNew':
                    answers = EachNew.solve(questions)

                elif method == 'EachNewReversed':
                    answers = EachNewReversed.solve(questions)

                elif method == 'EachOdd':
                    answers = EachOdd.solve(questions)

                elif method == 'EachEven':
                    answers = EachEven.solve(questions)

                correct_answers.append(correct(questions, answers)[1])

                iterated.value = _iterated

                page.update()

            color = getattr(colors, choice(dir(colors)))

            chart.sections = [
                PieChartSection(
                    average(correct_answers) + (0.0001 if method == 'EachNewReversed' else 0),

                    title=f'{method} ({average(correct_answers)}).',

                    color=color if isinstance(color, str) else 'red',

                    radius=90
                )
            ]

            page.update()

        else:
            correct_answers = [[], [], [], [], [], []]

            methods = [Random, RandomWeights, EachNew, EachNewReversed, EachOdd, EachEven]

            for _method in methods:
                for _ in range(iterations_per_method):
                    correct_answers[methods.index(_method)].append(correct(questions, _method.solve(questions))[1])

            chart.sections = [
                PieChartSection(
                    average(correct_answers[0]),

                    title=f'Random ({average(correct_answers[0])}).',

                    color='red',

                    radius=90
                ),

                PieChartSection(
                    average(correct_answers[1]),

                    title=f'RandomWeights ({average(correct_answers[1])}).',

                    color='green',

                    radius=90
                ),

                PieChartSection(
                    average(correct_answers[2]),

                    title=f'EachNew ({average(correct_answers[2])}).',

                    color='blue',

                    radius=90
                ),

                PieChartSection(
                    average(correct_answers[3]) + 0.0001,

                    title=f'EachNewReversed ({average(correct_answers[3]) + 0.0001}).',

                    color='yellow',

                    radius=90
                ),

                PieChartSection(
                    average(correct_answers[4]),

                    title=f'EachOdd ({average(correct_answers[4])}).',

                    color='orange',

                    radius=90
                ),

                PieChartSection(
                    average(correct_answers[5]),

                    title=f'EachEven ({average(correct_answers[3])}).',

                    color='purple',

                    radius=90
                ),
            ]

            page.update()

            return correct_answers

    def upd_method(_):
        nonlocal method

        method = method_dropdown.value

    def upd_iters(_):
        nonlocal iterations_per_method

        iterations_per_method = round(iterations_per_method_slider.value)

        iterations_per_method_label.value = f'{iterations_per_method} Iterations.'

        page.update()

    def _compare_all(_):
        nonlocal method

        method_dropdown.disabled = compare_all.value

        method = 'All' if compare_all.value else 'Random'

        page.update()

    def _refresh(_):
        nonlocal refresh

        refresh = refresh_checkbox.value

    iterations_per_method = 10

    method = 'Random'

    refresh = False    

    chart = PieChart([])

    chart_matplotlib = matplotlib_chart.MatplotlibChart(l_figure, expand=True)

    calculate_button = ElevatedButton('Calculate.', on_click=calculate)

    method_dropdown = Dropdown(
        options=[
            dropdown.Option('Random'),
            dropdown.Option('RandomWeights'),
            dropdown.Option('EachNew'),
            dropdown.Option('EachNewReversed'),
            dropdown.Option('EachOdd'),
            dropdown.Option('EachEven')
        ], on_change=upd_method, hint_text='Random'
    )

    compare_all = Checkbox(label='Compare all?', on_change=_compare_all)

    refresh_checkbox = Checkbox(label='Refresh?', on_change=_refresh)

    iterations_per_method_slider = Slider(min=10, max=1000, on_change=upd_iters)

    iterations_per_method_label = Text('1 Iterations.')

    iterated = ProgressRing(value=0, scale=0.9)

    most_correct = Text('Most Correct: ?')

    logs = ListView(expand=True, auto_scroll=True)

    page.add(
        chart,

        chart_matplotlib,

        Row([
            calculate_button,

            method_dropdown,

            compare_all,

            refresh_checkbox,

            iterations_per_method_slider,
            iterations_per_method_label,

            most_correct,

            iterated
        ]),

        logs
    )

    def _calculate():
        if compare_all.value and refresh:
            calc_out = calculate(None)

            if calc_out:
                methods = ['Random', 'RandomWeights', 'EachNew', 'EachNewReversed', 'EachOdd', 'EachEven']

                l_ax.clear()

                _most_correct = [average(sub) for sub in calc_out]

                most_correct.value = f'Most Correct: {max(_most_correct)}f ({methods[_most_correct.index(max(_most_correct))]}).'

                for index, correctness in enumerate(calc_out):
                    l_ax.plot(correctness, label=methods[index])

                    logs.controls.append(Text(f'{methods[index]} AV: {average(correctness)}f.'))

                l_ax.legend(loc='upper right')

                l_ax.set_xlabel('Iterations.')
                l_ax.set_ylabel('Average Correctness.')

                chart_matplotlib.figure = l_figure

    time_thread(do_inf(_calculate, 0.1), True)

app(main)
