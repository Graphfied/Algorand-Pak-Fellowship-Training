from algopy import ARC4Contract, String,Account, UInt64,Global,itxn ,Bytes
from algopy.arc4 import abimethod


class Contract(ARC4Contract):
    @abimethod()
    def hello(self, name: String) -> String:
        return "Hello, " + name
    
    @abimethod()
    def get_balance(self, account: Account) -> UInt64:
        """
        Returns the balance of the given address.
        """
        return account.balance
    @abimethod()
    def get_total_assets(self,account:Account) ->UInt64:
        return account.total_assets
    @abimethod()
    def get_min_balance(self,account:Account)->UInt64:
        return account.min_balance    
    @abimethod()
    def transfer_algo(self, receiver: Account, amount: UInt64) -> Bytes:
        """
        Transfers the specified amount of microAlgos from the contract account to the receiver.
        Returns the transaction ID.
        """
        payment = itxn.Payment(
            receiver=receiver,
            amount=amount,
            sender=Global.current_application_address,
            fee=1000  # Minimum transaction fee (0.001 ALGO)
        ).submit()
        return payment.txn_id
    
    4000000000.07
    4000000000080000
