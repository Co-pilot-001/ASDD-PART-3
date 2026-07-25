from number_guess import check_guess

def test_check_guess():
    assert check_guess(50, 30) == "Too low!"
    assert check_guess(50, 70) == "Too high!"
    assert check_guess(50, 50) == "Correct"

if __name__ == "__main__":
    test_check_guess()
    print("All tests passed successfully!")
