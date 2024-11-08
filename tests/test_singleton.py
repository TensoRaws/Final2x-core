from Final2x_core.util import PrintProgressLog, singleton


class Test_Singleton:
    def test_singleton_instance(self) -> None:
        class MyClass:
            def __init__(self, value: int):
                self.value = value

        instance1 = MyClass(1145141919810)
        instance2 = singleton(instance1)  # type: ignore

        assert instance1 == instance2
        assert instance1.value == instance2.value

    def test_progresslog(self) -> None:
        p1 = PrintProgressLog()
        p2 = PrintProgressLog()
        p3 = PrintProgressLog()
        assert p1 == p2 == p3
