class Cinema:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.hall = [[0] * seats_per_row for _ in range(rows)]  

    def show_hall(self):
        #Показывает текущее состояние зала#
        print("          Зал:")
        print("   " + " ".join(str(i+1) for i in range(self.seats_per_row)))  # Номера мест
        for i, row in enumerate(self.hall):
            print(f"{i+1}: " + " ".join('1' if seat == 1 else '0' for seat in row))
        print("[ 0 - свободно, 1 - занято ]\n")

    def book_seats(self, num_seats):
        """Пытается забронировать num_seats мест подряд в одном ряду"""
        for row_num, row in enumerate(self.hall):
            # Ищем num_seats свободных мест подряд в текущем ряду
            for start_seat in range(self.seats_per_row - num_seats + 1):
                # Проверяем, свободны ли num_seats мест подряд
                if all(row[start_seat + i] == 0 for i in range(num_seats)):
                    # Бронируем num_seats мест
                    for i in range(num_seats):
                        row[start_seat + i] = 1
                    
                    booked_seats = [start_seat + 1 + i for i in range(num_seats)]
                    print(f"Успешно забронированы места в ряду {row_num + 1}: {booked_seats}")
                    return True
        
        print(f"Не удалось найти {num_seats} свободных мест подряд ни в одном ряду")
        return False

def main():
    # Создаем кинотеатр с 5 рядами по 10 мест
    cinema = Cinema(rows=5, seats_per_row=10)
    
    print("Кинотеатр")
    
    while True:
        cinema.show_hall()
        
        try:
            num_seats = int(input("Сколько мест подряд вы хотите забронировать? (0 - выход): "))
            if num_seats == 0:
                print("До свидания!")
                break
                
            if num_seats < 1 or num_seats > cinema.seats_per_row:
                print(f"Количество мест должно быть от 1 до {cinema.seats_per_row}")
                continue
                
            cinema.book_seats(num_seats)
            
        except ValueError:
            print("Пожалуйста, введите число")

# Запуск программы
main()
