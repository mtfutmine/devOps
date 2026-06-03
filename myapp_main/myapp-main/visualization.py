import matplotlib.pyplot as plt
import seaborn as sns

# Данные о запросах к серверу
request_types = ['GET /', 'POST /data', 'GET /status', 'DELETE /item', 'PUT /update']
request_counts = [120, 45, 80, 15, 30]

# Настройка стиля Seaborn
sns.set_theme(style="whitegrid")

# Создание графика
plt.figure(figsize=(10, 6))
bars = sns.barplot(x=request_types, y=request_counts, palette="Blues_d")

# Подписи значений над столбцами
for bar, count in zip(bars.patches, request_counts):
    bars.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        str(count),
        ha='center',
        va='bottom',
        fontsize=12,
        fontweight='bold'
    )

# Оформление графика
plt.title('Статистика запросов к серверу', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Тип запроса', fontsize=13)
plt.ylabel('Количество запросов', fontsize=13)
plt.tight_layout()

# Сохранение и отображение
plt.savefig('requests_stats.png', dpi=150)
print("График сохранён в файл requests_stats.png")
plt.show()
