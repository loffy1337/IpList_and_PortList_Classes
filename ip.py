from datetime import datetime


class IpList(object):
    __ips = []

    """Magic Methods"""

    def __init__(self, ip_list: list) -> None:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__log(f'Initialization: {now}')
        if ip_list is not None:
            for ip in ip_list:
                if self.__is_valid_ip(ip):
                    self.__ips.append(ip)
            self.__ips.sort()
        self.__log('')

    def __str__(self) -> str:
        return f'This ip list have length: {len(self.__ips)}\nIp list: {self.__ips}'

    def __repr__(self) -> str:
        return self.__ips

    """Public Methods"""

    def get_ip_list(self) -> list:
        return self.__ips

    def add_ip_list(self, ip_list: (str, list)) -> None:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__log(f'Add: {now}')
        if isinstance(ip_list, str):
            if self.__is_valid_ip(ip_list):
                self.__ips.append(ip_list)
        elif isinstance(ip_list, list):
            for ip in ip_list:
                if self.__is_valid_ip(ip):
                    self.__ips.append(ip)
        else:
            self.__log(f'Add Error {ip_list}: ip\\ip list for add need to have type string\\list!')
            return
        self.__log('')
        self.__ips.sort()

    """Private Methods"""

    def __log(self, msg: str) -> None:
        with open('ip.log', 'a') as file:
            file.write(msg + '\n')

    def __is_valid_ip(self, ip: str) -> bool:
        if isinstance(ip, str):
            if len(ip.split('.')) == 4:
                try:
                    ip_nums = list(map(int, list(ip.split('.'))))
                except ValueError as e:
                    self.__log(f'Error {ip}: {e}')
                    return False
                if ip_nums[0] == 0:
                    self.__log(f'Error {ip}: ip can\'t have 0 in first number!')
                    return False
                for ip_num in ip_nums:
                    if ip_num < 0 or ip_num > 255:
                        self.__log(f'Error {ip}: ip can\'t have a number less than 0 and more than 255!')
                        return False
                self.__log(f'Successful {ip}!')
                return True
            self.__log(f'Error {ip}: ip need to have 4 numbers, but this ip have {len(ip.split("."))}!')
            return False
        self.__log(f'Error {ip}: ip need to have type string!')
        return False
