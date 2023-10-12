from datetime import datetime


class PortList(object):
    __ports = []

    """Magic Methods"""

    def __init__(self, port_list=None) -> None:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__log(f'Initialization: {now}')
        if port_list is not None:
            for port in port_list:
                if self.__is_valid_port(port):
                    self.__ports.append(int(port))
            self.__ports.sort()

    def __str__(self) -> str:
        return f'This port list have length: {len(self.__ports)}\nPort list: {self.__ports}'

    def __repr__(self) -> str:
        return self.__ports

    """Public Methods"""

    def get_port_list(self) -> list:
        return self.__ports

    def add_port_list(self, port_list: (str, list, int)) -> None:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__log(f'Add: {now}')
        if isinstance(port_list, str) or isinstance(port_list, int):
            if self.__is_valid_port(port_list):
                self.__ports.append(int(port_list))
        elif isinstance(port_list, list):
            for port in port_list:
                if self.__is_valid_port(port):
                    self.__ports.append(port)
        else:
            self.__log(f'Add Error {port_list}: port\\port list for add need to have type string\\int\\list!')
            return
        self.__ports.sort()

    """Private Methods"""

    def __log(self, msg: str) -> None:
        with open('port.log', 'a') as file:
            file.write(msg + '\n')

    def __is_valid_port(self, port: (str, int)) -> bool:
        if isinstance(port, str):
            try:
                port = int(port)
            except ValueError as e:
                self.__log(f'Error {port}: {e}')
                return False
        if port < 1 or port > 65535:
            self.__log(f'Error {port}: port can\'t have a number less than 1 and more than 65535!')
            return False
        return True
