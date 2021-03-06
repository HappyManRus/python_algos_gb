"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

# Основой оптимизации памяти является постоянный контроль того что и как использует разработчик
# 1. Использовать генераторы
# 2. Использовать классы вместо например Dict
# 3. Одним из основныех способов ухода от Dict считается использование __slots__
# 4. Постоянно удалять неиспользуемые массивы
# 5. Избегать глубоких рекурсий. Особенно если внутрь передаются массивы, т.к. при этом множится использование памяти. Лучше пользоваться генератором для работы рекурсий, где это возможно.