import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
import os
from eth_account import Account

load_dotenv()

def main():
    rpc = os.getenv("RPC_URL")
    #print(rpc)
    #Connect the rpc to Titanoboa like this below
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    anvil_key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(anvil_key) 
    boa.env.add_account(my_account, force_eoa=True)

    favorites_contract = boa.load("favorites.vy")

    print("Storing a person")
    favorites_contract.add_person("Insha", 22)

    person_data = favorites_contract.list_of_people(0)
    print(f"Person: {person_data}")
    
if __name__ == "__main__":
    main()