# noinspection PyUnresolvedReferences
import toga
from colosseum import CSS


class MyApp(toga.App):
    def startup(self):
        main_window = toga.MainWindow(self.name)
        main_window.app = self

        main_box = toga.Box()

        toolbar = self.make_toolbar()
        main_box.add(toolbar)

        main_box.add(self.make_maincontent())

        main_window.content = main_box
        main_window.show()

    @staticmethod
    def make_toolbar():
        toolbar_box = toga.Box(style=CSS(
            flex_direction='row',
            justify_content='space-between',
            padding=5,
        ))

        refresh_btn = toga.Button('Refresh')
        summary_label = toga.Label('???%', alignment=toga.RIGHT_ALIGNED)
        toolbar_box.add(refresh_btn)
        toolbar_box.add(summary_label)

        return toolbar_box

    @staticmethod
    def make_maincontent():
        split = toga.SplitContainer(style=CSS(flex=1))
        left_container = toga.Box()

        tree = toga.Tree(['Fake File Navigator'])
        root1 = tree.insert(None, None, 'root1')
        tree.insert(root1, None, 'root1.1')
        root1_2 = tree.insert(root1, None, 'root1.2')
        tree.insert(root1_2, None, 'root1.2.1')
        tree.insert(root1_2, None, 'root1.2.2')
        tree.insert(root1_2, None, 'root1.2.3')

        codebox = MyApp.make_codebox()
        split.content = [tree, codebox]

        return split

    @staticmethod
    def make_codebox():
        code_box = toga.Box(style=CSS(flex=1))
        with open('make_a_window.py') as f:
            code_text = toga.MultilineTextInput(
                initial=f.read(),
                readonly = True,
                style=CSS(flex=1),
            )
        code_box.add(code_text)

        return code_box


if __name__ == '__main__':
    app = MyApp('Duvet', 'org.pybee.duvet')
    app.main_loop()
