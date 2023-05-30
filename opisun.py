import requests
from bs4 import BeautifulSoup
from lxml import html

class Opis:
    opisanie = 'Нижегородский государственный педагогический университет имени Козьмы Минина (Мининский университет) — вуз с богатыми традициями: ' \
               'учительский институт был основан в нашем городе в 1911 году, три четверти учителей в Нижегородской области ' \
               '— наши выпускники. Кроме того, среди наших студентов — психологи и лингвисты, инженеры и управленцы, художники и дизайнеры.\n ' \
               'Сегодня Мининский университет активно развивается, чтобы соответствовать современным требованиям и образовательным стандартам, ' \
               'удовлетворять потребности личности в непрерывном обучении, отвечать актуальным задачам общественного и государственного развития.' \
               'Мы реализуем амбициозные проекты: построение комплексной системы гарантий качества образования, открытие новых направлений и программ подготовки, информатизация деятельности вуза.' \
               'Расширяется международное сотрудничество: в настоящее время в университете учатся студенты из 27 стран мира. ' \
               'Совместно с другими образовательными учреждениями и научными центрами, общественными организациями и органами управления мы активно участвуем в научно-исследовательской деятельности (прежде всего, в области педагогики,' \
               'управления образованием, прикладной психологии, философии), стремимся быть центром воспитания гражданского самосознания и генерации социальных инициатив.\n ' \
               'Мы прилагаем все усилия для того, чтобы совершенствовать региональную и национальную систему образования,' \
               ' стать элементом международного образовательного процесса, подготовить педагога нового типа, понимающего себя и общество, ' \
               'личность, способную обеспечить развитие человека в течение всей жизни.'