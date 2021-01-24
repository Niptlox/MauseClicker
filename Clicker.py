try:
    import mouse as m
except:
    print("У вас не установлен модуль mause. \nДля установки модуля mause пропишите в командной сторке: pip install mause")
    input("Для выхода нажмите ENTER...")
    exit()

from time import sleep as delay

print("Для старта кликера сделать двойной щелчек по средней кнопке(роллеру)...")

# Примерное количество кликов в секунду
SPEED = 1000
# Размер квадрата в котором может двигаться мышка, не останавливая кликер
SIZE_RECT_MAUSE = 40


run_clicker = False
def clicker(speed):
    global run_clicker
    if run_clicker:
        return
    print("START CLICKER")
    run_clicker = True
    old_pos = m.get_position()
    ox, oy = old_pos
    abs_xy = SIZE_RECT_MAUSE // 2
    sec_s = 1 / speed
    j = 0
    # Число кликов после которого будет показано количество сделанный кликов
    n = 200
    while True:
        i = 0
        while i < n:
            delay(sec_s)
            pos = m.get_position()
            if old_pos != pos:
                x, y = pos
                if abs(oy - y) > abs_xy or abs(ox - x) > abs_xy:
                    run_clicker = False
                    print("STOP CLICKER")
                    return
                    
            old_pos = m.get_position()
            m.click(m.LEFT)
            i += 1
        j += 1
        print(n * j, "clicks")
    

m.on_button(lambda:clicker(SPEED), buttons=[m.MIDDLE], types=[m.DOUBLE])

## Для запуска чере Python IDLE раскоментировать цикл
##while True:
##    pass

input("Чтобы закрыь нажмите ENTER\n")
