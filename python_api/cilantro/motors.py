class Motors():
    def __init__(self):
        self._m0 = 0
        self._m1 = 0

    @property
    def m0(self) -> float:
        return self._m0

    @m0.setter()
    def m0(self, power: float) -> None:
        self._m0 = power

    @property
    def m1(self) -> float:
        return self._m1

    @m1.setter()
    def m1(self, power: float) -> None:
        self._m1 = power
