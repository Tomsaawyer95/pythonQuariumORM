from aquarium_package.models import AlgueORM


def create_algue(
    pv: int = 10,
    age: int = 0,
    id: int | None = None,
    algue_aquarium_id: int | None = None,
    name: str | None = None,
):
    """
    Args:
        pv (int, optional): PV number of the seaweed. Defaults to 10
        age (int, optional): Age of the seaweed. Defaults to 0
        id (int, optional): Id of the seaweed. Defaults to None
        algue_aquarium_id (int, optional): Id of the seaweed. Defaults to None
        name (str, optional): Name of the seaweed. Defaults to None
    Returns:
        AlgueORM
    """
    return AlgueORM(
        pv=pv, id=id, age=age, algue_aquarium_id=algue_aquarium_id, name=name
    )
