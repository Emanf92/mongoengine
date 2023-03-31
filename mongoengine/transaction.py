from typing import Type


class ITransactionContext:
    def get_current(self):
        return None

    def push_transaction(self, session):
        pass


class TransactionManager:
    context = ITransactionContext()

    @staticmethod
    def init(context: Type[ITransactionContext]):
        TransactionManager.context = context()

    @staticmethod
    def get_context() -> ITransactionContext:
        return TransactionManager.context
