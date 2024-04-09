pusher_client.trigger(
    f"{user.mail}",
    "conversation:new",
    jsonable_encoder(conversation),
)
