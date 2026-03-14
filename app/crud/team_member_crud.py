from bson import ObjectId
from app.core.database import team_collection
from app.models.team_member_model import team_member_helper


async def create_member(member_data: dict):
    result = await team_collection.insert_one(member_data)
    new_member = await team_collection.find_one({"_id": result.inserted_id})
    return team_member_helper(new_member)


async def get_members():
    members = []
    async for member in team_collection.find():
        members.append(team_member_helper(member))
    return members


async def delete_member(member_id: str):
    member = await team_collection.find_one({"_id": ObjectId(member_id)})

    if not member:
        raise Exception("Team member not found")

    await team_collection.delete_one({"_id": ObjectId(member_id)})

    return team_member_helper(member)


async def update_member(member_id: str, update_data: dict):

    member = await team_collection.find_one({"_id": ObjectId(member_id)})

    if not member:
        raise Exception("Team member not found")

    await team_collection.update_one(
        {"_id": ObjectId(member_id)},
        {"$set": update_data}
    )

    updated_member = await team_collection.find_one({"_id": ObjectId(member_id)})

    return team_member_helper(updated_member)