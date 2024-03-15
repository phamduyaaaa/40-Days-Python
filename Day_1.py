def calculate_can_chi_calendar(year):
    can_index = year%10
    chi_index = year%12
    can = ['Canh','Tân','Nhâm','Quý','Giáp','Ất','Bính','Đinh','Mậu','Kỷ']
    chi = ['Thân','Dậu','Tuất','Hợi','Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi']
    print("Sinh năm",year,"là:",can[can_index],chi[chi_index])
if __name__ == '__main__':
    calculate_can_chi_calendar(1976)
    calculate_can_chi_calendar(1980)
    calculate_can_chi_calendar(2004)
    calculate_can_chi_calendar(2011)