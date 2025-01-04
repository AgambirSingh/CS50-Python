import sys
import requests


def main():

    number_bitcoins = get_number_bitcoins()

    #get the current bitcoin rate value
    bitcoin_rate = get_bitcoin_rate_value()

    amount = number_bitcoins * bitcoin_rate
    print(f"${amount:,.4f}")


def get_number_bitcoins():

    args = sys.argv[1:]
    if len(args) < 1:
        sys.exit("Missing command-line argument")
    elif len(args) > 1:
        sys.exit("Too many command-line arguments")

    try:
        return float(args[0])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_bitcoin_rate_value():

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        rate_float_value = data["bpi"]["USD"]["rate_float"]
        return float(rate_float_value)

    except KeyError:
        sys.exit("No bpi\\USD\\rate_float in the json response of the coindesk API!")
    except ValueError:
        sys.exit("rate_float is not a float value!")
    except requests.RequestException:
        sys.exit(
            "An error occurred when trying to get the bitcoin rate float value, through the coindesk API!"
        )


if __name__ == "__main__":
    main()
