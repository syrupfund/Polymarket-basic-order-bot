from helpers.clob_client import create_clob_client


def get_market(condition_id: str) -> str:
    client = create_clob_client()

    return client.get_market(condition_id=condition_id)
