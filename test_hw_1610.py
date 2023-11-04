import pytest

link = ("https://www.taiwangun.com/pistols")

class TestPage1:
    @pytest.mark.smoke
    def test_math_1(self, browser):
        browser.get(link)
        result = 150 ** 2  # Возвожу 150 в квадрат
        expected_result = 22500
        assert result == expected_result
        print("Test test_math_1 complite! Well done!")

    @pytest.mark.smoke
    def test_math_2(self, browser):
        browser.get(link)
        result = 20 ** 3  # Возводим 20 в куб
        expected_result = 8000
        assert result == expected_result
        print("Тest_math_2 прошёл успешно!")

    @pytest.mark.regression
    def test_math_3(self, browser):
        browser.get(link)
        num1 = 75
        num2 = 25
        result = num1 + num2
        expected_result = 100
        assert result == expected_result
        print("Выполнен test_math_3")

    @pytest.mark.regression
    def test_math_4(self, browser):
        browser.get(link)
        result = 120 / 2  # Возводим 5 в квадрат
        expected_result = 60
        assert result == expected_result
        print("Выполнен test_math_4")

    @pytest.mark.regression
    def test_math_5(self, browser):
        browser.get(link)
        result = 75 - 6  # Возводим 5 в квадрат
        expected_result = 69
        assert result == expected_result
        print("Выполнен test_math_5")

    @pytest.mark.funct
    def test_math_6(self, browser):
        browser.get(link)
        result = 250 ** 2  # Возводим 5 в квадрат
        expected_result = 62500
        assert result == expected_result
        print("Выполнен test_math_6")

