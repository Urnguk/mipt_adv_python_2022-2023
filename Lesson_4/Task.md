# Урок 4 - полиморфизм
## Контрольные вопросы:
- Чем классовая переменная отличается от поля? В какой ситуации можно через поле влиять
на поля других экземпляров?
- Как называется типизация в питоне и какой идеей она руководствуется?
- Каким образом мы реализуем полиморфизм для созданных нами объектов?
- Зачем переопределять метод `__radd__()` наравне с 
`__add__()`?

## Задания:
1) Доработайте класс комплексного числа из прошлого занятия: переопределите математические 
операторы (__+, -, /, *, ==__), так, чтобы она 
работали с другими комплексными и со стандартными
числами. Добейтесь правилньой работы с комплексным 
числом функций `print()`, `abs()`, а также
реализуйте обращение к действительной и мнимой части 
комплексного числа через `x[0]` и `x[1]`
соответственно (как для получения так и для присваивания).
2) Доработайте класс двусвязного списка из классного примера: обращение к элементу
по индексу должно занимать не более чем __N/2__ операций, создайте возможность
инициализировать ваш лист заданным набором чисел, добавьте операцию выкидывания
по индексу через метод `pop()` и переопределите оператор сложения двух листов как
их конкатенацию.

