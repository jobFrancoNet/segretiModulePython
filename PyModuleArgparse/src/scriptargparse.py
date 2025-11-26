import argparse

parser = argparse.ArgumentParser(description="Esempio con argparse")
parser.add_argument("--nome", required=True, type=str, help="Il tuo nome")
parser.add_argument("--eta", required=True, type=int, help="La tua età")

args = parser.parse_args()

def main(nome,età):
    print(f"Ciao {args.nome}, hai {args.eta} anni!")


if __name__ == "__main__":
    main(args.nome,args.eta)