
import random
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

# 성공 확언 리스트
affirmations = [
    "나는 매일 더 나은 기회를 창출하고 있다.",
    "모든 도전은 나를 성공으로 이끄는 발판이다.",
    "나는 목표를 명확히 알고, 이를 달성하기 위해 꾸준히 노력한다.",
    "내 삶은 긍정적인 에너지로 가득 차 있다.",
    "오늘 나는 내 꿈에 한 걸음 더 가까워졌다.",
    "나는 충분히 유능하고, 필요한 모든 자원을 가지고 있다.",
    "모든 행동은 나의 비전을 실현시키는 데 기여한다.",
    "나는 변화를 환영하고, 성장의 기회를 최대한 활용한다.",
    "내가 하는 모든 일은 성공으로 이어진다.",
    "나는 내 능력을 믿고, 최고의 성과를 만들어낸다."
]

class ChecklistApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # 오늘 날짜 기반으로 확언 선택
        today = datetime.now().date()
        random.seed(today.toordinal())  # 매일 같은 확언이 나오도록 설정
        daily_affirmation = random.choice(affirmations)

        # 확언 표시
        affirmation_label = Label(
            text=f"[b]{daily_affirmation}[/b]",
            size_hint=(1, 0.2),
            halign="center",
            valign="middle",
            markup=True
        )
        layout.add_widget(affirmation_label)

        # 체크리스트 생성
        checklist_items = [
            "성공한 평범한 사람 10명 리스트 작성",
            "성공 사례별 핵심 성공 요인 분석",
            "성공 사례 공통 패턴 도출",
            "나만의 차별화 전략 수립"
        ]
        
        for item in checklist_items:
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            checkbox = CheckBox()
            label = Label(text=item, halign="left", valign="middle")
            row.add_widget(checkbox)
            row.add_widget(label)
            layout.add_widget(row)
        
        # 초기화 버튼
        reset_button = Button(text="체크리스트 초기화", size_hint=(1, 0.1))
        reset_button.bind(on_press=self.reset_checklist)
        layout.add_widget(reset_button)
        
        return layout
    
    def reset_checklist(self, instance):
        # 간단히 UI를 다시 로드하는 방식으로 초기화
        self.root.clear_widgets()
        self.build()

if __name__ == "__main__":
    ChecklistApp().run()
