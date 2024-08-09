class SecurityMeasures:
    def __init__(self):
        self.security_logs = []

    def log_transaction(self, transaction):
        self.security_logs.append(transaction)
        print("Transaction logged for security.")
