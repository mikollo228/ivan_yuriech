class CalendarEvent:
    def __init__(self, title, duration_minutes):
        if duration_minutes <= 0:
            raise ValueError("целое > 0")
        self.title = title
        self.duration_minutes = duration_minutes

    @classmethod
    def from_hours(cls, title, hours):
        minutes = int(hours * 60)
        return cls(title, minutes)

    @staticmethod
    def is_long(duration_minutes):
        return duration_minutes >= 120




# === ДЕМОНСТРАЦИЯ И ПРОВЕРКА ===

# 1. Создаем событие через from_hours (2 часа = 120 минут)
event = CalendarEvent.from_hours("Финальный матч", 2)
print(f"Создано событие: '{event.title}'")
print(f"Длительность: {event.duration_minutes} мин.")

# 2. Проверяем is_long до продления (120 не > 120, должно быть False)
print(f"Является ли долгим до продления? {CalendarEvent.is_long(event.duration_minutes)}")

# 3. Вызываем метод extend для увеличения длительности на 15 минут
print(f"\nСобытие продлено на 15 минут.")
print(f"Новая длительность: {event.duration_minutes} мин.")

# 4. Проверяем is_long после продления (135 > 120, должно быть True)
print(f"Является ли долгим после продления? {CalendarEvent.is_long(event.duration_minutes)}")

