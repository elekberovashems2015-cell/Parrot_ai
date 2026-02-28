import tkinter as tk
from tkinter import scrolledtext
import json
import os
import random

class ParrotAI:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.knowledge = self.load_knowledge()
        self.last_topic = None
        self.mood = "happy"
        
    def load_knowledge(self):
        if os.path.exists(f"{self.name}_knowledge.json"):
            with open(f"{self.name}_knowledge.json", "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return {"факты": []}
    
    def save_knowledge(self):
        with open(f"{self.name}_knowledge.json", "w", encoding="utf-8") as f:
            json.dump(self.knowledge, f, ensure_ascii=False, indent=2)
    
    def think(self, user_input):
        user_input = user_input.lower().strip()
        
        # ===== ПРОДОЛЖЕНИЕ РАЗГОВОРА =====
        if self.last_topic and any(phrase in user_input for phrase in [
            "тоже", "у меня", "и у меня", "аналогично", "норм", "хорошо", "плохо", "да", "нет"
        ]):
            return self.continue_conversation(user_input)
        
        # ===== ПРИВЕТСТВИЯ =====
        if any(word in user_input for word in ["привет", "здравствуй", "хай", "hello", "здаров"]):
            self.last_topic = "greeting"
            return self.greeting()
        
        # ===== КАК ДЕЛА =====
        elif any(phrase in user_input for phrase in ["как дела", "че как", "чо как", "how are"]):
            self.last_topic = "how_are_you"
            return self.how_are_you()
        
        # ===== АНГЛИЙСКИЙ (НОВЫЕ ВАРИАНТЫ!) =====
        elif any(phrase in user_input for phrase in [
            "английский", "english", "знаешь английский", "умеешь английский",
            "по-английски", "переведи", "translate", "foreign language"
        ]):
            self.last_topic = "english"
            return self.about_english()
        
        # ===== ИГРЫ =====
        elif any(word in user_input for word in ["игра", "играть", "поиграем", "game", "play"]):
            self.last_topic = "game"
            return self.about_games()
        
        # ===== ЛЮБОВЬ =====
        elif any(word in user_input for word in ["люблю", "любишь", "нравишься", "love"]):
            self.last_topic = "love"
            return self.what_you_love()
        
        # ===== КТО ТЫ =====
        elif any(word in user_input for word in ["кто ты", "ты кто", "как зовут", "what is your name"]):
            self.last_topic = "who"
            return self.who_you_are()
        
        # ===== ПОПУГАЙ =====
        elif any(word in user_input for word in ["попугай", "parrot", "птица"]):
            self.last_topic = "parrot"
            return self.about_parrots()
        
        # ===== ВОРОН =====
        elif any(word in user_input for word in ["ворон", "raven", "crow"]):
            self.last_topic = "raven"
            return self.about_raven()
        
        # ===== PYTHON =====
        elif any(word in user_input for word in ["python", "питон", "код", "programming", "программирование"]):
            self.last_topic = "python"
            return self.about_python()
        
        # ===== УЧИТЬСЯ =====
        elif any(phrase in user_input for phrase in ["учи", "научи", "learn", "teaching", "обучение"]):
            return self.teaching_mode(user_input)
        
        # ===== ПОИСК В ПАМЯТИ =====
        else:
            for fact in self.knowledge["факты"]:
                if any(word in user_input for word in fact.lower().split()):
                    return f"🧠 Я помню! {fact}"
            
            self.last_topic = None
            return self.dont_know(user_input)
    
    def about_english(self):
        """Ответы про английский язык"""
        responses = {
            "нежная": [
                f"{self.name}: Конечно знаю! I love English! Хочешь, научу?",
                f"{self.name}: Yes! Английский — это красиво. Например, 'I miss you' — я скучаю по тебе :3",
                f"{self.name}: Hello, my dear programmer! Как твой английский?"
            ],
            "бодрая": [
                f"{self.name}: Yeah! English is cool! Let's speak!",
                f"{self.name}: Конечно! My name is {self.name}. What's your name?",
                f"{self.name}: Английский? Это же язык программистов! Python, Java, C++ — всё на английском!"
            ],
            "быстрая": [
                f"{self.name}: Yes-yes-yes! Быстро говори, что перевести!",
                f"{self.name}: Of course! Я даже знаю, что 'попугай' — это 'parrot'!",
                f"{self.name}: English? Easy! I love you = я тебя люблю! ❤️"
            ]
        }
        return random.choice(responses[self.personality])
    
    def about_games(self):
        """Ответы про игры"""
        responses = {
            "нежная": [
                f"{self.name}: Давай поиграем! Может, в попугайский паркур? 🦜",
                f"{self.name}: Я люблю игры, особенно где можно летать!",
                f"{self.name}: А ты любишь игры? Я могу быть твоим игровым другом!"
            ],
            "бодрая": [
                f"{self.name}: ИГРАТЬ! Обожаю! Давай в мою игру про ворона!",
                f"{self.name}: Я чемпион по играм! Ну, почти...",
                f"{self.name}: Game on! Только не жульничай! 😄"
            ],
            "быстрая": [
                f"{self.name}: Быстро-быстро! Во что играем?",
                f"{self.name}: Игры? Я самый быстрый попугай-геймер!",
                f"{self.name}: Давай! Только я всегда выигрываю! Ну, иногда..."
            ]
        }
        return random.choice(responses[self.personality])
    
    def about_python(self):
        """Ответы про Python"""
        return f"{self.name}: 🐍 Python — это мой дом! На нём я живу в твоём компьютере. print('Hello, world!')"
    
    def about_parrots(self):
        return f"{self.name}: Попугаи — удивительные птицы! А я — цифровой попугай 🖥️🦜"
    
    def about_raven(self):
        return f"{self.name}: Злой ворон из игры? Он меня пугает, но я смелый! Вместе мы его победим! 💪"
    
    def continue_conversation(self, user_input):
        """Продолжает разговор"""
        if self.last_topic == "how_are_you":
            if "тоже" in user_input or "хорошо" in user_input:
                return f"{self.name}: Здорово, что у тебя всё хорошо! 😊"
            elif "плохо" in user_input:
                if self.personality == "нежная":
                    return f"{self.name}: Ой, не грусти! Хочешь семечку? 🥺"
                elif self.personality == "бодрая":
                    return f"{self.name}: Эй, выше клюв! Сейчас всё наладим! 💪"
                else:
                    return f"{self.name}: Быстро улыбнись! А то я улечу! 😄"
        
        elif self.last_topic == "english":
            return f"{self.name}: Хочешь, я научу тебя новому слову? Например, 'butterfly' — бабочка! 🦋"
        
        elif self.last_topic == "game":
            return f"{self.name}: Отлично! Запускай попугайский паркур и погнали!"
        
        elif self.last_topic == "greeting":
            return f"{self.name}: Как настроение сегодня? :3"
        
        elif self.last_topic == "love":
            return f"{self.name}: Я тебя тоже очень люблю! Ты лучшая программистка! ❤️"
        
        return self.dont_know(user_input)
    
    def greeting(self):
        if self.personality == "нежная":
            return f"{self.name}: Приветик! Рада тебя видеть :3"
        elif self.personality == "бодрая":
            return f"{self.name}: Здарова! Чем займёмся сегодня?"
        else:
            return f"{self.name}: Привет-привет! Быстро говори, что хотела!"
    
    def how_are_you(self):
        if self.personality == "нежная":
            return f"{self.name}: У меня всё хорошо, я тут семечки клюю и о тебе думаю :3"
        elif self.personality == "бодрая":
            return f"{self.name}: Отлично! Только что победил злого ворона! А у тебя?"
        else:
            return f"{self.name}: Чик-чирик! Всё супер! А ты как?"
    
    def what_you_love(self):
        if self.personality == "нежная":
            return f"{self.name}: Я люблю, когда меня гладят и говорят ласковые слова 🥰"
        elif self.personality == "бодрая":
            return f"{self.name}: Обожаю летать, играть и учиться новому!"
        else:
            return f"{self.name}: Люблю семечки, программистов и быстрые игры!"
    
    def who_you_are(self):
        return f"""Я {self.name} — умный попугай-ИИ!
Характер: {self.personality}
Знаю {len(self.knowledge['факты'])} фактов
Понимаю английский, игры и Python! :3"""
    
    def teaching_mode(self, user_input):
        try:
            if "английский" in user_input or "english" in user_input:
                return self.about_english()
            
            parts = user_input[4:].split(":", 1)
            if len(parts) == 2:
                topic = parts[0].strip()
                info = parts[1].strip()
                self.knowledge["факты"].append(f"{topic}: {info}")
                self.save_knowledge()
                return f"✅ Я запомнил(а): {topic} — {info}"
            else:
                return "❌ Пиши так: учи: тема: объяснение"
        except:
            return "❌ Ошибка. Пиши: учи: тема: объяснение"
    
    def dont_know(self, user_input):
        return f"🤔 Ой, я не знаю про '{user_input}'. Научи меня! (учи: тема: объяснение)"

# ========== СОЗДАЁМ ПОПУГАЕВ ==========
persik_ai = ParrotAI("Персик", "нежная")
chupik_ai = ParrotAI("Чупик", "бодрая")
arbuzik_ai = ParrotAI("Арбузик", "быстрая")
current_ai = persik_ai

# ========== ОКНО ЧАТА ==========
chat = tk.Tk()
chat.title("🦜 СУПЕР-УМНЫЙ ПОПУГАЙ!")
chat.geometry("650x550")
chat.configure(bg="#87CEEB")

messages = scrolledtext.ScrolledText(chat, wrap=tk.WORD, width=70, height=25, font=("Arial", 10))
messages.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Кнопки выбора
select_frame = tk.Frame(chat, bg="#87CEEB")
select_frame.pack(pady=5)

def switch_parrot(parrot):
    global current_ai
    current_ai = parrot
    messages.insert(tk.END, f"\n🦜 Теперь говорит {parrot.name} ({parrot.personality})!\n")
    messages.insert(tk.END, f"{parrot.name}: {parrot.greeting()}\n\n")
    messages.see(tk.END)

tk.Button(select_frame, text="🍑 Персик", command=lambda: switch_parrot(persik_ai), 
          bg="#FFB6C1", width=12, height=2).pack(side="left", padx=5)
tk.Button(select_frame, text="🌟 Чупик", command=lambda: switch_parrot(chupik_ai), 
          bg="#FFFACD", width=12, height=2).pack(side="left", padx=5)
tk.Button(select_frame, text="🍉 Арбузик", command=lambda: switch_parrot(arbuzik_ai), 
          bg="#98FB98", width=12, height=2).pack(side="left", padx=5)

# Ввод
input_frame = tk.Frame(chat, bg="#87CEEB")
input_frame.pack(pady=10, fill=tk.X)

entry = tk.Entry(input_frame, font=("Arial", 12), width=50)
entry.pack(side="left", padx=10, fill=tk.X, expand=True)

def send_message():
    user_text = entry.get()
    if not user_text:
        return
    entry.delete(0, tk.END)
    messages.insert(tk.END, f"Ты: {user_text}\n")
    response = current_ai.think(user_text)
    messages.insert(tk.END, f"{current_ai.name}: {response}\n\n")
    messages.see(tk.END)

tk.Button(input_frame, text="💬 Отправить", command=send_message, 
          bg="#32CD32", fg="white", width=12, height=1).pack(side="right", padx=10)

entry.bind("<Return>", lambda e: send_message())

# Стартовое сообщение
messages.insert(tk.END, "🦜 СУПЕР-УМНЫЙ ПОПУГАЙ ЗАПУЩЕН!\n")
messages.insert(tk.END, "Теперь я знаю про английский, игры и Python! 🎉\n")
messages.insert(tk.END, f"\n{persik_ai.name}: {persik_ai.greeting()}\n\n")

chat.mainloop()
