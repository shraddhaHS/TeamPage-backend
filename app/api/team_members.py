from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from typing import Optional
import cloudinary.uploader

from app.crud.team_member_crud import *

router = APIRouter(prefix="/team-members", tags=["Team Members"])


MAX_FILE_SIZE = 5 * 1024 * 1024
ALLOWED_TYPES = ["image/jpeg", "image/jpg", "image/png"]


def success_response(message: str, data=None):
    return {
        "flag": 1,
        "flagMessage": message,
        "data": data,
        "error": None
    }


def error_response(error_msg: str):
    return {
        "flag": 0,
        "flagMessage": "Operation failed",
        "data": None,
        "error": error_msg
    }


async def upload_image(photo: UploadFile) -> str:
    try:
        if photo.content_type not in ALLOWED_TYPES:
            raise Exception("Only JPG, JPEG, and PNG images are allowed")

        contents = await photo.read()

        if len(contents) > MAX_FILE_SIZE:
            raise Exception("Image size must be less than 5MB")

        result = cloudinary.uploader.upload(contents)

        photo_url = result.get("secure_url")

        if not photo_url:
            raise Exception("Image upload failed")

        return photo_url

    finally:
        await photo.close()


@router.post("")
async def create_team_member(
    name: str = Form(...),
    role: str = Form(...),
    bio: Optional[str] = Form(None),
    funFact: Optional[str] = Form(None),
    photo: Optional[UploadFile] = File(None),
    linkedInUrl: Optional[str] = Form(None),
    xUrl: Optional[str] = Form(None),
):
    try:
        photo_url = None

        if photo:
            photo_url = await upload_image(photo)

        member_data = {
            "name": name,
            "role": role,
            "bio": bio,
            "funFact": funFact,
            "linkedInUrl": linkedInUrl,
            "xUrl": xUrl,
        }

        if photo_url:
            member_data["photo"] = photo_url

        member = await create_member(member_data)

        return success_response(
            "Team member created successfully",
            member
        )

    except Exception as e:
        return error_response(str(e))


@router.get("")
async def list_team_members():
    try:
        members = await get_members()

        return success_response(
            "Team members retrieved successfully",
            members
        )

    except Exception as e:
        return error_response(str(e))


@router.delete("/{member_id}")
async def remove_team_member(member_id: str):
    try:
        member = await delete_member(member_id)

        return success_response(
            "Team member deleted successfully",
            member
        )

    except Exception as e:
        return error_response(str(e))


@router.put("/{member_id}")
async def edit_team_member(
    member_id: str,
    name: Optional[str] = Form(None),
    role: Optional[str] = Form(None),
    bio: Optional[str] = Form(None),
    funFact: Optional[str] = Form(None),
    photo: Optional[UploadFile] = File(None),
    linkedInUrl: Optional[str] = Form(None),
    xUrl: Optional[str] = Form(None),
):
    try:
        update_data = {}

        if name is not None:
            update_data["name"] = name

        if role is not None:
            update_data["role"] = role

        if bio is not None:
            update_data["bio"] = bio

        if funFact is not None:
            update_data["funFact"] = funFact

        if linkedInUrl is not None:
            update_data["linkedInUrl"] = linkedInUrl

        if xUrl is not None:
            update_data["xUrl"] = xUrl

        if photo:
            photo_url = await upload_image(photo)
            update_data["photo"] = photo_url

        member = await update_member(member_id, update_data)

        return success_response(
            "Team member's details updated successfully",
            member
        )

    except Exception as e:
        return error_response(str(e))