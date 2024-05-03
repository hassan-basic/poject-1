from kivy.app import App
from kivy.lang.builder import Builder
class Myapp(App):
    def build(self):return Builder.load_string("""Button:
        text:'click'
        on_release:self.text='exit' if self.text=='click' else setattr(self,'on_release',exit())
        """)
if __name__ == '__main__':Myapp().run()