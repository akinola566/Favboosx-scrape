# scrape.py
from aviator import Aviator

def main():
    aviator = Aviator()
    aviator.login()
    aviator.go_to_aviator()

    multipliers = aviator.get_multipliers()
    print("Last 30 Aviator multipliers:", multipliers)

    aviator.close()

if __name__ == "__main__":
    main()
