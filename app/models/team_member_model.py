def team_member_helper(member) -> dict:
    return {
        "id": str(member["_id"]),
        "name": member["name"],
        "role": member["role"],
        "bio": member.get("bio"),
        "funFact": member.get("funFact"),
        "photo": member.get("photo"),
        "linkedInUrl": member.get("linkedInUrl"),
        "xUrl": member.get("xUrl"),
    }