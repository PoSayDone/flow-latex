@user_router.patch("/interests/edit", tags=["interests"])
async def edit_user_interests(
    user: user_dependency, edit: schema.TagsEdit, db: db_dependency
):
    if not user:
        raise HTTPException(status_code=404, detail="Not authorized")
    user.interests = []
    db.commit()
    db.execute(
        insert(models.user_interest_table).values(
            [
                {"user_id": user.id, "interest_id": interest_id}
                for interest_id in edit.tags
            ]
        )
    )
    db.commit()
    return {"ok": True}
